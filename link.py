from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
website = 'http://suninjuly.github.io/find_link_text'
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

browser.get(website)
find_link = browser.find_element_by_link_text(link_text)
find_link.click()

input_first_name = browser.find_element_by_tag_name('input')
input_first_name.send_keys('Timur')

input_last_name = browser.find_element_by_name('last_name')
input_last_name.send_keys('Atabaev')

input_city = browser.find_element_by_class_name('city')
input_city.send_keys('Tashkent')

input_country = browser.find_element_by_id('country')
input_country.send_keys('Uzbekistan')

button = browser.find_element_by_css_selector('button.btn')
button.click()
