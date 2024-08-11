import allure

from pages.auth_page import MethodsAuth, LocatorsAuthPage
from pages.checkout_complete import MethodsCheckoutCompletePage
from pages.checkout_information import MethodsCheckoutInformationPage, LocatorsCheckoutInformationPage
from pages.checkout_overview import MethodsCheckoutOverviewPage
from pages.products import MethodsProducts, LocatorsProductsPage
from pages.your_cart import MethodsYourCart


class TestOrder:
    @allure.title('Позитивная проверка полного оформления заказа')
    def test_order_positive(self, driver):
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

        first_item_product_page = LocatorsProductsPage.choice_item_add_cart[2]
        product_page.click_add_item_to_cart_by_text(first_item_product_page)
        product_page.click_cart_button()
        your_cart_page = MethodsYourCart(driver)
        your_cart_page.visible_your_cart_title()
        your_cart_page.assert_title_page(your_cart_page.get_text_your_cart(), 'Your Cart')

        first_item_in_your_cart = your_cart_page.get_product_by_index(0).text
        your_cart_page.assert_product_name(first_item_in_your_cart, first_item_product_page)
        your_cart_page.click_checkout()
        checkout_information_page = MethodsCheckoutInformationPage(driver)
        checkout_information_page.visible_checkout_information_title()
        text_checkout_information_title = checkout_information_page.get_text_title_checkout_information()
        checkout_information_page.assert_title_page(text_checkout_information_title, "Checkout: Your Information")
        checkout_information_page.send_name(LocatorsCheckoutInformationPage.first_name)
        checkout_information_page.send_last_name(LocatorsCheckoutInformationPage.last_name)
        checkout_information_page.send_postal(LocatorsCheckoutInformationPage.postal_code)
        checkout_information_page.click_continue()

        checkout_overview_page = MethodsCheckoutOverviewPage(driver)
        checkout_overview_page.visible_checkout_overview_title()
        text_checkout_overview_title = checkout_overview_page.get_text_title_checkout_overview()
        checkout_overview_page.assert_title_page(text_checkout_overview_title, "Checkout: Overview")
        text_item = checkout_overview_page.get_text_from_item_order(first_item_product_page)
        checkout_overview_page.assert_product_name(text_item, first_item_in_your_cart)
        checkout_overview_page.click_finish_button()

        checkout_complete_page = MethodsCheckoutCompletePage(driver)
        checkout_complete_page.visible_checkout_complete_title()
        text_checkout_complete_title = checkout_complete_page.get_text_title_checkout_complete()
        checkout_complete_page.assert_title_page(text_checkout_complete_title, "Checkout: Complete!")

        checkout_complete_page.visible_complete_order()
        text_checkout_complete_order = checkout_complete_page.get_text_complete_order()
        checkout_complete_page.assert_title_page(text_checkout_complete_order, "Thank you for your order!")
        checkout_complete_page.click_back_home_button()
        product_page.visible_product_title()
        text_products_title = product_page.get_text_products()
        product_page.assert_title_page(text_products_title, 'Products')

