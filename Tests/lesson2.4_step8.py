import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(URL)
    print("Ok")
    
    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    browser.find_element_by_css_selector("button.btn").click()
    
    time.sleep(1)    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    
    answer = browser.find_element_by_id("answer").send_keys(y)
    
    browser.find_element_by_id("solve").click()
    
    time.sleep(1)
    
finally:
    time.sleep(10)
    browser.quit()