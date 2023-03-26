from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_FORM_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    MESSAGE_COST_THE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
