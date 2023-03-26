from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        self.add_product_to_basket()
        self.get_quiz_result()
        self.message_that_a_product_has_been_added_to_cart()
        self.product_price_should_match_the_cart_cost_in_message()

    def add_product_to_basket(self):
        """Нажимаем на кнопку 'Добавить в корзину'"""
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_quiz_result(self):
        """Посчитать результат математического выражения и ввести ответ на печать"""
        self.solve_quiz_and_get_code()

    def message_that_a_product_has_been_added_to_cart(self):
        """Проверить, что в сообщении о том, что товар добавлен в корзину
        - название товара совпадает с тем товаром, который был добавлен"""
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_added = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_CART).text
        assert product_name == message_product_added,\
            "The product name in the message does not match the product that was added to the cart."

    def product_price_should_match_the_cart_cost_in_message(self):
        """Проверить, что стоимость корзины совпадает с ценой товара"""
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cost_cart_massage = self.browser.find_element(*ProductPageLocators.MESSAGE_COST_THE_CART).text
        assert product_price == cost_cart_massage, "The price of the item does not match the cart price in the message."
