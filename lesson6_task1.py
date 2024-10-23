from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.XPATH, "//button[text()='Button Triggering AJAX Request']").click()

sleep(30)

element = driver.find_element(By.CSS_SELECTOR,'#content')
txt = element.text
print(txt)
