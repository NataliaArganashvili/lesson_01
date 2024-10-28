from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.implicitly_wait(5)

First_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
First_name.send_keys("Иван")

Last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
Last_name.send_keys("Петров")

Address = driver.find_element(By.CSS_SELECTOR, '.form-control[name="address"]')
Address.send_keys("Ленина, 55-3")

Email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
Email.send_keys("test@skypro.com")

Phone_number = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
Phone_number.send_keys("+7985899998787")

City = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
City.send_keys("Москва")

Country = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
Country.send_keys("Россия")

Job_position = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
Job_position.send_keys("QA")

Company = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
Company.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.alert.py-2.alert-danger'))
)

def test_form():
    zip_code_color = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "danger" in zip_code_color

    first_name_color = driver.find_element(By.ID, "first-name").get_attribute("class")
    assert "success" in first_name_color
    
    last_name_color = driver.find_element(By.ID, "last-name").get_attribute("class")
    assert "success" in last_name_color

    address_color = driver.find_element(By.ID, "address").get_attribute("class")
    assert "success" in address_color

    email_color = driver.find_element(By.ID, "e-mail").get_attribute("class")
    assert "success" in email_color

    phone_number_color = driver.find_element(By.ID, "phone").get_attribute("class")
    assert "success" in phone_number_color

    city_color = driver.find_element(By.ID, "city").get_attribute("class")
    assert "success" in city_color

    country_color = driver.find_element(By.ID, "country").get_attribute("class")
    assert "success" in country_color

    job_position_color = driver.find_element(By.ID, "job-position").get_attribute("class")
    assert "success" in job_position_color

    company_color = driver.find_element(By.ID, "company").get_attribute("class")
    assert "success" in company_color
