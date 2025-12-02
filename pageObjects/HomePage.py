from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.webDriverUtils import WebDriverUtils
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException


class HomePage:
# locators
    LIST_OF_PRODUCTS = (By.XPATH, "//div[@id = 'tbodyid']/div/div//h4/a")
    PRODUCT_TO_BE_SELECTED = (By.XPATH, "//a[text() = 'Samsung galaxy s7']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[text() = 'Add to cart']")
    CART_LINK = (By.ID, "cartur")
    PRODUCT_TITLE = (By.TAG_NAME, "h2")
    

    def __init__(self, driver):
        self.driver = driver

    def select_product(self, productName):
        WebDriverUtils.wait_for_visibility_of_all_elements(self.driver, self.LIST_OF_PRODUCTS)
        products = self.driver.find_elements(*self.LIST_OF_PRODUCTS)

        for product in products:
            value = product.text.strip()
            print("product name", value)
            if value == productName:
                try:
                    # Try to click
                    fresh_product = self.driver.find_element(By.XPATH, f"//a[text()='{productName}']")
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", fresh_product)
                    ActionChains(self.driver).move_to_element(fresh_product).click().perform()
                except StaleElementReferenceException:
                    # Refetch and retry if stale
                    fresh_product = self.driver.find_element(By.XPATH, f"//a[text()='{productName}']")
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", fresh_product)
                    ActionChains(self.driver).move_to_element(fresh_product).click().perform()
                break

    def select_product_01(self, productName):

        xpath = f"//a[text()='{productName}']"
        product =  WebDriverUtils.wait_for_element_to_be_clickable(self.driver,(By.XPATH, xpath))
         

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product)
        #ActionChains(self.driver).move_to_element(product).click().perform()
        self.driver.execute_script("arguments[0].click();", product)

        #WebDriverUtils.wait_for_text_in_element(self.driver, self.PRODUCT_TITLE, productName)


    def click_on_alert_Btn(self):
        WebDriverUtils.wait_for_element(self.driver, self.ADD_TO_CART_BUTTON).click()
        WebDriverUtils.handle_alert(self.driver)

    def click_on_alert_link(self):
        WebDriverUtils.wait_for_element(self.driver, self.CART_LINK).click()    

