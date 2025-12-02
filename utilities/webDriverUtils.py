from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class WebDriverUtils:

    @staticmethod
    def wait_for_element(driver, locator, timeout=10):
        """Wait until element is visible"""
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def click_element(driver, locator, timeout=10):
        """Wait until element is clickable and click"""
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @staticmethod
    def wait_for_visibility_of_all_elements(driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(
        EC.visibility_of_all_elements_located(locator)
    )

    @staticmethod
    def wait_for_element_to_be_clickable(driver, locator, timeout = 10):
        return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
)    

    @staticmethod
    def enter_text(driver, locator, text, timeout=10):
        """Wait until element is visible and enter text"""
        element = WebDriverUtils.wait_for_element(driver, locator, timeout)
        element.clear()
        element.send_keys(text)

    @staticmethod
    def scroll_to_element(driver, locator,timeout=10):
        """Scroll into element """
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @staticmethod
    def wait_for_text_in_element(driver, locator, expected_text, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.text_to_be_present_in_element(locator, expected_text)
        )
    
    @staticmethod
    def handle_alert(driver, accept=True, timeout=5):
        """Wait for alert and accept/dismiss"""
        try:
            WebDriverWait(driver, timeout).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            if accept:
                alert.accept()
            else:
                alert.dismiss()
        except TimeoutException:
            print("No alert appeared")

    @staticmethod
    def select_by_text(driver, locator, visible_text, timeout=10):
        """Select a dropdown option by visible text"""
        element = WebDriverUtils.wait_for_element(driver, locator, timeout)
        Select(element).select_by_visible_text(visible_text)

    @staticmethod
    def switch_to_frame(driver, locator, timeout=10):
        """Switch to frame using locator"""
        frame = WebDriverUtils.wait_for_element(driver, locator, timeout)
        driver.switch_to.frame(frame)

    @staticmethod
    def switch_to_default_content(driver):
        """Switch back to default content"""
        driver.switch_to.default_content()
