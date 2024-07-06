from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver



# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    def __init__(self, driver, base_url='https://go2.drkumo.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        self.first_window = driver.current_window_handle
        self.all_windows = driver.window_handles

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)
    
    def new_driver(self):
        self.driver.execute_script("window.open('');")
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != self.first_window:
                self.driver.switch_to.window(window)
                break

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator, time = 20):
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()
    
    def doi_element(self, *locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()