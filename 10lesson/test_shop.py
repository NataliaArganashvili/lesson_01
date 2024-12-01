from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from pages_shop.main_page import MainPage
from pages_shop.products_page import ProductsPage
from pages_shop.cart_page import CartPage
from pages_shop.checkout_page import CheckoutPage
from pages_shop.overview_page import OverviewPage

driver = webdriver.Chrome()

@allure.title("Проверка сайта магазина")
@allure.description("Проверка вычисления полной суммы заказа")
@allure.feature("COUNT") 
@allure.severity("critical")

def test_shop():
    with allure.step("Вход на страницу магазина"):
        main_page = MainPage(driver)
    with allure.step("Заполнение поля Username"):
        main_page.fill_in_username("standard_user")
    with allure.step("Заполнение поля password"):
        main_page.fill_in_password()
    with allure.step("Нажатие на кнопку login"):
        main_page.click_login()
    
    with allure.step("Создание страницы продуктов"):
        products_page = ProductsPage(driver)
    with allure.step("Выбор продуктов"):
        products_page.click_elements()
    with allure.step("Переход в корзину"):
        products_page.go_to_cart()

    with allure.step("Создание страницы корзины"):
        cart_page = CartPage(driver)
    with allure.step("Переход в checkout"):
        cart_page.go_to_checkout()

    with allure.step("Создание страницы checkout"):
        checkout_page = CheckoutPage(driver)
    with allure.step("Заполнение поля first_name"):
        checkout_page.fill_in_first_name("Natalia")
    with allure.step("Заполнение поля last_name"):
        checkout_page.fill_in_last_name("Arganashvili")
    with allure.step("Заполнение поля postal_code"):
        checkout_page.fill_in_postal_code("555555")
    with allure.step("Нажатие на кнопку Continue"):
        checkout_page.click_continue()

    with allure.step("Создание страницы Overview"):
        overview_page = OverviewPage(driver)
    with allure.step("Получение общей суммы заказа"):
        total_price = overview_page.get_total_price()
    with allure.step("Проверка общий суммы заказа"):
        assert total_price == 'Total: $58.29'