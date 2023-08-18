import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_Login_ddt:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):

        self.logger.info("****** Test_001_Login_ddt ******")
        self.logger.info("******************* Login verification started ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows are : ", self.rows)

        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            print("title is :", act_title)
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("********** Passed **********")
                    self.driver.save_screenshot(".//Screenshots//" + "Login_DDT_Passed.png")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("********** Failed **********")
                    self.driver.save_screenshot(".//Screenshots//" + "Login_DDT_Failed.png")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("********** Failed **********")
                    self.driver.save_screenshot(".//Screenshots//" + "Login_DDT_Failed.png")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("********** Passed **********")
                    self.driver.save_screenshot(".//Screenshots//" + "Login_DDT_Passed.png")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

        if "fail" not in lst_status:
            self.logger.info("********** Login DDT Test Passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Login DDt Test Failed **********")
            self.driver.close()
            assert False
        self.logger.info("***************** End of Login DDT Test *****************")
        self.logger.info("***************** Completed Test_001_Login_ddt *****************")



