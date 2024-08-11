import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LocatorsCheckoutInformationPage:
    locator_title_checkout = [By.XPATH, "//span[@class='title']"]
    locator_first_name = [By.ID, "first-name"]
    locator_last_name = [By.ID, "last-name"]
    locator_postal_code = [By.ID, "postal-code"]
    locator_continue_button = [By.ID, "continue"]
    first_name = 'Антон'
    last_name = 'Егоров'
    postal_code = '121609'


class MethodsCheckoutInformationPage(BasePage):
    @allure.step('Заполняем поле имя -{data}')
    def send_name(self, data):
        self.send_keys(LocatorsCheckoutInformationPage.locator_first_name, data)

    @allure.step('Заполняем поле фамилия -{data}')
    def send_last_name(self, data):
        self.send_keys(LocatorsCheckoutInformationPage.locator_last_name, data)

    @allure.step('Заполняем поле почтовый индекс -{data}')
    def send_postal(self, data):
        self.send_keys(LocatorsCheckoutInformationPage.locator_postal_code, data)

    @allure.step('Нажимаем кнопку "Continue"')
    def click_continue(self):
        self.click_on_element(LocatorsCheckoutInformationPage.locator_continue_button)

    def get_text_title_checkout_information(self):
        return self.get_text_from_element(LocatorsCheckoutInformationPage.locator_title_checkout)

    @allure.step('Ожидание появления заголовка страницы Заказ:Ваша информация')
    def visible_checkout_information_title(self):
        self.wait_element(LocatorsCheckoutInformationPage.locator_title_checkout)
