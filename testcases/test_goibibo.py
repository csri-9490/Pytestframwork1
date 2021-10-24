import time

from selenium.webdriver.common import keys

from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class TestCrm(BaseClass):
    def test_ibibo(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='gosuggest_inputSrc']").send_keys("Del")
        inner=self.driver.find_element_by_id("react-autosuggest-1")#.get_attribute("innerHTML")
        lielements=inner.find_elements_by_tag_name("li")
        time.sleep(5)
        for i in lielements:
            i.text=='Delhi'
            i.click()
            break
        time.sleep(10)
        self.driver.find_element_by_xpath("//input[@id='gosuggest_inputDest']").send_keys("Hyd")
        out = self.driver.find_element_by_id("react-autosuggest-1")
        lietolements = out.find_elements_by_tag_name("li")

        for i2 in lietolements:
            i2.text == 'Hyderabad'
            i2.click()
            break
        time.sleep(10)
        self.driver.save_screenshot("csri13.png")
        # BaseClass.takescreenshots(self.driver)




