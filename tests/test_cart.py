import allure

from pages.auth_page import LocatorsAuthPage, MethodsAuth
from pages.products import MethodsProducts, LocatorsProductsPage
from pages.your_cart import MethodsYourCart


class TestCartPage:

    @allure.title('Позитивная проверка добавления одного товара в корзину')
    def test_add_item_to_cart(self, driver):
        test_auth_page = MethodsAuth(driver)
        test_auth_page.open()
        test_auth_page.max_window()
        test_auth_page.send_user_name(LocatorsAuthPage.login)
        test_auth_page.send_password(LocatorsAuthPage.password)
        test_auth_page.click_login()
        test_product_page = MethodsProducts(driver)
        test_product_page.visible_product_title()
        text_products_title = test_product_page.get_text_products()
        assert text_products_title == 'Products', "Текст title 'Products' не соответсвует"
        first_item_in_cart = LocatorsProductsPage.choice_item_add_cart[0]
        test_product_page.click_add_item_to_cart_by_text(first_item_in_cart)
        test_product_page.click_cart_button()
        test_your_cart = MethodsYourCart(driver)
        test_your_cart.visible_your_cart_title()
        text_cart_title = test_your_cart.get_text_your_cart()
        assert text_cart_title == "Your Cart", "Текст title  your cart не соответсвует"
        product_cart = test_your_cart.get_product_by_index(0)
        assert product_cart.text == first_item_in_cart, "Название товара в корзине не соответствует ожидаемому"

    @allure.title('Позитивная проверка добавления двух товаров в корзину и удаление одного')
    def test_add_two_items_and_delete_one_item(self, driver):
        auth_page = MethodsAuth(driver)
        auth_page.open()
        auth_page.max_window()
        auth_page.send_user_name(LocatorsAuthPage.login)
        auth_page.send_password(LocatorsAuthPage.password)
        auth_page.click_login()
        product_page = MethodsProducts(driver)
        product_page.visible_product_title()
        text_products_title = product_page.get_text_products()
        product_page.assert_title_page(text_products_title, 'Products')

        first_item_products_page = LocatorsProductsPage.choice_item_add_cart[1]
        second_item_products_page = LocatorsProductsPage.choice_item_add_cart[5]
        product_page.click_add_item_to_cart_by_text(first_item_products_page)
        product_page.click_add_item_to_cart_by_text(second_item_products_page)
        product_page.click_cart_button()
        your_cart = MethodsYourCart(driver)
        your_cart.visible_your_cart_title()
        your_cart.assert_title_page(your_cart.get_text_your_cart(), "Your Cart")

        all_products = your_cart.get_all_products()
        your_cart.assert_product_count(len(all_products), 2)
        first_item_in_your_cart = your_cart.get_product_by_index(0)
        second_item_in_your_cart = your_cart.get_product_by_index(1)
        your_cart.assert_product_name(first_item_in_your_cart.text, first_item_products_page)
        your_cart.assert_product_name(second_item_in_your_cart.text, second_item_products_page)
        locator_remove_item_cart = your_cart.gen_locator_remove_id(first_item_products_page)
        your_cart.click_on_element(locator_remove_item_cart)
        without_one_product = your_cart.get_all_products()
        your_cart.assert_product_count(len(without_one_product), 1)
