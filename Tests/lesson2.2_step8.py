import time
import math
import os
from selenium import webdriver

URL = 'http://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')


try:
    browser = webdriver.Chrome()
    browser.get(URL)    
    print("Ok")
    
    first_name = browser.find_element_by_name("firstname").send_keys("Somename")
    last_name = browser.find_element_by_name("lastname").send_keys("Somelastname")
    email = browser.find_element_by_name("email").send_keys("Some@email.com")
    
    addfile = browser.find_element_by_id("file").send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    time.sleep(1)
    
finally:
    time.sleep(10)
    browser.quit()