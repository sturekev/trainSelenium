import time
from tests.base_test import BaseTest

from pages.main_page import MainPage
from pages.sub0_pages import ExtrPages

from utils.locators import MainPageLocators, patients_page

class Test_care_plan(BaseTest):
    
    def test_setup(self):
        page = MainPage(self.driver)
        
        login = page.click_sign_in_button()
        login.login_with_valid_user("valid_user")
        patient_page  = page.get_patient_1001(page)
        page  = patient_page.get_test_patient()
        # return super().Setup()
        care_plans_elements = page.find_elements(*patients_page.care_plan_headers)
        
        def test_care_plan_headers():
            time.sleep(5)
            print (len (care_plans_elements))
            assert len(care_plans_elements) == 2
            assert care_plans_elements[0].text.split("\n")[0] == "Congestive Heart Failure"
            assert care_plans_elements[1].text.split("\n")[0] == "Hypertension"
            care_plans_elements[0].find_elements()
        #run subtest
        test_care_plan_headers()
            
        def test_CHF_properties():
            print("CHF TESTING ---------------")
            
            properties_element = page.find_element(*patients_page.CHF_properties_locator)
            properties  = properties_element.find_elements(*patients_page.Child_properties)
            assert properties[0].text == "Dry Weight"
            assert properties[1].text == "Risk Stratification Level"
            assert properties[2].text == "Objective Data"
            assert properties[3].text == "Devices"
            assert properties[4].text == "Frequency Of DMP Measurement"
            assert properties[5].text == "Alert Rules"
            assert properties[6].text == "Patient Reminder"
        #run subtest
        test_CHF_properties()
        
        def test_HT_properties():
            print("HT TESTING ---------------")
            properties_element = page.find_element(*patients_page.HT_properties)
            properties  = properties_element.find_elements(*patients_page.Child_properties)
            assert properties[0].text == "Dry Weight"
            assert properties[1].text == "Risk Stratification Level"
            assert properties[2].text == "Objective Data"
            assert properties[3].text == "Devices"
            assert properties[4].text == "Frequency Of DMP Measurement"
            assert properties[5].text == "Alert Rules"
            assert properties[6].text == "Patient Reminder"    
        #run subtest
        test_HT_properties()
        