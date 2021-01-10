from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginForm(Page):

    LOGIN_FORM_POPUP = (By.CSS_SELECTOR, 'div #login-form-popup')

    def verify_login_form_popup(self):
        self.find_element(*self.LOGIN_FORM_POPUP)
