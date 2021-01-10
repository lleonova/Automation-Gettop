from selenium.webdriver.common.by import By
from pages.base_page import Page
from pages.categories_page import Category


class BrowseCategories(Page):

    BROWSE_OUR_CATEGORIES_TEXT = (By.CSS_SELECTOR, 'span.section-title-main[style]')
    CATEGORIES = (By.CSS_SELECTOR, 'div.flickity-viewport div.product-category')
    CATEGORY_NAMES = (By.CSS_SELECTOR, 'div.flickity-viewport div.product-category h5')
    CATEGORY_LINKS = (By.CSS_SELECTOR, 'div.flickity-viewport div.product-category a')

    # verify text for Browse categories is shown
    def verify_browse_text(self, text: str):
        self.verify_text(text, *self.BROWSE_OUR_CATEGORIES_TEXT)

    # Confirm there are {number} categories under Browse Our Categories
    def verify_number_of_categories(self, number: str):
        self.wait_for_presence_off_all_elements(self.CATEGORIES)
        categories = self.find_elements(*self.CATEGORIES)
        assert len(categories) == int(number), f"Expected to see {number} categories, but got {len(categories)}"

    # Verify category names match names from {arrow}
    def verify_category_names(self, array):
        self.wait_for_presence_off_all_elements(self.CATEGORY_NAMES)
        category_names = self.find_elements(*self.CATEGORY_NAMES)
        for _ in range(len(category_names)):
            text = category_names[_].get_attribute('textContent')
            assert array[_] in text, f'Expected to see {array[_]}, but got {text}'

    # Verify User can select trough categories and correct page opens
    def verify_correct_category(self):
        # find all categories
        self.wait_for_presence_off_all_elements(self.CATEGORIES)
        categories = self.find_elements(*self.CATEGORIES)

        for _ in range(len(categories)):

            # remember name ot the category
            category_name = (self.find_elements(*self.CATEGORY_NAMES)[_]).text
            # click category's link
            self.find_elements(*self.CATEGORY_LINKS)[_].click()

            # verify opened category page has correct name
            category_page = Category(self.driver)
            category_page.verify_correct_category_name(category_name)

            # return to home page
            self.open_page()
