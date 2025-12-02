from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.webDriverUtils import WebDriverUtils

class LoginPage:

    # -------- LOCATORS -------- #
    LOGIN_LINK = (By.ID, "login2")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space(text())='Log in']")
    CLOSE_BUTTON = (By.XPATH, "//button[normalize-space(text())='Log in']/preceding-sibling::button")
    LOGOUT_BUTTON = (By.ID, "logout2")

    def __init__(self, driver):
        self.driver = driver  # we will pass driver from test class

      # -------- PAGE ACTIONS -------- #
    def click_login_link(self):
        self.driver.find_element(*self.LOGIN_LINK).click() # here * is used for unpacking

    def enter_username(self, username):
        WebDriverUtils.enter_text(self.driver,self.USERNAME_INPUT,username)

    def enter_password(self, password):
        WebDriverUtils.wait_for_element(self.driver,self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        WebDriverUtils.wait_for_element(self.driver, self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.click_login_link()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()    

    def click_logout_button(self):
        WebDriverUtils.wait_for_element(self.driver, self.LOGOUT_BUTTON).click()
