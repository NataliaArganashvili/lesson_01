from time import sleep
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/entry_ad")
txt = driver.find_element(By.XPATH, "//button[text()='Close']")
print(txt)
sleep(3)
