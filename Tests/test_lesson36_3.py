import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    yield browser
    print("\nquit browser..")
    browser.quit()





class TestMainPage1():
    @pytest.mark.parametrize('paramlink', ["https://stepik.org/lesson/236895/step/1"])
    def test_type_answer(self, browser, paramlink):
        link = f"{paramlink}"
        browser.get(link)
    
        time.sleep(10)
    
        answer = math.log(int(time.time()))
        print(answer)
        
        field = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.ID, "ember89"))
        )
        
        typeanswer = browser.find_element_by_id("ember89").send_keys(answer)
        print("yes")
    
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        browser.find_element_by_class_name("submit-submission").click()
    
        smart = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "smart-hints__hint"))
        )
    
        correct = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "smart-hints__hint")), "Correct!"
        )
        print("we got correct")
    