from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class TestLoginDDT:
    BASE_URL= ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, driver):
        self.logger.info("******* Starting Login DDT Test **********")
        driver = driver
        driver.get(self.BASE_URL)

        login_page = LoginPage(driver)

        rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.logger.info(f"Total rows: {rows}")
        result = []


        for r in range(2, rows + 1):
            username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            expected = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.logger.info(f"Testing with username: {username}, password: {password}")

            login_page.login(username, password)
            try:
                #alert = driver.switch_to.alert
                alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
                alert.accept()
                actual = "fail"
            except TimeoutException:
                actual = "pass"
                login_page.click_logout_button()  

            # Compare results
            if actual == expected:
                result.append("pass")
            else:
                result.append("fail")

            # Always return to login page for next iteration
            driver.get(self.BASE_URL)
                
        assert "fail" not in result, "Login DDT test failed for some rows!"
            