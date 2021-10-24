from selenium.webdriver.common.by import By

from PageObjects.amz_cart import addtocart


class amazon_hm:

    def __init__(self,driver):
        self.driver=driver

    search=(By.CSS_SELECTOR,"#twotabsearchtextbox")
    riceckr=(By.XPATH,"//span[normalize-space()='rice cooker']")
    item=(By.CSS_SELECTOR,"span[class='celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1'] span[class='a-size-medium a-color-base a-text-normal']")

    def searchitems(self):
        return self.driver.find_element(*amazon_hm.search)

    def ricecooker(self):
        return  self.driver.find_element(*amazon_hm.riceckr)

    def itemselect(self):
        self.driver.find_element(*amazon_hm.item).click()
        addingcart = addtocart(self.driver)
        return  addingcart
