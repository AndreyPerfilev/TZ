import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

"""Класс с локаторами страницы товары"""


class LocatorsProductsPage:
    locator_products_title = [By.XPATH, "//span[@class='title']"]
    locator_add_cart_sauce_labs_bike_light = [By.ID, "add-to-cart-sauce-labs-bike-light"]
    locator_add_cart_sauce_labs_backpack = [By.ID, "add-to-cart-sauce-labs-backpack"]
    locator_cart_button = [By.XPATH, "//a[@class='shopping_cart_link']"]
    choice_item_add_cart = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                            "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]


"""Класс с методами для страницы товары"""


class MethodsProducts(BasePage):
    @allure.step('Ожидание появления заголовка страницы товары')
    def visible_product_title(self):
        self.wait_element(LocatorsProductsPage.locator_products_title)

    def get_text_products(self):
        return self.get_text_from_element(LocatorsProductsPage.locator_products_title)

    @allure.step('Добававить товар в корзину по названию -{text}')
    def click_add_item_to_cart_by_text(self, text):
        add_to_cart_product = [By.XPATH,
                               "//div[@class='inventory_item_description' and contains(., '" + text + "')]//button[contains(text(), 'Add to cart')]"]
        self.click_on_element(add_to_cart_product)

    @allure.step('Нажать на кнопку корзины')
    def click_cart_button(self):
        self.click_on_element(LocatorsProductsPage.locator_cart_button)
