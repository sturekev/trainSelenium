from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    # LOGO = (By.ID, 'nav-logo')
    # ACCOUNT = (By.ID, 'nav-link-accountList')
    # SIGNUP = (By.CSS_SELECTOR, '#nav-signin-tooltip > div > a')
    # LOGIN = (By.CSS_SELECTOR, '#nav-signin-tooltip > a')
    # SEARCH = (By.ID, 'twotabsearchtextbox')
    # SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
    DASHBOARD = (By.ID, "title-id")
    RPM_BTN = (By.ID, "rpm-wrapper-btn-id")

class patients_page(object):
    GENERAL_BTNs = (By.CSS_SELECTOR, "button[type='button']")
    GENERAL_BTN = (By.CSS_SELECTOR, "button[type='button'][6]")
    SEARCH_ID = (By.ID, "ats-input-text-search-comp")
    SCHEDULE_ID = (By.ID, 'data-date')
    S_ID = (By.XPATH, "//p[contains(@class,'css-1dzwkkb')]")
    
    
    # LIST_LOCATORS = (By.NAME)


class LoginPageLocators(object):    
    USERNAME = (By.NAME, "email")
    PASSWORD = (By.ID, "outlined-adornment-password")
    SUBMIT = (By.ID, "btn-sign-in")
    ERROR_MESSAGE = (By.CLASS_NAME, "css-1xsto0d")
    PASSWORD_REQUIRE = (By.ID, "outlined-adornment-password-helper-text")

