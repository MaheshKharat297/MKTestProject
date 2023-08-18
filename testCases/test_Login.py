import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.smoke
    def test_homePageTitle(self, setup):

        self.logger.info("******************* Test_001_Login *******************")
        self.logger.info("******************* Home page verification started ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ Home page title test case passed ************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************ Home page title test case failed ************")
            assert False

    @pytest.mark.smoke
    def test_login(self, setup):

        self.logger.info("******************* Login verification started ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print("title is :", act_title)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************ Login test case passed ************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.driver.close()
            self.logger.error("************ Login test case failed ************")
            assert False

    @pytest.mark.smoke
    def test_logout(self, setup):

        self.logger.info("******************* Logout verification started ***********************")
        self.driver = setup
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print("\nInside title is :", act_title)
        self.lp.clickLogout()
        act_title_logout = self.driver.title
        print("After Logout title : ", act_title_logout)
        if act_title_logout == "Your store. Login":
            self.driver.save_screenshot(".//Screenshots//" + "test_logout.png")
            assert True
            self.driver.close()
            self.logger.info("************ Logout test case passed ************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_logout.png")
            self.driver.close()
            self.logger.error("************ Login test case failed ************")
            assert False
