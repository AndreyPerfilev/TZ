import allure

from pages.auth_page import MethodsAuth, LocatorsAuthPage
from pages.products import MethodsProducts


class TestAuthPage:
    @allure.title('Позитивная проверка страницы авторизации')
    def test_positive_auth_page(self, driver):
        test_auth_page = MethodsAuth(driver)
        test_auth_page.open()
        test_auth_page.max_window()
        test_auth_page.send_user_name(LocatorsAuthPage.login)
        test_auth_page.send_password(LocatorsAuthPage.password)
        test_auth_page.click_login()
        test_product_page = MethodsProducts(driver)
        test_product_page.visible_product_title()
        text_products_title = test_product_page.get_text_products()
        test_product_page.assert_title_page(text_products_title, 'Products')


    @allure.title('Негативная проверка страницы авторизации')
    def test_negative_auth_page(self, driver):
        auth_page = MethodsAuth(driver)
        auth_page.open()
        auth_page.max_window()
        auth_page.send_user_name(LocatorsAuthPage.login)
        auth_page.send_password('qwer123')
        auth_page.click_login()
        auth_page.visible_error_password()
        text_password_error = auth_page.get_text_error_password()
        auth_page.assert_error_text(text_password_error,
                                    'Epic sadface: Username and password do not match any user in this service')
