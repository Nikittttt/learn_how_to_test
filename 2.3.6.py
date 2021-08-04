import time
import os
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


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element_by_xpath('//button[contains(text(), "I want to go on a magical journey!")]')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    num = browser.find_element_by_xpath('//span[@id="input_value"]').text
    calc_result = calc(num)
    element = browser.find_element_by_xpath('//input[@id="answer"]')
    element.send_keys(calc_result)

    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()


finally:
    print(browser.switch_to.alert.text)
    browser.quit()
