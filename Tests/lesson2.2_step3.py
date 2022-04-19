import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

URL = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(URL)    
    print("Ok")   
    
    x = browser.find_element_by_id("num1").text
    x = int(x)
    print(x)
    y = browser.find_element_by_id("num2").text
    y = int(y)
    print(y)
    summ = x+y
    print(summ)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ))
        
    browser.find_element_by_css_selector("button.btn").click()
    
    time.sleep(1)
    
finally:
    time.sleep(10)
    browser.quit()