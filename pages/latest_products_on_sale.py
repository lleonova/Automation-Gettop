from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from pages.product_page import Product
from pages.shopping_cart import ShoppingCart
from pages.top_menu_bar import TopMenu
from pages.wishlist_page import WishList

from app.logger import logger


class LatestSale(Page):

    LATEST_ON_SALE_TEXT = (By.XPATH, "//span[@class='section-title-main']")
    PRODUCTS_UNDER_LATEST_ON_SALE = (By.CSS_SELECTOR, 'div.sale')

    ON_SALE_BADGE = (By.CSS_SELECTOR, 'span.onsale')
    LATEST_ON_SALE_PRODUCT_NAME = (By.CSS_SELECTOR, 'p.name')
    LATEST_ON_SALE_PRODUCT_CATEGORY = (By.CSS_SELECTOR, 'p.category')
    LATEST_ON_SALE_PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.price ins span.amount')
    LATEST_ON_SALE_STAR_RATING = (By.CSS_SELECTOR, 'div.sale div.star-rating')
    LATEST_ON_SALE_PRODUCT_IMAGE = (By.CSS_SELECTOR, 'img.size-woocommerce_thumbnail')

    HEART_BUTTON = (By.CSS_SELECTOR, 'button.wishlist-button')
    ADD_TO_WISHLIST_POPUP = (By.CSS_SELECTOR, 'a.add_to_wishlist span')
    ITEM_ADDED_POPUP = (By.CSS_SELECTOR, 'div#yith-wcwl-message')
    BROWSE_WISHLIST_POP_UP = (By.CSS_SELECTOR, "a[data-title='Browse wishlist']")

    SALE_ITEM_PICTURES = (By.CSS_SELECTOR, 'div.image-fade_in_back a')


    # verify text for products on sale is shown
    def verify_sale_text(self, text):
        self.verify_text(text, *self.LATEST_ON_SALE_TEXT)


    # verify every product on sale has Sale icon, image, product category, name, price, and star-rating
    def verify_sale_products_attributes(self):

        # find all the products from sale slider
        self.wait_for_presence_off_all_elements(self.PRODUCTS_UNDER_LATEST_ON_SALE)
        products = self.find_elements(*self.PRODUCTS_UNDER_LATEST_ON_SALE)

        for item in products:
            # verify every product on sale has a Sale icon
            assert "Sale!" in item.find_element(*self.ON_SALE_BADGE).text, \
                f"Expected 'Sale!' in product price, but get {item.text}"

            # verify every product on the page has a product name
            name = item.find_element(*self.LATEST_ON_SALE_PRODUCT_NAME).text
            assert name != '', f"Expected every product on the sale slider has a product name, but could not find it"

            # verify every product on the page has a product category
            assert item.find_element(*self.LATEST_ON_SALE_PRODUCT_CATEGORY).text != '', \
                f"Expected every product on the sale slider has a product category, but {name} does not have it"

            # verify every product on the page has a price
            assert item.find_element(*self.LATEST_ON_SALE_PRODUCT_PRICE).text != '', \
                f"Expected every product on the sale slider has a price, but {name} does not have it"

            try:
                # verify every product on the page has star-rating
                assert item.find_element(*self.LATEST_ON_SALE_STAR_RATING).text != ''

            except NoSuchElementException:  # Some products don't have star-ratings
                print(f'Product "{name}" does not have star-rating')
                logger.warning(f'Product "{name}" does not have star-rating')

            # verify every product on the page has image
            self.verify_image_present(*self.LATEST_ON_SALE_PRODUCT_IMAGE), \
                f"Expected every product on the sale slider has a image, but could not find it"


    # verify when you hoover over heart icon, pop-up message is: text (Add to wishlist)
    def verify_add_to_wishlist_pop_up(self, text: str):
        # find all hearts/add to wishlist buttons
        self.wait_for_presence_off_all_elements(self.HEART_BUTTON)
        hearts = self.find_elements(*self.HEART_BUTTON)

        for _ in range(len(hearts)):
            # hoover over heart
            self.actions.move_to_element((self.find_elements(*self.HEART_BUTTON))[_]).perform()
            # make sure Add To Wishlist popup is visible
            add_to_wishlist_blocks = self.find_elements(*self.ADD_TO_WISHLIST_POPUP)
            self.wait_for_element_visible(add_to_wishlist_blocks[_])
            pop_up_add_to_wishlist = self.find_elements(*self.ADD_TO_WISHLIST_POPUP)[_]
            assert text in pop_up_add_to_wishlist.text, \
                f"Expected text: Add to wishlist, but got {pop_up_add_to_wishlist.text}"


    # User click on heart icon to add to wishlist, verify Pop-up message Product added!
    # and correct item is added to Wishlist
    def verify_adding_to_wishlist(self, text: str):
        # find all the hearts/add to wishlist buttons
        self.wait_for_presence_off_all_elements(self.HEART_BUTTON)
        hearts = self.find_elements(*self.HEART_BUTTON)

        for _ in range(len(hearts)):
            # remember item name
            product_name = (self.find_elements(*self.LATEST_ON_SALE_PRODUCT_NAME))[_].get_attribute('textContent')

            self.actions = ActionChains(self.driver)
            # hoover and click over heart
            self.actions.move_to_element((self.find_elements(*self.HEART_BUTTON))[_]).click().perform()

            # verify Product Added! popup is visible
            self.wait_for_element_visible(self.find_element(*self.ITEM_ADDED_POPUP))
            added_pop_up = self.find_element(*self.ITEM_ADDED_POPUP).get_attribute('textContent')
            assert text in added_pop_up, f'Expected to see Item added!, but got {added_pop_up}'

            # click Heart Icon to go to Wishlist Page
            self.actions = ActionChains(self.driver)
            self.actions.move_to_element((self.find_elements(*self.HEART_BUTTON))[_]).click().perform()

            # verify product was added to Wishlist with the same name
            wishlist_page = WishList(self.driver)
            wishlist_page.verify_wishlist_product_name(product_name)
            # Remove product from Wishlist
            wishlist_page.remove_item_from_wishlist()
            #  verify Empty Wishlist message
            wishlist_page.verify_empty_wishlist_message()
            #  verify Empty Wishlist message
            wishlist_page.verify_empty_wishlist_message()

            # return to home page
            self.open_page()


    # User can open product from Sale and see product price and description
    def sale_product_click(self):
        # find all the products from sale slider
        self.wait_for_presence_off_all_elements(self.PRODUCTS_UNDER_LATEST_ON_SALE)
        products = self.find_elements(*self.PRODUCTS_UNDER_LATEST_ON_SALE)

        for item in range(len(products)):
            # find again after reloading page
            product = self.find_elements(*self.PRODUCTS_UNDER_LATEST_ON_SALE)[item]

            # remember item name
            item_name = product.find_element(*self.LATEST_ON_SALE_PRODUCT_NAME).get_attribute('textContent')

            # click on product picture
            self.wait_for_presence_off_all_elements(self.SALE_ITEM_PICTURES)
            product_picture = self.find_elements(*self.SALE_ITEM_PICTURES)
            product_picture[item].click()

            # verify click opens product page with the same name
            product_page = Product(self.driver)
            product_page.verify_product_name(item_name)

            # verify fields sale price and original price not empty
            product_page.verify_price_and_sale_price()

            # return to home page
            self.open_page()


    # User can open every product from Sale, add it to cart,
    # verify items in cart counter become equal 1 and remove product from cart
    def add_sale_item_to_cart(self):

        # find all the products from sale slider
        self.wait_for_presence_off_all_elements(self.PRODUCTS_UNDER_LATEST_ON_SALE)
        products = self.find_elements(*self.PRODUCTS_UNDER_LATEST_ON_SALE)

        for item in range(len(products)):
            # remember item name
            product_name = self.find_elements(*self.LATEST_ON_SALE_PRODUCT_NAME)[item].get_attribute('textContent')

            # click on product image and go to product page
            product_views = self.find_elements(*self.SALE_ITEM_PICTURES)
            product_views[item].click()

            # click add to cart button on product page
            product = Product(self.driver)
            product.click_add_to_cart()

            # verify shopping cart counter changes to 1
            banner = TopMenu(self.driver)
            banner.verify_cart_counter('1')

            # click shopping cart button and go to cart page
            banner.click_cart_button()

            # verify quantity of items in the cart equals 1
            shopping_cart = ShoppingCart(self.driver)
            shopping_cart.verify_quantity_in_the_cart('1')

            # verify user added product with correct name
            shopping_cart.verify_added_product_name(product_name)

            # empty the shopping cart
            shopping_cart.remove_item_from_card()

            # return to home page
            self.open_page()
