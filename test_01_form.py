from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

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

#Zip_code = driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')
#Zip_code.send_keys("Иван")

City = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
City.send_keys("Москва")

Country = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
Country.send_keys("Россия")

Job_position = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
Job_position.send_keys("QA")

Company = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
Company.send_keys("SkyPro")

driver.find_element(By.TAG_NAME, 'button').click()

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.alert py-2 alert-danger'))
)
company_color = Company.get_attribute("style")
print(company_color)
