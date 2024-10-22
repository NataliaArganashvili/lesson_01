from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

driver.find_element(By.CSS_SELECTOR, '#f2cf7343-1874-9b19-f7a8-b2e378830bb5').click

sleep(5)
