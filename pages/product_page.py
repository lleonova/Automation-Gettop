from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
# from pages.top_menu_bar import TopMenu
# from pages.wishlist_page import WishList


class Product(Page):

    ALL_PRODUCT_LINKS = (By.XPATH, "//ul[contains(@class, 'nav-dropdown-default')]//a")
    PRODUCT_DESCRIPTION_LINK = (By.XPATH, "//li[@id='tab-title-description']//a")
    PRODUCT_DESCRIPTION_TAB = (By.XPATH, "//li[@id='tab-title-description']")
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h1.product-title')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price span.amount')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.single_add_to_cart_button')

    HOME_BUTTON = (By.CSS_SELECTOR, "div.product-info  a[href='https://gettop.us']")

    HEART_BUTTON = (By.CSS_SELECTOR, "button.wishlist-button")

    # collect links for all products on the site
    def open_product_pages(self):
        self.wait_for_presence_off_all_elements(self.ALL_PRODUCT_LINKS)
        product_links = self.grab_href_links_from_a_tags(*self.ALL_PRODUCT_LINKS)
        return product_links


    # Verify clicking Logo Icon takes user to Home Page from every Product page
    def verify_return_to_home_page_from_every_product_pages(self):
        self.wait_for_presence_off_all_elements(self.ALL_PRODUCT_LINKS)
        product_links = self.grab_href_links_from_a_tags(*self.ALL_PRODUCT_LINKS)
        top_menu = TopMenu(self.driver)
        for product in product_links:
            self.open_page(product)
            top_menu.click_logo_icon()
            top_menu.verify_home_page()


    # verify every product has description tab
    def verify_description(self):
        self.wait_for_presence_off_all_elements(self.ALL_PRODUCT_LINKS)
        product_links = self.grab_href_links_from_a_tags(*self.ALL_PRODUCT_LINKS)
        for product in product_links:
            self.open_page(product)
            self.find_element(*self.PRODUCT_DESCRIPTION_TAB)


    # verify every product has name
    def verify_product_name(self, name: str):
        product_name = self.find_element(*self.PRODUCT_NAME).get_attribute('textContent')
        assert name in product_name, f'Expected to see {name}, but got {product_name}'


    # verify fields sale price and original price not empty
    def verify_price_and_sale_price(self):
        product_name = self.find_element(*self.PRODUCT_NAME).get_attribute('textContent')
        product_price = self.find_elements(*self.PRODUCT_PRICE)
        for _ in range(len(product_price)):
            assert product_price[_].text != '', \
                f'Product price on {product_name} product page is missing'


    # click add to cart button
    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)


    # Verify Home link takes user to Home Page from every Product page
    def verify_home_link_from_every_product_page(self):
        self.wait_for_presence_off_all_elements(self.ALL_PRODUCT_LINKS)
        product_links = self.grab_href_links_from_a_tags(*self.ALL_PRODUCT_LINKS)
        top_menu = TopMenu(self.driver)
        for product in product_links:
            self.open_product_page(product)
            self.click(*self.HOME_BUTTON)
            top_menu.verify_home_page()


    # User can add correct item to Wishlist, remove item and see a confirmation Pop-up
    def add_correct_item_to_wishlist(self):
        self.wait_for_presence_off_all_elements(self.ALL_PRODUCT_LINKS)
        product_links = self.grab_href_links_from_a_tags(*self.ALL_PRODUCT_LINKS)
        for _ in product_links:
            self.open_product_page(_)

            # remember product name
            product_name = self.find_element(*self.PRODUCT_NAME).get_attribute('textContent')

            # click Heart Icon to add item to Wishlist Page
            self.actions = ActionChains(self.driver)
            self.actions.move_to_element(self.find_element(*self.HEART_BUTTON)).click().perform()

            # click Heart Icon again to go to Wishlist Page
            current_url = self.driver.current_url
            self.wait_for_element_clickable(self.HEART_BUTTON)
            self.click(*self.HEART_BUTTON)

            # verify product was added to Wishlist with the same name
            self.wait_for_url_change(current_url)
            wishlist_page = WishList(self.driver)
            wishlist_page.verify_wishlist_product_name(product_name)

            # Remove product from Wishlist and verify Empty Wishlist message
            wishlist_page.remove_item_from_wishlist()

            # # return to home page
            self.open_page()


    # User can add correct item to Wishlist, see social logos, remove item and see a confirmation Pop-up
    def verify_wishlist_has_social_logos(self):
        self.wait_for_presence_off_all_elements(self.ALL_PRODUCT_LINKS)
        product_links = self.grab_href_links_from_a_tags(*self.ALL_PRODUCT_LINKS)
        for _ in product_links:
            self.open_product_page(_)

            # remember product name
            product_name = self.find_element(*self.PRODUCT_NAME).get_attribute('textContent')

            # click Heart Icon to add item to Wishlist Page
            self.actions = ActionChains(self.driver)
            self.actions.move_to_element(self.find_element(*self.HEART_BUTTON)).click().perform()

            # click Heart Icon again to go to Wishlist Page
            current_url = self.driver.current_url
            self.wait_for_element_clickable(self.HEART_BUTTON)
            self.click(*self.HEART_BUTTON)

            # verify product was added to Wishlist with the same name
            self.wait_for_url_change(current_url)
            wishlist_page = WishList(self.driver)
            wishlist_page.verify_wishlist_product_name(product_name)

            # verify User can see social logos
            wishlist_page.verify_social_logos()

            # Remove product from Wishlist and verify Empty Wishlist message
            wishlist_page.remove_item_from_wishlist()

            # # return to home page
            self.open_page()


    # User add correct item to Wishlist, verify User can click on wishlist item and is taken to correct product page
    def verify_wishlist_correct_link(self):
        self.wait_for_presence_off_all_elements(self.ALL_PRODUCT_LINKS)
        product_links = self.grab_href_links_from_a_tags(*self.ALL_PRODUCT_LINKS)
        for _ in product_links:
            self.open_product_page(_)

            # remember product name
            product_name = self.find_element(*self.PRODUCT_NAME).get_attribute('textContent')

            # click Heart Icon to add item to Wishlist Page
            self.actions = ActionChains(self.driver)
            current_url = self.driver.current_url
            self.actions.move_to_element(self.find_element(*self.HEART_BUTTON)).click().perform()

            # click Heart Icon again to go to Wishlist Page
            self.wait_for_element_clickable(self.HEART_BUTTON)
            self.click(*self.HEART_BUTTON)
            self.wait_for_url_change(current_url)

            # verify product was added to Wishlist with the same name
            wishlist_page = WishList(self.driver)
            wishlist_page.verify_wishlist_product_name(product_name)
            current_url = self.driver.current_url

            # click on wishlist item link
            wishlist_page.click_item_link()
            self.wait_for_url_change(current_url)

            # verify link takes user to correct item page
            new_product_name = self.find_element(*self.PRODUCT_NAME).get_attribute('textContent')
            assert product_name == new_product_name, \
                f'Expected to see {product_name}, but got to the page with {new_product_name}'
            current_url = self.driver.current_url

            # click Heart Icon again to go to Wishlist Page
            self.actions = ActionChains(self.driver)
            self.actions.move_to_element(self.find_element(*self.HEART_BUTTON)).click().perform()
            self.wait_for_url_change(current_url)

            # Remove product from Wishlist and verify Empty Wishlist message
            wishlist_page.remove_item_from_wishlist()

            # # return to home page
            self.open_page()


    # User can click trough multiple product pages by clicking 1, 2 for page number
    def clicks_through_product_pages_with_1_2(self):
        pass


    # User can click trough multiple product pages by clicking > and <
    def clicks_through_product_pages_with_arrows(self):
        pass


from pages.top_menu_bar import TopMenu
from pages.wishlist_page import WishList
