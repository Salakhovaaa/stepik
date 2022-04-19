import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//div[@class=\"first_block\"]//input[@class=\"form-control first\"]")
        input1.send_keys("First name")
        input2 = browser.find_element_by_xpath("//div[@class=\"first_block\"]//input[@class=\"form-control second\"]")
        input2.send_keys("Last name")
        input3 = browser.find_element_by_xpath("//div[@class=\"first_block\"]//input[@class=\"form-control third\"]")
        input3.send_keys("Email")
        time.sleep(5)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        #ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "They are not equal, silly")
        
    def test_2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//div[@class=\"first_block\"]//input[@class=\"form-control first\"]")
        input1.send_keys("First name")
        input2 = browser.find_element_by_xpath("//div[@class=\"first_block\"]//input[@class=\"form-control second\"]")
        input2.send_keys("Last name")
        input3 = browser.find_element_by_xpath("//div[@class=\"first_block\"]//input[@class=\"form-control third\"]")
        input3.send_keys("Email")
        time.sleep(5)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        #ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "They are not equal, silly")        


if __name__ == "__main__":
    unittest.main()