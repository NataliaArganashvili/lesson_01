from selenium.webdriver.common.by import By

class OverviewPage:
    
    def __init__(self, driver):
        self.driver = driver

    def get_total_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text