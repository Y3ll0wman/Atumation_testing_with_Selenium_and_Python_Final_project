from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_is_emtpy(self):
        """Проверить, что корзина пустая"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty."

    def should_message_basket_is_empty_displayed(self):
        """Проверить, что сообщение 'Ваша корзина пуста' - отображается"""
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), \
            "Message 'Basket is empty' not displayed."
