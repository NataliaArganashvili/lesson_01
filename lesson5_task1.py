from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")


for x in range (6):
    driver.find_element(By.LINK_TEXT, "Add Element").click()

driver.find_elements(By.LINK_TEXT, "Delete")

sleep(5)
