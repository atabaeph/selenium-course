from selenium import webdriver
import time
import math

def calc_func(x):
    calc = str(math.log(abs(12 * math.sin(int(x)))))
    return calc

website = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(website)

x = browser.find_element_by_id('treasure').get_attribute('valuex')
calc = calc_func(x)

browser.find_element_by_css_selector('#answer').send_keys(calc)

browser.find_element_by_css_selector('#robotCheckbox').click()

browser.find_element_by_css_selector('#robotsRule').click()

browser.find_element_by_css_selector('.btn').click()

time.sleep(55)
browser.quit()