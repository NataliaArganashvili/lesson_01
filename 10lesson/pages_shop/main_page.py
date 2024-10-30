from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def fill_in_username(self, name: str) ->None:
        """Заполнение поля Username"""
        username = self.driver.find_element(By.CSS_SELECTOR, '#user-name')
        username.send_keys(name)

    def fill_in_password(self: str) ->None:
        """Заполнение поля Password"""
        password = self.driver.find_element(By.CSS_SELECTOR, '#password')
        password.send_keys("secret_sauce")

    def click_login(self: str) ->None:
        """Нажатие на кнопку Login"""
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()



    
        