from selenium.webdriver.common.by import By

class VerifyFooter:
    lnkPowerVy_xpath = '//a[contains(text(), \'nopCommerce\') and @href=\'https://www.nopcommerce.com/?utm_source=demo-admin-panel&utm_medium=footer&utm_campaign=admin-panel\']'
    txtVersion_xpath = '//b[contains(text(), "nopCommerce version 4.60.0")]'
    #txtDate_xpath = ''

    def __init__(self, driver):
        self.driver = driver

    def checkPowerBy(self):
        flag = False
        power_statement = self.driver.find_element(By.XPATH, self.lnkPowerVy_xpath).text
        print(power_statement)
        if power_statement == "nopCommerce":
            flag = True

    def checkVersion(self):
        flag = False
        version_no = self.driver.find_element(By.XPATH, self.txtVersion_xpath).text
        if version_no == "nopCommerce version 4.60.0":
            flag = True



