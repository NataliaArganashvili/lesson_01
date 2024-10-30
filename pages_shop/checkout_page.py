from selenium.webdriver.common.by import By

class CheckoutPage:
    
    def __init__(self, driver):
        self.driver = driver
        
    def fill_in_first_name(self, name):
        first_name = self.driver.find_element(By.CSS_SELECTOR, '#first-name')
        first_name.send_keys(name)

    def fill_in_last_name(self, surname):
        last_name = self.driver.find_element(By.CSS_SELECTOR, '#last-name')
        last_name.send_keys(surname)

    def fill_in_postal_code(self, code):
        postal_code = self.driver.find_element(By.CSS_SELECTOR, '#postal-code')
        postal_code.send_keys(code)

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()
