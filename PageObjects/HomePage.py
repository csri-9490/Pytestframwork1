from selenium.webdriver.common.by import By

from PageObjects.CheckOut import checkout


class HomePage:

    def __init__(self, driver): # to make connection between test case driver and here driver using constrctr because of thise we define driver as self.drver
        self.driver = driver


    shop=(By.CSS_SELECTOR,"a[href*='shop']")

    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    id = (By.ID, "exampleCheck1")
    gndr = (By.ID, "exampleFormControlSelect1")
    sbmit = (By.XPATH, "//input[@value='Submit']")
    alrt = (By.CSS_SELECTOR,"[class*='alert-success']")





    def shopitems(self):
        #return  self.driver.find_element(*HomePage.shop) # here '*' will be used deserialize and show like driver.find_element_by_css_selector("a[href*='shop']")
        self.driver.find_element(*HomePage.shop).click()
        checkut = checkout(self.driver)
        return checkut

    def getname(self):
        return self.driver.find_element(*HomePage.name)


    def getemail(self):
        return self.driver.find_element(*HomePage.email)
    def getid(self):
        return self.driver.find_element(*HomePage.id)
    def getgndr(self):
        return self.driver.find_element(*HomePage.gndr)
    def getsbmt(self):
        return self.driver.find_element(*HomePage.sbmit)
    def getalrt(self):
        return self.driver.find_element(*HomePage.alrt)

