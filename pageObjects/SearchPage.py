from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SearchCustomer:
    txtEmail_xpath = '//input[@id="SearchEmail"]'
    txtFirstName_xpath = '//input[@id="SearchFirstName"]'
    txtLastName_xpath = '//input[@id="SearchLastName"]'
    drpDOBMonth_xpath = '//select[@id="SearchMonthOfBirth"]'
    drpDOBDay_xpath = '//select[@id="SearchDayOfBirth"]'
    txtRegistrationDateFrom_xpath = '//input[@id="SearchRegistrationDateFrom"]'
    txtRegistrationDateTo_xpath = '//input[@id="SearchRegistrationDateTo"]'
    txtLastActivityFrom_xpath = '//input[@id="SearchLastActivityFrom"]'
    txtLastActivityTo_xpath = '//input[@id="SearchLastActivityTo"]'
    txtCompany_xpath = '//input[@id="SearchCompany"]'
    txtIPAddress_xpath = '//input[@id="SearchIpAddress"]'
    lstCustomerRoles_xpath = '//ul[@id="SelectedCustomerRoleIds_taglist"]'
    lstitmRegistered_xpath = '//option[contains(text(),"Registered")]'
    lstitmGuest_xpath = '//option[contains(text(),"Guests")]'
    lstitmAdministrator_xpath = "//option[contains(text(),'Administrator')]"
    lstitmVendor_xpath = "//option[contains(text(),'Vendor')]"
    btnSearch_xpath = "//button[@id='search-customers']"
    tblSearchResult_xpath = "//div[@id='customers-grid_wrapper']"
    tblTable_xpath = "//table[@id='customers-grid']"
    tblTableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tblTableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    lstExportExcel_xpath = "//li[@id='exportexcel-selected']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def setDateOfBirthMonth(self, dateofbirth_month, dateofbirth_day):
        month = Select(self.driver.find_element(By.XPATH, self.drpDOBMonth_xpath))
        month.select_by_visible_text(dateofbirth_month)

        day = Select(self.driver.find_element(By.XPATH, self.drpDOBDay_xpath))
        day.select_by_visible_text(dateofbirth_day)

    def setRegistrationDateFrom(self, registration_date_from):
        self.driver.find_element(By.XPATH, self.txtRegistrationDateFrom_xpath).send_keys(registration_date_from)

    def setRegistrationDateTo(self, registration_date_to):
        self.driver.find_element(By.XPATH, self.txtRegistrationDateTo_xpath).send_keys(registration_date_to)

    def setLastActivityFrom(self, lastactivity_from):
        self.driver.find_element(By.XPATH, self.txtLastActivityFrom_xpath).send_keys(lastactivity_from)

    def setLastActivityTo(self, lastactivity_to):
        self.driver.find_element(By.XPATH, self.txtLastActivityTo_xpath).send_keys(lastactivity_to)

    def setCompany(self, company):
        self.driver.find_element(By.XPATH, self.txtCompany_xpath).send_keys(company)

    def setIpAddress(self, ipaddress):
        self.driver.find_element(By.XPATH, self.txtIPAddress_xpath).send_keys(ipaddress)

    def setCustomerRoles(self, customer_role):
        self.driver.find_element(By.XPATH, self.lstCustomerRoles_xpath).click()
        if customer_role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitmRegistered_xpath)
        elif customer_role == "Administrator":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitmAdministrator_xpath)
        elif customer_role == "Vendor":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitmVendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitmGuest_xpath)

        self.driver.execute_script("arguments[0].click()", self.listitem)

    def searchClick(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tblTableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tblTableColumns_xpath))

    def searchCustomerByEmail(self, email):
        print("Email received : " + email)
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.tblTable_xpath)
            email_id = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.tblTable_xpath)
            name_table = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name_table == name:
                flag = True
                break
        return flag
