from selenium.webdriver.common import keys

from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class TestCrm(BaseClass):
    def test_crm(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("#userid").send_keys("sathguru")
        self.driver.find_element_by_css_selector("#txtpassword").send_keys("Spd1234#")
        self.driver.find_element_by_css_selector("#submit").click()
        self.driver.find_element_by_xpath("//h2[normalize-space()='CRM']").click()
        self.driver.find_element_by_xpath("//body/div[@id='wrap']/div[@id='top']/nav[1]/div[1]/div[2]/ul[1]/li[3]/a[1]").click()
        self.driver.find_element_by_link_text("Leads").click()
        self.driver.find_element_by_xpath("//a[@id='btnaddnew']").click()
        self.driver.find_element_by_xpath("//input[@id='fldLeadName']").send_keys("leadnamesone")
        self.driver.find_element_by_xpath("//input[@id='fldLastName']").send_keys("fnames")
        self.driver.find_element_by_xpath("//div[@id='fldCompany']").click()
        orgns=self.driver.find_element_by_xpath("//div[@id='listBoxContentinnerListBoxjqxWidget1681f9bc04d9']/div/div")
        for i in orgns:
            print(i.get_attribute("innerText"))

        print(orgns.text)
        # self.driver.find_element_by_xpath("//button[@id='btnsave']").click()


