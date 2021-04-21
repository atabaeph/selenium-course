from selenium import webdriver
import time

website = 'http://suninjuly.github.io/find_xpath_form'
xpath = "//button[@type='submit']"

try:
    browser = webdriver.Chrome()
    browser.get(website)

    input_first_name = browser.find_element_by_tag_name('input')
    input_first_name.send_keys('Timur')

    input_last_name = browser.find_element_by_name('last_name')
    input_last_name.send_keys('Atabaev')

    input_city = browser.find_element_by_class_name('city')
    input_city.send_keys('Tashkent')

    input_country = browser.find_element_by_id('country')
    input_country.send_keys('Uzbekistan')

# X PATH
    button = browser.find_element_by_xpath(xpath)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(25)
    # закрываем браузер после всех манипуляций
    browser.quit()