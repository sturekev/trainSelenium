from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpBasePage
from utils.locators import *


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        locator = self.locator.DASHBOARD
        return True if self.find_element(*locator) else False

    def search_item(self, search_locator, list_locator, item):
        self.find_element(*search_locator).send_keys(item)
        self.find_element(*search_locator).send_keys(Keys.ENTER)
        return self.find_element(*list_locator).text
    
    def search_items(self, search_locator, list_locator, item):
        self.find_element(*search_locator).send_keys(item)
        self.find_element(*search_locator).send_keys(Keys.ENTER)
        return self.find_elements(*list_locator)
    
    def send_key(self, keys):
        self.driver.send_keys(keys)

    # def click_sign_up_button(self):
    #     self.find_element(*self.locator.SIGNUP).click()
    #     return SignUpBasePage(self.driver)

    def click_sign_in_button(self):
        return LoginPage(self.driver)
