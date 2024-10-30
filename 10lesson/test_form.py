from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome()

from pages_form.main_page import MainPage

@allure.title("Проверка заполнения формы")
@allure.description("Проверка обязательности заполнения всех полей формы")
@allure.feature("FILL IN") 
@allure.severity("S3")

def test_form():
    with allure.step("создание клькулятора"):
        main_page = MainPage(driver)
    with allure.step("Заполнение поля First name"):
        main_page.fill_in_first_name("Иван")
    with allure.step("Заполнение поля Last name"):
        main_page.fill_in_last_name("Петров")
    with allure.step("Заполнение поля address"):
        main_page.fill_in_address("Ленина, 55-3")
    with allure.step("Заполнение поля email"):
        main_page.fill_in_email("test@skypro.com")
    with allure.step("Заполнение поля phone_number"):
        main_page.fill_in_phone_number("+7985899998787")
    with allure.step("Заполнение поля city"):
        main_page.fill_in_city("Москва")
    with allure.step("Заполнение поля country"):
        main_page.fill_in_country("Россия")
    with allure.step("Заполнение поля job_position"):
        main_page.fill_in_job_position("QA")
    with allure.step("Заполнение поля company"):
        main_page.fill_in_company("SkyPro")
    with allure.step("Нажатие на кнопку Submit"):
        main_page.click_submit()

    with allure.step("Ожидание"):
        main_page.waiter()
    with allure.step("Получение цвета поля Zip-code"):
        zip_code_color = main_page.get_zip_code_color()
    with allure.step("Получение цвета поля first_name"):
        first_name_color = main_page.get_first_name_color()
    with allure.step("Получение цвета поля last_name"):
        last_name_color = main_page.get_last_name_color()
    with allure.step("Получение цвета поля address"):
        address_color = main_page.get_address_color()
    with allure.step("Получение цвета поля email"):
        email_color = main_page.get_email_color()
    with allure.step("Получение цвета поля phone_number"):
        phone_number_color = main_page.get_phone_number_color()
    with allure.step("Получение цвета поля city"):
        city_color = main_page.get_city_color()
    with allure.step("Получение цвета поля country"):
        country_color = main_page.get_country_color()
    with allure.step("Получение цвета поля job_position"):
        job_position_color = main_page.get_job_position_color()
    with allure.step("Получение цвета поля company"):
        company_color = main_page.get_company_color()

    with allure.step("Проверка цвета плоля zip_code"):
        assert "danger" in zip_code_color
    with allure.step("Получение цвета поля first_name"):
        assert "success" in first_name_color
    with allure.step("Получение цвета поля last_name"):
        assert "success" in last_name_color
    with allure.step("Получение цвета поля address"):
        assert "success" in address_color
    with allure.step("Проверка цвета плоля email"):
        assert "success" in email_color
    with allure.step("Проверка цвета плоля phone_number"):
        assert "success" in phone_number_color
    with allure.step("Проверка цвета плоля city"):
        assert "success" in city_color
    with allure.step("Проверка цвета плоля country"):
        assert "success" in country_color
    with allure.step("Проверка цвета плоля job_position"):
        assert "success" in job_position_color
    with allure.step("Проверка цвета плоля company"):
        assert "success" in company_color
