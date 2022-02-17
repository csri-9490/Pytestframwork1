from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
v=[]
v1=["choice 2 1","choice 2","choice 7"]
def waits():
    driver.implicitly_wait(5)
    return waits
def dropdpwn_selection(ele,v1):
 if  v1[0]=='all':

    for i in ele:
       for j in range(len(v1)):
           if i.text==v1[j]:
               i.click()
               break
 else:
     try:
         for s in ele:
             s.click(12)
     except Exception as e:

         print("sdfsdf")

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.find_element(By.XPATH,"//input[@id='justAnInputBox']").click()
waits()
ele=driver.find_elements(By.CSS_SELECTOR,"span.comboTreeItemTitle")
actions=ActionChains(driver)
actions.send_keys_to_element()


# dropdpwn_selection(ele,"choice ")
dropdpwn_selection(ele,v1)
# for i in ele:
#     i.click()
#     print(i.text)