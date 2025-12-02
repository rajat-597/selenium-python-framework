from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.webDriverUtils import WebDriverUtils
import time


class TestHomepage:

    logger = LogGen.loggen()

    def test_product_to_cart(self, driver):
        self.logger.info("**************** Test HomePage *******************")
        driver = driver
        driver.get(ReadConfig.getApplicationURL())
        login = LoginPage(driver)
        login.login(ReadConfig.getUsername(), ReadConfig.getPassword())

        homepage = HomePage(driver)
        homepage.select_product_01("Samsung galaxy s7")
        actual_title = driver.title
        if actual_title == 'STORE':
            print("We have sucessfully selected the products")
            self.logger.info("**************** Title is correct,We have sucessfully selected the products *******************")
            assert True
        else:
            self.logger.info("**************** there is some issue with product selection *******************")
            assert False
        try:
            homepage.click_on_alert_Btn()
            self.logger.info("Alert handled successfully after adding product to cart")
        except Exception as e:
            self.logger.error(f"Error handling alert: {e}")
            driver.save_screenshot(".\\Screenshots\\alert_error.png")
            assert False


