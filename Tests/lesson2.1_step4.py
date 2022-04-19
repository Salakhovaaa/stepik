import time
import math

from selenium import webdriver

URL = ' http://suninjuly.github.io/math.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(URL)
    
    print("Ok")
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    
    answer = browser.find_element_by_id("answer").send_keys(y)
    time.sleep(1)
    
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()
    
    browser.find_element_by_css_selector("button.btn").click()
    
    time.sleep(1)
    
finally:
    time.sleep(10)
    browser.quit()