import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.Footer import VerifyFooter
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_verifyFooter:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.smoke
    def test_powerbyCheck(self, setup):
        self.logger.info("******************* Test_005_1_Verify Power By Footer *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login Successful ******************")
        self.logger.info("******************* Footer: Power by test started ***********************")

        self.pb = VerifyFooter(self.driver)
        self.pb.checkPowerBy()
        time.sleep(5)
        assert True
        self.lp.clickLogout()
        self.driver.close()

    def test_version(self, setup):
        self.logger.info("******************* Test_005_2_Verify Version Footer *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login Successful ******************")
        self.logger.info("******************* Footer: Version test started ***********************")

        self.pb = VerifyFooter(self.driver)
        self.pb.checkVersion()
        time.sleep(5)
        assert True
        self.lp.clickLogout()
        self.driver.close()
