############# APLICACIÓN DE PRONÓSTICOS ############

import time
import datetime

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly

### Preliminares

def date(y, m, d):

    period = int(time.mktime(datetime.datetime(y, m, d, 23, 59).timetuple()))
    return period

inicio = date(2000, 1, 1)
hoy = int(time.mktime(datetime.datetime.now().timetuple()))
interval = '1mo' # 1d, 1wk

# Dashboard

st.title('App de pronósticos')

ticker = st.text_input('Introduzca el "ticker" del activo que desea analizar')

n_years = st.slider('Años de pronóstico:', 1, 4)
periodo = n_years * 365

# Query

@st.cache
def fin_data(ticker: str):

    qstr = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={inicio}&period2={hoy}&interval={interval}&events=history&includeAdjustedClose=true'

    datos = pd.read_csv(qstr)

    return datos

loadstate_datos = st.text('Cargando datos...')
data = fin_data(ticker)
loadstate_datos.text('Cargando datos... listo!!')

st.subheader('Datos crudos')
st.write(data.tail())

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

# Descarga de datos

def save(df):

    df.to_excel(f'historical_prices_{ticker}.xlsx', sheet_name=ticker, index=False)

st.download_button(label='Descarga los datos', data=save(data))

# Prophet

# df_train = data[['Date','Close']]
# df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# m = Prophet()
# m.fit(df_train)
# future = m.make_future_dataframe(periods=periodo)
# forecast = m.predict(future)

# st.subheader('Datos pronosticados')
# st.write(forecast.tail())

# st.write(f'Proóstico para {n_years} años')
# fig1 = plot_plotly(m, forecast)
# st.plotly_chart(fig1)

# st.write("Componentes del pronóstico")
# fig2 = m.plot_components(forecast)
# st.write(fig2)