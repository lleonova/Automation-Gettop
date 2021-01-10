from selenium.webdriver.common.by import By
from pages.base_page import Page


class ShoppingCart(Page):

    EMPTY_CART_MESSAGE = (By.XPATH, "//p[@class='cart-empty woocommerce-info']")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, "div.quantity input[type='number']")
    PRODUCT_NAME = (By.CSS_SELECTOR, 'td.product-name a')
    MINUS_BUTTON = (By.CSS_SELECTOR, "input.minus")
    UPDATE_CART_BUTTON = (By.CSS_SELECTOR, "button[name='update_cart']")

    def verify_quantity_in_the_cart(self, number: str):
        self.wait_for_element(self.PRODUCT_QUANTITY)
        quantity = self.find_element(*self.PRODUCT_QUANTITY).get_attribute('value')
        assert quantity == number, f'Expected to have {number} item in the cart, but got {quantity}'

    def remove_item_from_card(self):
        self.wait_for_element_click(self.MINUS_BUTTON)
        self.wait_for_element_click(self.UPDATE_CART_BUTTON)
        self.verify_quantity_in_the_cart('0')

    def verify_added_product_name(self, name: str):
        added_product_name = self.find_element(*self.PRODUCT_NAME).get_attribute('textContent')
        assert name in added_product_name, f'Expected to see {name}, but got {added_product_name}'
