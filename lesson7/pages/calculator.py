from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    def set_delay(self, time):
        delay = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(time)

    def click_buttons(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def waiting(self):
        WebDriverWait(self.driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
        
    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text

    