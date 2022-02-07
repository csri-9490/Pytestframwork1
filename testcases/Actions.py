import time

from selenium import webdriver
from selenium.webdriver import ActionChains

# from testcases.conftest import tdat
# from testdata.HomePageData import HomePageData
# from zmq.sugar.constants import found
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
# from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from testcases.test_entry6 import s1
from testdata import HomePageData
from utilities.BaseClass import BaseClass



# driver=webdriver.Chrome(executable_path='D:\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.flipkart.com/")
driver.maximize_window()
s=[]
with open("C:\\Users\\srika\\PycharmProjects\\automation\\Pytestframwork1\\testcases\\td.txt") as f:
 lines=f.readlines()
for l in lines:
  r=l.split(",")[0]
s.append(r)
print('s details',s)
driver.implicitly_wait(5)
actions = ActionChains(driver)
driver.find_element(By.CSS_SELECTOR,"._2KpZ6l._2doB4z").click()
driver.find_element(By.CSS_SELECTOR,"a._1_3w1N").click()
driver.find_element(By.CSS_SELECTOR,"input[class='_2IX_2- VJZDxU']").send_keys(s)
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@class='_2IX_2- _3mctLh VJZDxU']").send_keys(s1.tdata["pwd"])
driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
time.sleep(5)
menu = driver.find_element(By.XPATH,"//img[@alt='Electronics']")
actions.move_to_element(menu).perform()
child = driver.find_element(By.XPATH,"//a[normalize-space()='Bluetooth Headphones']")
actions.move_to_element(child).click().perform()
time.sleep(5)
driver.back()
time.sleep(5)
#s1.tdata["uname"]
mobile=driver.find_element(By.XPATH,"//img[@alt='Mobiles']")
actions.context_click(mobile).click().perform()
time.sleep(10)
# driver.execute_script("window.scrollBy(0,2000)","")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")#for end of page scroll
time.sleep(5)
double=driver.find_element(By.XPATH,"//div[@class='_1AtVbE col-12-12']//div[2]//div[1]//a[1]//div[1]//img[2]")
time.sleep(5)
actions.double_click(double).perform()
time.sleep(5)

