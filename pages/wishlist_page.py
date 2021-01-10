from selenium.webdriver.common.by import By
from pages.base_page import Page


class WishList(Page):

    WISH_LIST_PRODUCT_NAME = (By.CSS_SELECTOR, "td.product-name a")
    REMOVE_FROM_WISHLIST_BUTTON = (By.CSS_SELECTOR, "a.remove")
    WISHLIST_EMPTY_MESSAGE = (By.CSS_SELECTOR, "td.wishlist-empty")

    LINK_TO_ITEM_FROM_WISHLIST = (By.CSS_SELECTOR, "td.product-thumbnail a")

    SOCIAL_LOGOS = (By.CSS_SELECTOR, 'div.share-icons i')
    SOCIAL_MEDIA_ITEMS = ['icon-facebook', 'icon-twitter', 'icon-pinterest', 'icon-envelop']

    # verify product name in Wishlist
    def verify_wishlist_product_name(self, name: str):
        self.wait_for_element(self.WISH_LIST_PRODUCT_NAME)
        wishlist_product_name = self.find_element(*self.WISH_LIST_PRODUCT_NAME).get_attribute('textContent')
        assert name.strip() in wishlist_product_name, f'Expected to see {name}, but got {wishlist_product_name}'

    # Remove product from Wishlist
    def remove_item_from_wishlist(self):
        self.wait_for_element_click(self.REMOVE_FROM_WISHLIST_BUTTON)

    # verify Empty Wishlist message
    def verify_empty_wishlist_message(self):
        self.wait_for_element_visible(self.find_element(*self.WISHLIST_EMPTY_MESSAGE))
        wishlist_empty_message = self.find_element(*self.WISHLIST_EMPTY_MESSAGE).get_attribute('textContent')
        assert 'No products added to the wishlist' in wishlist_empty_message, \
            f'Expected to see "No products added to the wishlist", but got {wishlist_empty_message}'

    # verify User can see social logos
    def verify_social_logos(self):
        self.wait_for_presence_off_all_elements(self.SOCIAL_LOGOS)
        social_logos = self.find_elements(*self.SOCIAL_LOGOS)
        # verify quantity of social media icons matches requirements
        assert len(social_logos) == len(self.SOCIAL_MEDIA_ITEMS)
        # collect names of social media icons
        social_media_names = []
        for _ in range(len(social_logos)):
            social_media_names.append((self.find_elements(*self.SOCIAL_LOGOS)[_]).get_attribute('class'))
        # verify required social media links exist even if they are be in different order
        for _ in range(len(self.SOCIAL_MEDIA_ITEMS)):
            assert self.SOCIAL_MEDIA_ITEMS[_] in social_media_names, \
                f"Expected to see {self.SOCIAL_MEDIA_ITEMS[_]}, but couldn't find it"

    # click on wishlist item link
    def click_item_link(self):
        self.wait_for_element_click(self.LINK_TO_ITEM_FROM_WISHLIST)
