from pages.calculator import Calculator
from selenium import webdriver
browser = webdriver.Chrome()

def test_calculator():
    calculator = Calculator(browser)
    calculator.set_delay("45")
    calculator.click_buttons
    calculator.waiting
    as_is = calculator.get_result

    assert as_is == "15"
