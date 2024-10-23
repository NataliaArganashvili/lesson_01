from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(20)

driver.find_element(By.XPATH, "//button[text()='Button Triggering AJAX Request']").click()

content = driver.find_element(By.CSS_SELECTOR,'#content')
txt = content.find_element(By.CSS_SELECTOR,'p.bg-success').text
print(txt)
