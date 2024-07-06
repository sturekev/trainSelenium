import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.base_test import BaseTest

from pages.main_page import MainPage
from pages.scroll_page import Scroll_page

from utils.locators import MainPageLocators, patients_page
from utils.utils import time_Measurement
# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestSignInPage(BaseTest):

    # def test_sign_in_with_in_valid_user(self):
    #     main_page = MainPage(self.driver)
    #     login_page = main_page.click_sign_in_button()
    #     result = login_page.login_with_in_valid_user("invalid_user")
    #     assert result.text == "Invalid credential"
        
    # def test_sign_in_with_valid_user(self):
    #     main_page = MainPage(self.driver)
    #     login_page = main_page.click_sign_in_button()
    #     result = login_page.login_with_valid_user("valid_user")
    #     self.assertIn("", result.get_url())
    
    def test_general_patient_page(self):
        main_page = MainPage(self.driver)
        login = main_page.click_sign_in_button()
        login.login_with_valid_user("valid_user")
        main_page.wait_element(*MainPageLocators.DASHBOARD)
        main_page.open("patients")
        
        # self.driver.implicitly_wait(10)
        main_page.wait_element(*patients_page.GENERAL_BTNs)
        button = main_page.find_elements(*patients_page.GENERAL_BTNs)
        button[6].click()
        main_page.wait_element(*patients_page.SEARCH_ID)
        target = main_page.find_element(*patients_page.SEARCH_ID)
        target.send_keys("1001")
        target.send_keys(Keys.ENTER)
        
        # this sleep not optimize        
        time.sleep(10)
        last_measurement = self.driver.execute_script("""
            const rowsWithClass = document.querySelectorAll('div.value')[0].innerHTML;
            return rowsWithClass;
        """)
        six_month_ago = time_Measurement.traverse_time_str_to_array(last_measurement )
        patient_url = self.driver.execute_script("""
            const y = document.querySelectorAll('a[title]')[0];
            return y;
        """)
        patient_url.click()
        
        print (main_page.get_url())
        time.sleep(5)
        # schedule = self.driver.execute_script("""
        #     const z = document.getElementById('data-date');
        #     z
        #     return z;
        # """)
        # main_page.doi_element(*patients_page.SCHEDULE_ID)
        # main_page.wait_element(*patients_page.S_ID,30)
        # self.driver.implicitly_wait(2)
        element = main_page.find_element(*patients_page.S_ID)
        
        wait = WebDriverWait(self.driver, timeout=2)
        wait.until(lambda d : element.is_displayed())
        
        
        # schedule.click()
        # main_page.wait_element(*patients_page.SCHEDULE_ID,30)
        # element = main_page.find_elements(*patients_page.SCHEDULE_ID)
        print (element)
        element.click()
        # WebDriverWait(self.driver, 10).until(lambda d: main_page.click() or True)
        # main_page.click()
        
        # start_date = main_page.find_elements(*(By.ID, ":r"))
        # for idx, val in enumerate(start_date):
        #     print(idx,val.text)
        # end_date = main_page.find_element(*(By.ID, ":r35:"))
        time.sleep(5)
        
        
        
        
        
        # time.sleep(30)