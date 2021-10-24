from selenium.webdriver.common.by import By


class addtocart:

    def __init__(self,driver):
        self.driver=driver

    # addcart=(By.CSS_SELECTOR,"a[id='a-autoid-0-announce']")
    addcart=(By.XPATH,"//input[@id='add-to-cart-button']")

    def carting(self):
        return self.driver.find_element(*addtocart.addcart)