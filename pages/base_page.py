import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""Класс с общими методами для всех страниц"""


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def max_window(self):
        return self.driver.maximize_window()

    def find_element_page(self, locator):
        return self.driver.find_element(*locator)

    def find_elements_page(self, locator):
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    def wait_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def get_text_from_element(self, locator):
        return self.find_element_page(locator).text

    @allure.step('Проверка соответствия названия товара {actual} == {expected}')
    def assert_product_name(self, actual, expected):
        assert actual == expected, "Название товара  не соответствует ожидаемому"

    @allure.step('Проверка соответствия количества товара {actual} == {expected}')
    def assert_product_count(self, actual, expected):
        assert actual == expected, "Количество товара не соответствует ожидаемому"

    @allure.step('Проверка заголовка страницы {actual} == {expected}')
    def assert_title_page(self, actual, expected):
        assert actual == expected, "Название заголовка не соответствует ожидаемому"

    @allure.step('Проверка текста ошибки  {actual} == {expected}')
    def assert_error_text(self, actual, expected):
        assert actual == expected, "Текст ошибки  не соответствует ожидаемому"
