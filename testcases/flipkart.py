import time

import pytest

from PageObjects.Amazon_home import amazon_hm
from PageObjects.amz_cart import addtocart
from utilities.readProperties import readfiles

class Testflip():
    @pytest.mark.usefixtures("setup")
    def test_m1(self):
        self.driver.implicitly_wait(10)
        self.driver.get(readfiles.readurl())  #https://www.amazon.in/
        amzn_search=amazon_hm(self.driver)
        # self.driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("electric")
        amzn_search.searchitems().send_keys("electric")

        time.sleep(10)
        # self.driver.find_element_by_xpath("//span[normalize-space()='rice cooker']").click()
        amzn_search.ricecooker().click()
        prds=self.driver.find_elements_by_xpath("//div[@class='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20']/div[@class='sg-col-inner']/div[@class='a-section a-spacing-none']/div/h2")
        for i in prds:
             print(i.text)
        # self.driver.find_element_by_css_selector("span[class='celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1'] span[class='a-size-medium a-color-base a-text-normal']").click()
        addingcart=amzn_search.itemselect()
        childwindow = self.driver.window_handles[1]
        self.driver.switch_to.window(childwindow)
        # self.driver.find_element_by_css_selector("a[id='a-autoid-0-announce']").click()
        # addingcart=addtocart(self.driver)
        addingcart.carting().click()
        self.driver.find_element_by_xpath("//input[@id='ap_email']").send_keys("9490219077")
        self.driver.find_element_by_xpath("//input[@id='continue']").click()
        self.driver.switch_to.window(self.driver.window_handles[0])


