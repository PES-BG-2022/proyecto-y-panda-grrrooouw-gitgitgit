############# APLICACIÓN DE PRONÓSTICOS ############

import time
import datetime as dt
import datetime
from openpyxl import Workbook
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


from operator import index
from io import BytesIO
from prophet import Prophet
from prophet.plot import plot_plotly

### Preliminares

def date(y, m, d):

    period = int(time.mktime(datetime.datetime(y, m, d, 23, 59).timetuple()))
    return period

#inicio = date(2000, 1, 1)
hoy = int(time.mktime(datetime.datetime.now().timetuple()))

# Dashboard

st.title('App de pronósticos: Martín Cordón y Erick Ruíz -grrrrrraaaaww GITGITGIT')

inicio = st.date_input('Introduzca una fecha', datetime.datetime(2000, 1, 1, 23, 59))
inicio2 = int(time.mktime(inicio.timetuple()))

ticker = st.text_input('Introduzca el "ticker" del activo que desea analizar', "PZZA")

interval = st.selectbox('Escoja un intervalo de tiempo', ['1d', '1wk', '1mo'])

n_years = st.slider('Años de pronóstico:', 1, 4)

if interval == '1d':

    periodo = n_years * 365

elif interval == '1wk':

    periodo = n_years * 52

else:

    periodo = n_years * 12

# Query

@st.cache
def fin_data(ticker: str):
    
    qstr = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={inicio2}&period2={hoy}&interval={interval}&events=history&includeAdjustedClose=true'

    datos = pd.read_csv(qstr)

    return datos

loadstate_datos = st.text('Cargando datos...')
data = fin_data(ticker)
loadstate_datos.text('Cargando datos... listo!!')

st.subheader('Datos crudos')
st.write(data.tail())

# Descarga de datos

@st.cache
def xls_df(df):

    output = BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'})
    worksheet.set_column('A:A', None, format1)
    writer.save()
    processed_data = output.getvalue()
    return processed_data

xlsx = xls_df(data)

st.download_button(label='Descarga los datos en formato Excel',
                   data=xlsx,
                   file_name=f'historical_prices_{ticker}.xlsx')

# Candelas

def candle():

    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'])])
    fig.layout.update(title_text=f'Gráfico de candelas interactivo para {ticker}', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

candle()

# Prophet

df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=periodo)
forecast = m.predict(future)

st.subheader('Datos pronosticados')
st.write(forecast.tail())

st.write(f'Pronóstico para {n_years} años')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Componentes del pronóstico")
fig2 = m.plot_components(forecast)
st.write(fig2)