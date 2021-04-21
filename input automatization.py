from selenium import webdriver
import time

link = 'http://suninjuly.github.io/simple_form_find_task.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #time.sleep(1)

    input_first_name = browser.find_element_by_tag_name('input')
    input_first_name.send_keys('Timur')
    #time.sleep(1)

    input_last_name = browser.find_element_by_name('last_name')
    input_last_name.send_keys('Atabaev')
    #time.sleep(1)

    input_city = browser.find_element_by_class_name('city')
    input_city.send_keys('Tashkent')
    #time.sleep(1)

    input_country = browser.find_element_by_id('country')
    input_country.send_keys('Uzbekistan')
    #time.sleep(1)

    button = browser.find_element_by_id('submit_button')
    button.click()
    #time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(25)
    # закрываем браузер после всех манипуляций
    browser.quit()

