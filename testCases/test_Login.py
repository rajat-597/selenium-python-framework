from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestLogin:
    BASE_URL= ReadConfig.getApplicationURL()
    USERNAME= ReadConfig.getUsername()
    PASSWORD= ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, driver):
        self.logger.info("*************** Test HomePage Title **********************")
        self.logger.info("*************** verifying Home page title  **********************")
        driver = driver
        driver.get(self.BASE_URL)
        actual_title = driver.title
        if actual_title == "STORE":
            assert True
            self.logger.info("*************** verified Home page title successfully **********************")

        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.info("***************  Home page title failed **********************")
            assert False

    def test_login(self,driver):
        self.logger.info("*************** Test Login **********************")
        self.logger.info("*************** verifying After login title  **********************")
        driver = driver
        #driver.get(self.BASE_URL)
        driver.get(ReadConfig.getApplicationURL())
        login = LoginPage(driver)
        login.login(self.USERNAME, self.PASSWORD)
        actual_title = driver.title

        if actual_title == "STORE":
            assert True 
            self.logger.info("*************** Login Successful **********************")
        else:
            self.logger.info("*************** Capture Screenshots **********************")
            driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.info("***************  Login Failed **********************")
            assert False   


