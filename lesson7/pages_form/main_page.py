from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    def fill_in_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)

    def fill_in_last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)

    def fill_in_address(self, address):
        self.driver.find_element(By.CSS_SELECTOR, '.form-control[name="address"]').send_keys(address)

    def fill_in_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(email)

    def fill_in_phone_number(self, phone_number):
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone_number)

    def fill_in_city(self, city):
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)

    def fill_in_country(self, country):
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)

    def fill_in_job_position(self, job_position):
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)

    def fill_in_company(self, company):
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()



    