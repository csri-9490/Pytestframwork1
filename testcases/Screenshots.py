from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

option1=webdriver.ChromeOptions()
option1.headless=True
# option1.add_argument("--incognito")
def waits(n):
    time.sleep(n)
    return waits
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option1)
driver.get("https://www.flipkart.com/")
# driver.get_screenshot_as_file('csri1.png')
s=lambda x:driver.execute_script('return document.body.parentNode.scroll'+x)
driver.set_window_size(s('Width'),s('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('jason.png')
