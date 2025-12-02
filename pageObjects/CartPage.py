from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.webDriverUtils import WebDriverUtils
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

class CartPage:
    PLACE_ORDER = (By.XPATH, "//button[text() = 'Place Order']")

    def __init__(self, driver):
        self.driver = driver

    def verify_place_order_text(self):
        element = WebDriverUtils.wait_for_element(self.driver, self.PLACE_ORDER) 
        return element.text   