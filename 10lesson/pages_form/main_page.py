from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    def fill_in_first_name(self, first_name: str) -> None:
        """Заполнение поля First name"""
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)

    def fill_in_last_name(self, last_name: str) -> None:
        """Заполнение поля Last name"""
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)

    def fill_in_address(self, address: str) -> None:
        """Заполнение поля Address"""
        self.driver.find_element(By.CSS_SELECTOR, '.form-control[name="address"]').send_keys(address)

    def fill_in_email(self, email: str) -> None:
        """Заполнение поля E-mail"""
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(email)

    def fill_in_phone_number(self, phone_number: str) -> None:
        """Заполнение поля Phone number"""
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone_number)

    def fill_in_city(self, city: str) -> None:
        """Заполнение поля City"""
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)

    def fill_in_country(self, country: str) -> None:
        """Заполнение поля Country"""
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)

    def fill_in_job_position(self, job_position: str) -> None:
        """Заполнение поля Job_position"""
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)

    def fill_in_company(self, company: str) -> None:
        """Заполнение поля Company"""
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def click_submit(self) -> None:
        """Нажатие на кнопку Submit"""
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    
    def waiter(self) -> None:
        """Ожидание окрашивания полей"""
        WebDriverWait(self.driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.alert.py-2.alert-danger'))
)


    def get_zip_code_color(self) ->str: 
        """Получение цвета поля Zip-code"""
        return self.driver.find_element(By.ID, "zip-code").get_attribute("class")
        
    def get_first_name_color(self) ->str:
        """Получение цвета поля First name"""
        return self.driver.find_element(By.ID, "first-name").get_attribute("class")

    def get_last_name_color(self) ->str:
        """Получение цвета поля Last name"""
        return self.driver.find_element(By.ID, "last-name").get_attribute("class")
    
    def get_address_color(self) ->str:
        """Получение цвета поля Address"""
        return self.driver.find_element(By.ID, "address").get_attribute("class")
    
    def get_email_color(self) ->str:
        """Получение цвета поля E-mail"""
        return self.driver.find_element(By.ID, "e-mail").get_attribute("class")

    def get_phone_number_color(self) ->str:
        """Получение цвета поля Phone number"""
        return self.driver.find_element(By.ID, "phone").get_attribute("class")
    
    def get_city_color(self) ->str:
        """Получение цвета поля City"""
        return self.driver.find_element(By.ID, "city").get_attribute("class")
    
    def get_country_color(self) ->str:
        """Получение цвета поля Country"""
        return self.driver.find_element(By.ID, "country").get_attribute("class")
    
    def get_job_position_color(self) ->str:
        """Получение цвета поля Job-position"""
        return self.driver.find_element(By.ID, "job-position").get_attribute("class")
    
    def get_company_color(self) ->str:
        """Получение цвета поля Company"""
        return self.driver.find_element(By.ID, "company").get_attribute("class")