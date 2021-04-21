from selenium import webdriver
import time

website = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(website)
    elements = browser.find_elements_by_tag_name('input')
    print(elements)
    print(type(elements))
    for element in elements:
        element.send_keys('salam')

    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()

