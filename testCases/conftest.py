import pytest
from selenium import webdriver
import allure
import shutil
import os
from allure_commons.types import AttachmentType

# ------------ Browser Option ------------ #
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ------------ WebDriver Fixture ------------ #
@pytest.fixture()
def driver(browser):
    if browser == "chrome":
        print("Launching Chrome Browser...")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        print("Launching Firefox Browser...")
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Firefox(options=options)
    else:
        raise Exception("Invalid browser!")

    driver.maximize_window()
    yield driver
    driver.quit()

"""
# ------------ HTML Report Customization ------------ #
@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "BlazeDemo Automation Report"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.clear()
    prefix.extend([
        "Project Name: BlazeDemo",
        "Module Name: Products",
        "Tester: Rajat"
    ])
    """


# ------------ Allure Screenshot on Failure ------------ #
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        driver = item.funcargs.get("driver", None)

        # For class-based tests
        if driver is None and hasattr(item.instance, "driver"):
            driver = item.instance.driver

        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Failure Screenshot - {item.name}",
                    attachment_type=AttachmentType.PNG
                )
                print("Screenshot attached for:", item.name)
            except Exception as e:
                print("Screenshot not captured:", e)


# ------------ Clean Allure Results ------------ #
@pytest.fixture(scope="session", autouse=True)
def clean_allure_results():
    allure_folder = "allure-results"

    if os.path.exists(allure_folder):
        shutil.rmtree(allure_folder)
        print("Deleted old allure-results folder.")

    os.makedirs(allure_folder)
    print("Created new allure-results folder.")


# ------------ Generate Report at End ------------ #
#def pytest_sessionfinish(session, exitstatus):
#    os.system("allure generate allure-results -o allure-report --clean")
#    print("Allure report generated!")
