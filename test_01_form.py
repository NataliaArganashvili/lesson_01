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
    Zip_code = driver.find_element(By.CSS_SELECTOR, '#zip-code')
    color_zip_code = Zip_code.get_attribute("style")
    
    First_name_colored = driver.find_element(By.CSS_SELECTOR, '#first-name')
    color_first_name = First_name_colored.get_attribute("style")
    
    last_name_colored = driver.find_element(By.CSS_SELECTOR, '#last-name')
    color_last_name = last_name_colored.get_attribute("style")

    address_colored = driver.find_element(By.CSS_SELECTOR, '#address')
    color_address = address_colored.get_attribute("style")

    email_colored = driver.find_element(By.CSS_SELECTOR, '#e-mail')
    color_email = email_colored.get_attribute("style")

    phone_number_colored = driver.find_element(By.CSS_SELECTOR, '#phone')
    color_phone_number = phone_number_colored.get_attribute("style")

    city_colored = driver.find_element(By.CSS_SELECTOR, '#city')
    color_city = city_colored.get_attribute("style")

    country_colored = driver.find_element(By.CSS_SELECTOR, '#country')
    color_country = country_colored.get_attribute("style")

    job_position_colored = driver.find_element(By.CSS_SELECTOR, '#job-position')
    color_job_position = job_position_colored.get_attribute("style")

    company_colored = driver.find_element(By.CSS_SELECTOR, '#company')
    color_company = company_colored.get_attribute("style")


    assert color_zip_code == "rgba(255, 0, 0, 1)"
    assert color_first_name == "rgba(0, 128, 0, 1)"
    assert color_last_name == "rgba(0, 128, 0, 1)"
    assert color_address == "rgba(0, 128, 0, 1)"
    assert color_email == "rgba(0, 128, 0, 1)"
    assert color_phone_number == "rgba(0, 128, 0, 1)"
    assert color_city == "rgba(0, 128, 0, 1)"
    assert color_country == "rgba(0, 128, 0, 1)"
    assert color_job_position == "rgba(0, 128, 0, 1)"
    assert color_company == "rgba(0, 128, 0, 1)"
