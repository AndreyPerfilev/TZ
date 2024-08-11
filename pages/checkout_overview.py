import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LocatorsCheckoutOverviewPage:
    locator_title_checkout_overview = [By.XPATH, "//span[@class='title']"]
    locator_first_name = [By.ID, "first-namee"]
    locator_last_name = [By.ID, "last-name"]
    locator_finish = [By.ID, "finish"]


class MethodsCheckoutOverviewPage(BasePage):

    def get_text_title_checkout_overview(self):
        return self.get_text_from_element(LocatorsCheckoutOverviewPage.locator_title_checkout_overview)

    @allure.step('Ожидание появления заголовка Заказ:Обзор заказа')
    def visible_checkout_overview_title(self):
        self.wait_element(LocatorsCheckoutOverviewPage.locator_title_checkout_overview)

    @allure.step('Нажать кнопку "Finish"')
    def click_finish_button(self):
        self.click_on_element(LocatorsCheckoutOverviewPage.locator_finish)

    def get_text_from_item_order(self, text):
        find_item = [By.XPATH, "//div[@class='inventory_item_name' and contains(., '" + text + "')]"]
        return self.get_text_from_element(find_item)
