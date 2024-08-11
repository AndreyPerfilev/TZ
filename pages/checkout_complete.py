import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LocatorsCheckoutCompletePage:
    locator_title_checkout_complete = [By.XPATH, "//span[@class='title']"]
    locator_back_home_button = [By.ID, "back-to-products"]
    locator_complete_order = [By.XPATH, "//h2[@class='complete-header']"]


class MethodsCheckoutCompletePage(BasePage):

    def get_text_title_checkout_complete(self):
        return self.get_text_from_element(LocatorsCheckoutCompletePage.locator_title_checkout_complete)

    @allure.step('Ожидание заголовка страницы Заказ:Успешно оформлен')
    def visible_checkout_complete_title(self):
        self.wait_element(LocatorsCheckoutCompletePage.locator_title_checkout_complete)

    @allure.step('Нажать на кнопку назад')
    def click_back_home_button(self):
        self.click_on_element(LocatorsCheckoutCompletePage.locator_back_home_button)

    def get_text_complete_order(self):
        return self.get_text_from_element(LocatorsCheckoutCompletePage.locator_complete_order)

    @allure.step('Ожидание статуса "Успешный заказ"')
    def visible_complete_order(self):
        self.wait_element(LocatorsCheckoutCompletePage.locator_complete_order)
