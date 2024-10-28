from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome()

from pages_shop.main_page import MainPage
from pages_shop.products_page import ProductsPage
from pages_shop.cart_page import CartPage
from pages_shop.checkout_page import CheckoutPage
from pages_shop.overview_page import OverviewPage

def test_shop():
    main_page = MainPage(driver)
    main_page.fill_in_username("standard_user")
    main_page.fill_in_password()
    main_page.click_login()
    
    products_page = ProductsPage(driver)
    products_page.click_elements()
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_in_first_name("Natalia")
    checkout_page.fill_in_last_name("Arganashvili")
    checkout_page.fill_in_postal_code("555555")
    checkout_page.click_continue()

    overview_page = OverviewPage(driver)
    total_price = overview_page.get_total_price()
    assert total_price == 'Total: $58.29'
