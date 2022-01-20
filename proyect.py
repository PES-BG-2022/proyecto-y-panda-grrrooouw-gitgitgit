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

