from selenium.webdriver.common.by import By
from pages.base_page import Page
from pages.quick_view import QuickView


class Category(Page):

    CATEGORIES_PAGE_MAME = (By.CSS_SELECTOR, 'nav.uppercase')
    HOME_LINK = (By.CSS_SELECTOR, "nav.uppercase a")

    ALL_PRODUCTS_IN_CATEGORY = (By.CSS_SELECTOR, 'div.product div.col-inner')

    # click on "home" link
    def click_home_link(self):
        self.wait_for_element_click(self.HOME_LINK)

    # verify category name matches {name}
    def verify_correct_category_name(self, name: str):
        category_name = self.find_element(*self.CATEGORIES_PAGE_MAME).get_attribute('textContent')
        assert name.upper() in category_name.upper(), f'Expected to see {name}, but got {category_name}'


    # def click_quick_view_buttons(self):
    #     quick_view = QuickView(self.driver)
    #     quick_view.open_and_closing_window()
