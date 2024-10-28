from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome()

from pages_form.main_page import MainPage
from pages_form.second_page import SecondPage

def test_form():
    main_page = MainPage(driver)
    main_page.fill_in_first_name("Иван")
    main_page.fill_in_last_name("Петров")
    main_page.fill_in_address("Ленина, 55-3")
    main_page.fill_in_email("test@skypro.com")
    main_page.fill_in_phone_number("+7985899998787")
    main_page.fill_in_city("Москва")
    main_page.fill_in_country("Россия")
    main_page.fill_in_job_position("QA")
    main_page.fill_in_company("SkyPro")
    main_page.click_submit()

    second_page = SecondPage(driver)
    second_page.waiter()
    zip_code_color = second_page.get_zip_code_color()
    first_name_color = second_page.get_first_name_color()
    last_name_color = second_page.get_last_name_color()
    address_color = second_page.get_address_color()
    email_color = second_page.get_email_color()
    phone_number_color = second_page.get_phone_number_color()
    city_color = second_page.get_city_color()
    country_color = second_page.get_country_color()
    job_position_color = second_page.get_job_position_color()
    company_color = second_page.get_company_color()

    assert "danger" in zip_code_color
    assert "success" in first_name_color
    assert "success" in last_name_color
    assert "success" in address_color
    assert "success" in email_color
    assert "success" in phone_number_color
    assert "success" in city_color
    assert "success" in country_color
    assert "success" in job_position_color
    assert "success" in company_color
