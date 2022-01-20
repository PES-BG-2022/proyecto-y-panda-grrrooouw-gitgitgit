import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Buscar orden de : ID, name y por ultimo class

driver.get("https://finance.yahoo.com/")
print(driver.title)

#ID: del buscador donde escribe el usuario
search = driver.find_element_by_name("yfin-usr-qry")
search.send_keys("S&P 500")
search.send_keys(Keys.RETURN)

Historical_data = driver.find_element_by_xpath("href=/quote/%5EGSPC/history?p=%5EGSPC")

try:
    element = WebDriverWait(driver, 15).until((EC.presence_of_all_elements_located(By.find_element_by_xpath, Historical_data))
    )
    element.click()
except:
    driver.quit()










#time.sleep(5)
#driver.quit()

#*************************************************************************************************************

# DATE

def date(y, m, d):

    period = int(time.mktime(datetime.datetime(y, m, d, 23, 59).timetuple()))
    return period

date1 = date(2020, 1, 1)
date2 = date(2021, 12, 31)

# QUERY

ticker = 'AAPL'
interval = '1mo' # 1d, 1wk

def fin_data(ticker: str, date1: int, date2: int, interval: str):

    qstr = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={date1}&period2={date2}&interval={interval}&events=history&includeAdjustedClose=true'

    return pd.read_csv(qstr)

# CANDLESTICK

def candle(df):

    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])

    fig_w = go.FigureWidget(fig)

    return fig_w

# SAVE

def save(df):

    df.to_excel(f'historical_prices_{ticker}.xlsx', sheet_name=ticker, index=False)

def save_mult():

    writer = pd.ExcelWriter('historical_prices.xlsx')

    for t in tickers:

        df = fin_data(t, date1, date2, interval)
        df.to_excel(writer, sheet_name=t, index=False)

    writer.save()