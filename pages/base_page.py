import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class UrlChanges(object):
    """An expectation for checking that current url changes to new url
    url - used to find the url of the current page
    returns the new url once it differs from old one
    """
    def __init__(self, url):
        self.url = url

    def __call__(self, driver):
        new_url = driver.current_url
        if new_url != self.url:
            return new_url
        else:
            return False


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://gettop.us/'
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def open_product_page(self, url: str):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def wait_for_element(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(*locator))

    def wait_for_element_click(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(*locator)).click()

    def wait_for_element_clickable(self, *element):
        self.driver.wait.until(EC.element_to_be_clickable(*element))

    def wait_for_element_visible(self, element):
        self.driver.wait.until(EC.visibility_of(element))

    def wait_for_element_disappear(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element(*locator))

    def wait_for_element_stale(self, element):
        self.driver.wait.until(EC.staleness_of(element))

    def wait_for_presence_off_all_elements(self, *locator):
        self.driver.wait.until(EC.presence_of_all_elements_located(*locator))

    # custom wait condition for url change
    def wait_for_url_change(self, current_url):
        self.driver.wait.until(UrlChanges(current_url))

    # Verify string 'link' matches the current url
    def verify_link(self, link: str):
        current_link = self.driver.current_url
        assert current_link == link, f"Expected to open {link}, but get {current_link}"

    # grab the link 'href' value from all 'a' link tags.
    # Use only XPATH for locators
    def grab_href_links_from_a_tags(self, *locator):
        list_of_links = []
        links = self.driver.find_elements(*locator)
        for link in links:
            list_of_links.append(link.get_attribute("href"))
        return list_of_links

    def verify_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).get_attribute('textContent')
        assert expected_text in actual_text, f'Expected text {expected_text}, but got {actual_text}'

    # verify link loads correctly
    def verify_image_present(self, *locator):
        self.driver.wait.until(EC.visibility_of(self.driver.find_element(*locator)))
        link = self.driver.find_element(*locator).get_attribute('src')
        status = requests.get(link)
        assert status.status_code == 200, "image not found"

    # Verify string 'partial link' matches the part of current link
    def verify_partial_link(self, partial_link: str):
        link = self.driver.current_url
        assert partial_link in link, f"Expected to open Sign In page, but get {link}"
