from selenium import webdriver
import time

website = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(website)

num1 = browser.find_element_by_id('num1').text
num2 = browser.find_element_by_id('num2').text
result = int(num1)+int(num2)
print(result)

browser.find_element_by_tag_name('select').click()
browser.find_element_by_css_selector("[value='{}']".format(result)).click()
time.sleep(2)
browser.find_element_by_css_selector('.btn').click()
time.sleep(2)
browser.quit()