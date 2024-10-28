from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SecondPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    def waiter(self):
        WebDriverWait(self.driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.alert.py-2.alert-danger'))
)
    
    def get_zip_code_color(self): 
        self.driver.find_element(By.ID, "zip-code").get_attribute("class")

    def get_first_name_color(self):
        self.driver.find_element(By.ID, "first-name").get_attribute("class")

    def get_last_name_color(self):
        self.driver.find_element(By.ID, "last-name").get_attribute("class")
    
    def get_address_color(self):
        self.driver.find_element(By.ID, "address").get_attribute("class")
    
    def get_email_color(self):
        self.driver.find_element(By.ID, "e-mail").get_attribute("class")

    def get_phone_number_color(self):
        self.driver.find_element(By.ID, "phone").get_attribute("class")
    
    def get_city_color(self):
        self.driver.find_element(By.ID, "city").get_attribute("class")
    
    def get_country_color(self):
        self.driver.find_element(By.ID, "country").get_attribute("class")
    
    def get_job_position_color(self):
        self.company_colordriver.find_element(By.ID, "job-position").get_attribute("class")
    
    def get_company_color(self):
        self.driver.find_element(By.ID, "company").get_attribute("class")
