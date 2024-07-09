from utils.locators import *
from pages.base_page import BasePage


from selenium.webdriver.common.keys import Keys

class ExtrPages(BasePage):
    def __init__(self, driver, page):
        self.page = page
        super(ExtrPages, self).__init__(driver)  # Python2 version

    def get_test_patient (self,patient_full_name = "1001"):
        self.open_patient_page(patient_name=patient_full_name)
        self.get_patient_personal_page()
        return self.page
    
    def open_patient_page(self,patient_name):
        self.page.open("patients")
        self.page.wait_element(*patients_page.GENERAL_BTNs)
        button = self.page.find_elements(*patients_page.GENERAL_BTNs)
        button[6].click()
        self.page.wait_element(*patients_page.SEARCH_ID)
        target = self.page.find_element(*patients_page.SEARCH_ID)
        target.send_keys(patient_name)
        target.send_keys(Keys.ENTER)
        
    def get_patient_personal_page (self):
        patient_url = self.driver.execute_script("""
            const y = document.querySelectorAll('a[title]')[0];
            return y.href;
        """)
        self.page.open(None, str(patient_url))
        care_plan_btn = self.page.find_element(*patients_page.dash_care_btn)
        care_plan_btn.click()
        return self.page
        
        
        

    # def enter_email(self, email):
    #     self.find_element(*self.locator.USERNAME).send_keys(email)

    # def enter_password(self, password):
    #     self.find_element(*self.locator.PASSWORD).send_keys(password)

    # def click_login_button(self):
    #     self.find_element(*self.locator.SUBMIT).click()

    # def login(self, user):
    #     user = users.get_user(user)
    #     print(user)
    #     self.enter_email(user["email"])
    #     self.enter_password(user["password"])
    #     self.click_login_button()

    # def login_with_valid_user(self, user, locator = locators.MainPageLocators.DASHBOARD):
    #     self.login(user)
    #     self.wait_element(*locator)
    #     return HomePage(self.driver)

    # def login_with_in_valid_user(self, user):
    #     self.login(user)
    #     return self.find_element(*self.locator.ERROR_MESSAGE)
