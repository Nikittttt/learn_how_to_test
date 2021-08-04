import time
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")

try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("http://suninjuly.github.io/selects1.html")
    num1 = int(browser.find_element_by_xpath('//span[@id="num1"]').text)
    num2 = int(browser.find_element_by_xpath('//span[@id="num2"]').text)
    select = Select(browser.find_element_by_xpath('//select[@id="dropdown"]'))
    select.select_by_value(str(num1+num2))

    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()


finally:
    time.sleep(5)
    browser.quit()
