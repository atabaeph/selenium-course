from selenium import webdriver
import time

try:
    website = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(website)


    input_first_name = browser.find_element_by_css_selector('.first_block > .first_class > input.form-control')
    input_first_name.send_keys('Timur')

    input_second_name = browser.find_element_by_css_selector('.first_block > .second_class > input.form-control')
    input_second_name.send_keys('Timurov')

    input_email = browser.find_element_by_css_selector('.first_block > .third_class > input.form-control')
    input_email.send_keys('Timur@gmail.com')

    submit_button = browser.find_element_by_css_selector('.btn')
    submit_button.click()

finally:
    time.sleep(3)
    browser.quit()
