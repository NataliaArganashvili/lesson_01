from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

driver.find_element(By.CLASS_NAME, ('.class1')).click

sleep(5)