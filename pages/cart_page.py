from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_cart_is_emtpy(self):
        """Проверить, что корзина пустая"""
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), \
            "Cart is not empty."

    def should_message_cart_is_empty_displayed(self):
        """Проверить, что сообщение 'Ваша корзина пуста' - отображается"""
        assert self.is_element_present(*CartPageLocators.MESSAGE_CART_IS_EMPTY), \
            "Message 'Cart is empty' not displayed."
