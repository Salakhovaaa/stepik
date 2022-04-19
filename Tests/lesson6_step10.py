import time

from selenium import webdriver

URL_old = 'http://suninjuly.github.io/registration1.html'
URL_new = 'http://suninjuly.github.io/registration2.html'

try:
    driver = webdriver.Chrome()
    driver.get(URL_old)
    
    field_name = driver.find_element(By.CSS_SELECTOR, 'div.first_block input.first').send_keys('Test')
    field_surname = driver.find_element(By.CSS_SELECTOR, 'div.first_block input.second').send_keys('Test')
    field_email = driver.find_element(By.CSS_SELECTOR, 'div.first_block input.third').send_keys('Test')
    time.sleep(10)
    
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    
    time.sleep(1)
    
    welcome_text_el = driver.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_el.text
    
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    time.sleep(10)
    driver.quit()