import time
from selenium import webdriver
import math
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("http://suninjuly.github.io/get_attribute.html")
    num = browser.find_element_by_xpath('//img[@id="treasure"]').get_attribute('valuex')
    calc_result = calc(num)
    element = browser.find_element_by_xpath('//input[@id="answer"]')
    element.send_keys(calc_result)
    element = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    element.click()
    element = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    element.click()

    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()


finally:
    time.sleep(5)
    browser.quit()