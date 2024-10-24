from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.CSS_SELECTOR, '#user-name')
username.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys("secret_sauce")

driver.find_element(By.CSS_SELECTOR, '#login-button').click()

#sleep(3)

driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

#sleep(3)

driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

#sleep(3)

driver.find_element(By.CSS_SELECTOR, '#checkout').click()
#sleep(3)

first_name = driver.find_element(By.CSS_SELECTOR, '#firstName')
first_name.send_keys("Natalia")

last_name = driver.find_element(By.CSS_SELECTOR, '#lastName')
last_name.send_keys("Arganashvili")

postal_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
postal_code.send_keys("125475")

driver.find_element(By.CSS_SELECTOR, '#continue').click()



total_price = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
print(total_price)


