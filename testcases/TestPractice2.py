import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
class Test1:
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get("https://rahulshettyacademy.com/angularpractice/")

    @pytest.mark.parametrize("username,password",[("sr@gmail.com",1234),("dg@gmail.com","erer")])
    def test_login(self,username,password):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.find_element(By.CSS_SELECTOR,"input[class='form-control ng-untouched ng-pristine ng-invalid']").send_keys(username)
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys(password)
        time.sleep(5)

