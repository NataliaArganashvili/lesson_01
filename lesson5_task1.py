from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range (5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

driver.find_elements(By.XPATH, "//button[text()='Delete']")
list_len = len(driver.find_elements(By.XPATH, "//button[text()='Delete']"))
print(f'Длина списка: {list_len}')

