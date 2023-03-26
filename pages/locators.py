from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    MESSAGE_COST_THE_CART = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")


class CartPageLocators():
    CART_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
