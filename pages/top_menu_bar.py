from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
# from pages.categories_page import Category
# from pages.quick_view import QuickView


class TopMenu(Page):

    ACCOUNT_ICON = (By.CSS_SELECTOR, 'i.icon-user')

    GETTOP_LOGO = (By.CSS_SELECTOR, '#logo a')

    CART_ICON = (By.CSS_SELECTOR, 'li.has-dropdown span.cart-icon strong')
    REMOVE_FROM_CART_BUTTON = (By.CSS_SELECTOR, 'a.remove.remove_from_cart_button')
    CART_BUTTON = (By.CSS_SELECTOR, "li.has-dropdown a.header-cart-link")

    CATEGORIES = (By.CSS_SELECTOR, 'li.menu-item.has-dropdown')
    CATEGORY_LINKS = (By.CSS_SELECTOR, "li[id^='menu-item']  a[href*=product-category]")

    # click on account icon
    def click_account_icon(self):
        self.wait_for_element_click(self.ACCOUNT_ICON)

    # click on logo link
    def click_logo_icon(self):
        self.wait_for_element_click(self.GETTOP_LOGO)

    # verify Home Page is opened
    def verify_home_page(self):
        self.verify_link(self.base_url)

    # click cart button
    def click_cart_button(self):
        self.wait_for_element_click(self.CART_BUTTON)

    # verify Items in cart Counter changes to {number}
    def verify_cart_counter(self, number: str):
        cart_icon = self.find_element(*self.CART_ICON)
        self.wait_for_element_stale(cart_icon)

        self.wait_for_element_clickable(self.CART_ICON)
        self.verify_text(number, *self.CART_ICON)

    # empty the shopping cart
    def click_x_on_cart_pop_up(self):
        cart_icon = self.find_element(*self.CART_ICON)
        self.wait_for_element_stale(cart_icon)

        self.wait_for_element_clickable(self.CART_ICON)
        cart_icon = self.find_element(*self.CART_ICON)

        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(cart_icon).perform()

        self.wait_for_element(self.REMOVE_FROM_CART_BUTTON)
        self.click(*self.REMOVE_FROM_CART_BUTTON)

    # Verify Home link takes user to Home Page from every Category
    def verify_home_link_from_every_category_page(self):
        self.wait_for_presence_off_all_elements(self.CATEGORY_LINKS)
        category_links = self.grab_href_links_from_a_tags(*self.CATEGORY_LINKS)
        category = Category(self.driver)
        for _ in category_links:
            self.open_product_page(_)
            category.click_home_link()
            self.verify_home_page()

    # Verify clicking Logo Icon takes user to Home Page from every Category page
    def verify_logo_icon_from_every_category_page(self):
        self.wait_for_presence_off_all_elements(self.CATEGORY_LINKS)
        category_links = self.grab_href_links_from_a_tags(*self.CATEGORY_LINKS)
        for _ in category_links:
            self.open_product_page(_)
            self.click_logo_icon()
            self.verify_home_page()


    def open_quick_view(self):
        self.wait_for_presence_off_all_elements(self.CATEGORY_LINKS)
        category_links = self.grab_href_links_from_a_tags(*self.CATEGORY_LINKS)
        # category = Category(self.driver)
        quick_view = QuickView(self.driver)
        for _ in category_links:
            self.open_product_page(_)
            sleep(2)
            # category.click_quick_view_buttons()

            quick_view.open_and_closing_window()

            # self.wait_for_presence_off_all_elements()
            # all_products_in_category = self.find_elements()
            # for product in all_products_in_category:
            # return to home page
            self.open_page()

from pages.categories_page import Category
from pages.quick_view import QuickView