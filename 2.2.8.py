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


try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("http://suninjuly.github.io/file_input.html")
    element = browser.find_element_by_xpath('//input[@name="firstname"]')
    element.send_keys('-')
    element = browser.find_element_by_xpath('//input[@name="lastname"]')
    element.send_keys('-')
    element = browser.find_element_by_xpath('//input[@name="email"]')
    element.send_keys('-')
    element = browser.find_element_by_xpath('//input[@type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    time.sleep(5)
    browser.quit()
