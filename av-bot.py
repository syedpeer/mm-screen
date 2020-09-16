from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# creates new Selenium driver object
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# The below downloads full time series daily csv file for every ticker in your "stock-names.txt" file. Go to https://www.alphavantage.co/documentation/ for more information.
# Note: You must use your own API key. Also note that AlphaVantage limits the number of calls per minute you can make to their server with a free account. You can manipulate the time.sleep function below to avoid making too many calls too quickly.
f = open("stock-names.txt", "r")
for x in f:
    str = x
    ph = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + str + "&apikey=[YOUR-AV-API-KEY]&outputsize=full&datatype=csv"
    driver.get(ph)
    time.sleep(20)
