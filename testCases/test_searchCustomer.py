import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchPage import SearchCustomer
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_searchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("******************* Test_004_1_SearchCustomer By Email *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login Successful ******************")
        self.logger.info("******************* Search Customer by email test started ***********************")

        self.ac = AddCustomer(self.driver)
        self.ac.clickOnCustomersMenu()
        self.ac.clickOnCustomersMenuItem()

        search_cust = SearchCustomer(self.driver)
        search_cust.setEmail("james_pan@nopCommerce.com")
        search_cust.searchClick()
        #search_cust.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

        status = search_cust.searchCustomerByEmail("james_pan@nopCommerce.com")
        assert True == status
        self.logger.info("******************* Search Customer by email test finished ***********************")
        self.lp.clickLogout()
        self.driver.close()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("******************* Test_004_2_SearchCustomer By Name *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login Successful ******************")
        self.logger.info("******************* Search Customer by Name test started ***********************")

        self.ac = AddCustomer(self.driver)
        self.ac.clickOnCustomersMenu()
        self.ac.clickOnCustomersMenuItem()

        search_cust = SearchCustomer(self.driver)
        search_cust.setFirstName("James")
        search_cust.setLastName("Pan")
        search_cust.searchClick()
        #search_cust.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

        status = search_cust.searchCustomerByName("James Pan")
        assert True == status
        self.logger.info("******************* Search Customer by Name test finished ***********************")
        self.lp.clickLogout()
        self.driver.close()