import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import  expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://h5p.org/tutorial-drag-and-drop-question")
driver.maximize_window()
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"google_esf")))
# driver.switch_to.frame("google_esf")
time.sleep(10)
# driver.switch_to.frame("google_esf")
driver.execute_script("window.scrollBy(0,1000)","")
driver.implicitly_wait(10)
target=driver.find_element(By.XPATH,"//p[normalize-space()='Rubus']")
dest=driver.find_element(By.XPATH,"//div[@class='h5p-inner ui-droppable']")
actions=ActionChains(driver)
actions.drag_and_drop(target,dest).perform()
