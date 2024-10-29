from selenium.webdriver.common.by import By
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
        self.driver.find_element(By.ID, "job-position").get_attribute("class")
    
    def get_company_color(self):
        self.driver.find_element(By.ID, "company").get_attribute("class")
