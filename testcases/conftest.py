import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="D:/Selenium/browser/chromedriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="D:/Selenium/browser/geckodriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    elif browser_name == "ie":
        print("ie browser")





    request.cls.driver=driver




