from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome()

from pages.calculator import Calculator

@allure.title("Проверка калькулятора")
@allure.description("Проверка калькулятора с ожиданием результата")
@allure.feature("COUNT") 
@allure.severity("blocker")

def test_calculator():
    with allure.step("создание клькулятора"):
        calculator = Calculator(driver)
    with allure.step("Передача длины ожидания"):
        calculator.set_delay("45")
    with allure.step("Ввод данных для вычисления"):
        calculator.click_buttons()
    with allure.step("Ожидание"):
        calculator.waiting()
    with allure.step("Получение результата"):
        as_is = calculator.get_result()
    with allure.step("Проверка"):
        assert as_is == "15"
