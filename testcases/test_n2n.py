import pytest

from PageObjects.CheckOut import Che
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By


class Testone(BaseClass):
    def test_n2n(self):
         homepage=HomePage(self.driver)
         #homepage.shopitems().click()  ---for thise we are handling click in checkout page  class and shpitem method and returned as  checkut,same passing here
         #self.driver.find_element_by_css_selector("a[href*='shop']").click()
         checkut= homepage.shopitems()
         #checkut=checkout(self.driver) #moved this to home page
         products = checkut.carttiems()
         #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")


#//div[@class='card h-100']/div/h4/a
#product =//div[@class='card h-100']
         for product in products:
              #productName = checkut.prdtxts().text
              productName = product.find_element_by_xpath("div/h4/a").text
              #productName = product.text

              if productName == "Blackberry":
                   #product.checkut.getberrys().click()
                   product.find_element_by_xpath("div/button").click()

                   #Add item into cart


         self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
         #checkut.checkout().click()
         #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
         confirmpg = checkut.checkout()
         self.driver.find_element_by_id("country").send_keys("ind")
         self.waitlinkprsnce("India") # here we are inherting the parent class, we can use self to use baseclass method
         self.driver.find_element_by_link_text("India").click()
         self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
         self.driver.find_element_by_css_selector("[type='submit']").click()
         successText = self.driver.find_element_by_class_name("alert-success").text

         assert "Success! Thank you!" in successText

         # self.driver.get_screenshot_as_file("screen.png")


