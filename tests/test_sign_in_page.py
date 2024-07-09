import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.base_test import BaseTest

from pages.main_page import MainPage
from pages.scroll_page import Scroll_page

from utils.locators import MainPageLocators, patients_page
from utils.utils import time_Measurement, basic_analysis
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
        login.login_with_valid_user("valid_user",*MainPageLocators.DASHBOARD)
        main_page.open("patients")
        
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
        six_month_ago = time_Measurement.traverse_time_str_to_array(date_time_str=last_measurement)
        
        patient_url = self.driver.execute_script("""
            const y = document.querySelectorAll('a[title]')[0];
            return y.href;
        """)
        main_page.open(None, str(patient_url))
        
        time.sleep(5)
        element=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(patients_page.S_ID))
        element  = self.driver.find_element(*patients_page.S_ID)
       
        element.click() 
        time.sleep(5)
        inputs = main_page.find_elements(*patients_page.input_locate)

        inputs[0].send_keys(Keys.TAB)
        inputs[0].send_keys(Keys.BACK_SPACE)  
        inputs[0].send_keys('10232023')
        inputs[0].send_keys(Keys.TAB)
        inputs[0].send_keys(Keys.TAB)
        
        inputs[1].send_keys(Keys.TAB)
        inputs[1].send_keys(Keys.BACK_SPACE)  
        inputs[1].send_keys('04232024')
        
        search_btn = main_page.find_element(*patients_page.SEARCH_BTN)
        search_btn.click()
        
        rows = main_page.find_elements(*patients_page.rows)
        data = []
        for row_idx, row_vals in enumerate(rows):
            data_by_row = {}
            cols_vals = row_vals.find_elements(*(By.CSS_SELECTOR,"td"))
            for col_idx, col_value in enumerate(cols_vals):
                data_by_row[col_idx] = col_value.text
            data.append(data_by_row)
               
        analysis = basic_analysis(data)
        print(analysis.get_analysis_SYS())
        print(analysis.get_analysis_DIA())
        print(analysis.get_analysis_HR())