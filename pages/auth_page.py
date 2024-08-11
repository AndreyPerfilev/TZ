import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

"""Класс с локаторами и данными для авторизации """


class LocatorsAuthPage():
    url = "https://www.saucedemo.com/"
    locator_user_name = [By.CSS_SELECTOR, "[placeholder='Username']"]
    locator_password = [By.ID, "password"]
    locator_login_button = [By.XPATH, "//input[@type='submit']"]
    locator_error_password = [By.XPATH, "//h3[@data-test='error']"]
    login = "standard_user"
    password = "secret_sauce"


"""Класс с методами для страницы авторизации"""


class MethodsAuth(BasePage):

    @allure.step('Открыть страницу авторизации')
    def open(self):
        self.driver.get(LocatorsAuthPage.url)

    @allure.step('Ввести {login} в поле ввода логина')
    def send_user_name(self, login):
        self.send_keys(LocatorsAuthPage.locator_user_name, login)

    @allure.step('Ввести {password} в поле ввода пароля')
    def send_password(self, password):
        self.send_keys(LocatorsAuthPage.locator_password, password)

    @allure.step('Нажать кнопку login')
    def click_login(self):
        self.click_on_element(LocatorsAuthPage.locator_login_button)

    @allure.step('Ожидание появления в поле ввода пароля ошибки')
    def visible_error_password(self):
        self.wait_element(LocatorsAuthPage.locator_error_password)

    def get_text_error_password(self):
        return self.get_text_from_element(LocatorsAuthPage.locator_error_password)


