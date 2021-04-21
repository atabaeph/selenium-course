import os
from selenium import webdriver
import time

website = 'http://suninjuly.github.io/file_input.html'

file_path = os.path.join(os.getcwd(), 'notice')

browser = webdriver.Chrome()
browser.get(website)
browser.find_element_by_css_selector(" [name='firstname'] ").send_keys('Timur')
browser.find_element_by_css_selector(" [name='lastname'] ").send_keys('Atabaev')
browser.find_element_by_css_selector(" [name='email'] ").send_keys('g@g.com')
browser.find_element_by_css_selector('#file').send_keys(file_path)
browser.find_element_by_css_selector(" [type='submit'] ").click()
time.sleep(3)
browser.quit()
