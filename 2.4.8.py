import time
import os
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 15).until((
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    )
    button = browser.find_element_by_xpath('//button[contains(text(), "Book")]')
    button.click()

    num = browser.find_element_by_xpath('//span[@id="input_value"]').text
    calc_result = calc(num)
    element = browser.find_element_by_xpath('//input[@id="answer"]')
    element.send_keys(calc_result)

    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    button.click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()
