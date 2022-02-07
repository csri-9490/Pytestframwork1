from selenium import webdriver

driver=webdriver.Chrome(executable_path='D:\drivers\chromedriver.exe')

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.switch_to.new_window()
child=driver.window_handles[1]
driver.switch_to.window(child)
driver.get("https://www.google.com/")
parent=driver.window_handles[0]
driver.switch_to.window(parent)
driver.find_element_by_css_selector("[name='name']").send_keys("dfsfsdf")