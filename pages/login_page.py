from utils.locators import *
from pages.base_page import BasePage
from pages.home_page import HomePage

from utils import users, locators

from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)  # Python2 version

    def enter_email(self, email):
        self.find_element(*self.locator.USERNAME).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.SUBMIT).click()

    def login(self, user):
        user = users.get_user(user)
        print(user)
        self.enter_email(user["email"])
        self.enter_password(user["password"])
        self.click_login_button()

    def login_with_valid_user(self, user, locator = locators.MainPageLocators.DASHBOARD):
        self.login(user)
        self.wait_element(*locator)
        return HomePage(self.driver)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*self.locator.ERROR_MESSAGE)
