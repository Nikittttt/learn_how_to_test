import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")


try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("http://suninjuly.github.io/registration1.html")
    element = browser.find_element_by_xpath('//div[@class="first_block"] //input[@class="form-control first"]')
    element.send_keys("First name")
    element = browser.find_element_by_xpath('//div[@class="first_block"] //input[@class="form-control second"]')
    element.send_keys("Last name")
    element = browser.find_element_by_xpath('//div[@class="first_block"] //input[@class="form-control third"]')
    element.send_keys("Email")

    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
