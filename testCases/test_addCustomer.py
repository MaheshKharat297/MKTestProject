import random
import string
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("******************* Test_003_AddCustomer *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login Successful ******************")
        self.logger.info("******************* Add Customer test started ***********************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.email = random_generator() + "@gmail.com"
        self.addcust.clickOnEmail(self.email)
        self.addcust.clickOnPassword("test123")
        self.addcust.clickOnFirstName("Mahesh")
        self.addcust.clickOnLastName("Kharat")
        self.addcust.setCustomerRoles("Male")
        self.addcust.clickOnDateOfBirth("7/29/1990")
        self.addcust.clickOnCompanyName("Gs Lab")
        self.addcust.clickOnIsTaxExempt()
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManageOfVendors("Vendor 1")
        self.addcust.clickOnActivecheck()
        self.addcust.clickOnAdminComment("Mahesh Kharat as Customer for NOPCustomer")
        self.addcust.clickOnSave()

        self.logger.info("******************* Saving Customer info ***********************")

        self.logger.info("******************* Add Customer validation started ***********************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        #print(self.msg)
        if 'successfully.' in self.msg:
            assert True == True
            self.logger.info("******************* Add customer test Passed ***********************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "AddCustomerFailed.png")
            self.logger.info("******************* Add customer test Failed ***********************")
            assert True == False

        self.lp.clickLogout()
        self.driver.close()
        self.logger.info("******************* Ending Test_003_AddCustomer ***********************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
