import main
import inspect
import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("tdat")



class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    #def waitlinkprsnce(self):        ############using below one, becuase we optimized to reuse, insted of hard code the india text
    #    wait = WebDriverWait(self.driver, 7)
    #    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

    def waitlinkprsnce(self,text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


    def selectOption(self,locator,text):
        #sel = Select(hmobj.gndr())
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def takescreenshots(self,driver):
        fileName=str(round(time.time()*1000))+".png"
        scrnshtpath = "/users/desktop/"
        destfile = scrnshtpath + fileName
        try:
            driver.save_screenshot(scrnshtpath)
            print("scrnshot saved to path")
        except NotADirectoryError:
            print("not a directry issues")
