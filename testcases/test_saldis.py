import pytest
from selenium import webdriver
import self

from utilities.BaseClass import BaseClass


class saleDist(BaseClass):

    def __init__(self,name):
        self.name=name

    def sales(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='it1::content']").send_keys("sathguru") #css_selector
        self.driver.find_element_by_xpath("//input[@id='it2::content']").send_keys("T35T@2021")
        self.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()

