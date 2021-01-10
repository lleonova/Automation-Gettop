from selenium.webdriver.common.by import By
from pages.base_page import Page
# from pages.top_menu_bar import TopMenu
# from pages.shopping_cart import ShoppingCart
from selenium.webdriver import ActionChains


class QuickView(Page):

    QUICK_VIEW_CONTAINER = (By.CSS_SELECTOR, "div.product-quick-view-container")
    QUICK_VIEW_BUTTONS = (By.CSS_SELECTOR, 'a.quick-view')
    IMAGE_SLIDER = (By.CSS_SELECTOR, 'div.product-gallery-slider button.next')
    DOTS = (By.CSS_SELECTOR, 'div.product-gallery-slider li')
    X_BUTTON = (By.CSS_SELECTOR, "button.mfp-close")
    QUICK_VIEW_ITEM_NAME = (By.CSS_SELECTOR, 'a.plain h1')
    QUICK_VIEW_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.single_add_to_cart_button")
    QUICK_VIEW_PRODUCT_NAME = (By.CSS_SELECTOR, 'td.product-name')
    QUICK_VIEW_PRODUCT_IMAGE = (By.CSS_SELECTOR, 'div.slide.is-selected img')

    # User can open Quick View by clicking Quick View pop up and close by clicking X
    def open_and_closing_window(self):
        self.actions = ActionChains(self.driver)

        self.wait_for_presence_off_all_elements(self.QUICK_VIEW_BUTTONS)
        qv_buttons = self.find_elements(*self.QUICK_VIEW_BUTTONS)

        for product in range(len(qv_buttons)):

            self.actions = ActionChains(self.driver)
            # find again after reloading page
            button = self.find_elements(*self.QUICK_VIEW_BUTTONS)[product]
            # click QV button to open QV window
            self.actions.move_to_element(button).click().perform()

            # click X button to close QV window
            self.click(*self.X_BUTTON)
            self.wait_for_element_disappear(self.QUICK_VIEW_CONTAINER)

    # User can click Quick View, add product to cart, verify adding
    # exact item on cart counter and Cart Page
    def add_product_to_cart(self):

        self.wait_for_presence_off_all_elements(self.QUICK_VIEW_BUTTONS)
        qv_buttons = self.find_elements(*self.QUICK_VIEW_BUTTONS)

        for product in range(len(qv_buttons)):
            self.actions = ActionChains(self.driver)
            # find again after reloading page
            button = self.find_elements(*self.QUICK_VIEW_BUTTONS)[product]
            # click Quick View button to open Quick View window
            self.actions.move_to_element(button)
            self.actions.click().perform()
            self.wait_for_element(self.QUICK_VIEW_ITEM_NAME)

            # remember item name
            product_name = self.find_element(*self.QUICK_VIEW_ITEM_NAME).get_attribute('textContent')

            # click add to cart button
            self.wait_for_element(self.QUICK_VIEW_ADD_TO_CART_BUTTON)
            self.click(*self.QUICK_VIEW_ADD_TO_CART_BUTTON)

            # verify shopping cart counter changes to 1
            banner = TopMenu(self.driver)
            banner.verify_cart_counter('1')

            # click shopping cart button and go to cart page
            banner.click_cart_button()

            # verify quantity of items in the cart
            shopping_cart = ShoppingCart(self.driver)
            shopping_cart.verify_quantity_in_the_cart('1')

            # verify user added product with correct name
            shopping_cart.verify_added_product_name(product_name)

            # empty shopping cart
            shopping_cart.remove_item_from_card()

            # return to home page
            self.open_page()

    # User can open Quick View and click through product images
    def click_through_images(self):

        self.wait_for_presence_off_all_elements(self.QUICK_VIEW_BUTTONS)
        qv_buttons = self.find_elements(*self.QUICK_VIEW_BUTTONS)

        for product in range(len(qv_buttons)):
            # find again after reloading page
            self.actions = ActionChains(self.driver)
            # click Quick View pop up button
            button = self.find_elements(*self.QUICK_VIEW_BUTTONS)[product]
            self.actions.move_to_element(button).click().perform()

            # click through product images
            self.wait_for_presence_off_all_elements(self.DOTS)
            dots = self.find_elements(*self.DOTS)

            for _ in range(len(dots)):
                self.actions = ActionChains(self.driver)

                self.wait_for_presence_off_all_elements(self.DOTS)
                self.actions.click(dots[_]).perform()
                # verify image exists
                self.verify_image_present(*self.QUICK_VIEW_PRODUCT_IMAGE)

            # return to home page
            self.open_page()

from pages.top_menu_bar import TopMenu
from pages.shopping_cart import ShoppingCart
