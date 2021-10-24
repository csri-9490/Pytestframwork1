import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
# from testdata.HomePageData import HomePageData
from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formsubmission(self,getdata):
        log=self.getLogger()
        #driver = webdriver.Chrome("")
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
       # driver.maximize_window()
        hmobj = HomePage(self.driver)
        #1# hmobj.getname().send_keys("srikatnhhh")
        #2#hmobj.getname().send_keys(getdata[0])
        hmobj.getname().send_keys(getdata["firstname"])
        log.info("fname etntry as" + getdata["firstname"])
        #self.driver.find_element_by_css_selector("[name='name']").send_keys("srikanth")
        #1#hmobj.getemail().send_keys("reddy")
        #2#hmobj.getemail().send_keys(getdata[1])
        hmobj.getemail().send_keys(getdata["email"])
        #self.driver.find_element_by_name("email").send_keys("reddy")
        hmobj.getid().click()
        #self.driver.find_element_by_id("exampleCheck1").click()
        #1#self.selectOption(hmobj.getgndr(),"Female")
        #2#self.selectOption(hmobj.getgndr(), getdata[2])
        self.selectOption(hmobj.getgndr(), getdata["gender"])
        #sel = Select(hmobj.gndr())--------------------
        #sel = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        #sel.select_by_visible_text("Male")
        hmobj.getsbmt().click()
        #self.driver.find_element_by_xpath("//input[@value='Submit']").click()
        alertText = hmobj.getalrt().text
        #alertText = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        assert ("success" in alertText)
        self.driver.refresh() # to overcome two test data entry in one field same time, not cleaering previous entry data



    #@pytest.fixture(params=[("pranav","singh","Male"),("shruthi","reddy","Female")])
    #@pytest.fixture(params=[{"firstname":"jason","email":"csri","gender":"Male"},{"firstname":"shruthi","email":"beauty","gender":"Female"}])
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    # @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    def getdata(self,request):
             return request.param



