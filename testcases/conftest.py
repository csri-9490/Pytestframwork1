import pytest
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from testdata import HomePageData

driver = None # to sync the driver of  setup method and capture screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver # to sync the driver of  setup method and capture screenshot
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome(executable_path="D:/Selenium/browser/chromedriver.exe",options=options)

        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        # driver.get("http://121.241.54.185/MDDVICTORIAVIS/")
        # driver.get("https://www.goibibo.com/")
        # driver.get("https://www.amazon.in/")
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="D:/Selenium/browser/geckodriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    elif browser_name == "ie":
        print("ie browser")

    request.cls.driver=driver
    # yield
    # driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):

        driver.get_screenshot_as_file(name)


#updated


