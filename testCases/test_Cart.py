from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.webDriverUtils import WebDriverUtils
from pageObjects.CartPage import CartPage
import time


class TestCart:

    logger = LogGen.loggen()

    def test_check_out_button_presence(self, driver):
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

        homepage.click_on_alert_link()    

        cart = CartPage(driver)
        expected = cart.verify_place_order_text()
        if expected == 'Place Order':
            print("we have successfully landed to Cart Page") 
            self.logger.info("we have successfully landed to Cart Page")
            assert True
        else:
            self.logger("get some issue before coming to Cart Page")
            assert False





