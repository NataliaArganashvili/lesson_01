from time import sleep
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR, '#username')
username.send_keys("tomsmith")
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, 'button').click()

sleep(3)
