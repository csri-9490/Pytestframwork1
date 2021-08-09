from selenium.webdriver.common.by import By

from PageObjects.confirmpage import confirm


class checkout:
    def __init__(self,driver):
        self.driver=driver

    carts=(By.XPATH,"//div[@class='card h-100']")
    berry=(By.XPATH,"div/button")
    prdtxt=(By.XPATH,"div/h4/a")
    out=(By.XPATH,"//button[@class='btn btn-success']")

    def carttiems(self):

        return   self.driver.find_elements(*checkout.carts)

    def prdtxts(self):

        return  self.driver.find_element(*checkout.prdtxt)

    def getberrys(self):
        return  self.driver.find_element(*checkout.berry)

    def checkout(self):

        #return  self.driver.find_element(*checkout.out)
        self.driver.find_element(*checkout.out).click()
        cnfrmobj = confirm(self.driver)
        return  cnfrmobj
