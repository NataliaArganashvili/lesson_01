from selenium.webdriver.common.by import By

class CartPage:
    
    def __init__(self, driver):
        self.driver = driver
        
    def go_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()