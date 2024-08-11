import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LocatorsYourCartPage:
    locator_your_cart = [By.XPATH, "//span[@class='title']"]
    locator_checkout = [By.ID, "checkout"]
    locator_remove_bike_light = [By.ID, 'remove-sauce-labs-backpack']


class MethodsYourCart(BasePage):
    @allure.step('Ожидание появления заголовка Ваша корзина')
    def visible_your_cart_title(self):
        self.wait_element(LocatorsYourCartPage.locator_your_cart)

    def get_text_your_cart(self):
        return self.get_text_from_element(LocatorsYourCartPage.locator_your_cart)

    @allure.step('Поиск товара в корзине по названию - {text}')
    def get_product_by_text(self, text):
        cart_product = [By.XPATH, "//div[@data-test='inventory-item-name' and contains(text(),'" + text + "')]"]
        return self.find_element_page(cart_product)

    @allure.step('Поиск товара в корзине по индексу - {index}')
    def get_product_by_index(self, index):
        cart_products = [By.XPATH, "//div[@data-test='inventory-item-name']"]
        return self.find_elements_page(cart_products)[index] if cart_products else None

    @allure.step('Поиск всех товарор в корзине')
    def get_all_products(self):
        cart_products = [By.XPATH, "//div[@data-test='inventory-item-name']"]
        return self.find_elements_page(cart_products) if cart_products else None



    def gen_locator_remove_id(self, text):
        remove_str = f'remove {text}'
        remove_str_with_dash = remove_str.replace(' ', '-').lower()
        locator_remove_id = [By.ID, f"{remove_str_with_dash}"]
        return locator_remove_id

    @allure.step('Нажать на кнопку "Checkout"')
    def click_checkout(self, ):
        self.click_on_element(LocatorsYourCartPage.locator_checkout)
