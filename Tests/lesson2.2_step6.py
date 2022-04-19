import time
import math

from selenium import webdriver

URL = 'http://suninjuly.github.io/execute_script.html'

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
    
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    time.sleep(1)
    
finally:
    time.sleep(10)
    browser.quit()