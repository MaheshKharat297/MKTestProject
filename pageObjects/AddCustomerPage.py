from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer page
    lnkCustomers_menu_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    lnkCustomers_menuitem_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    btnAddnew_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"

    rdGenderMale_xpath = "//input[@id='Gender_Male']"
    rdGenderFemale_xpath = "//input[@id='Gender_Female']"
    txtBirthDate_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    chkIsTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    txtCustomerRole_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    lstitmRegistered_xpath = "//span[contains(text(),'Registered')]"
    lstitmAdministrator_xpath = "//span[contains(text(),'Administrators')]"
    lstitmVendor_xpath = "//span[contains(text(),'Vendors')]"
    lstitmGuest_xpath = "//li[contains(text(),'Guests')]"
    drpManageVendors_xpath = "//select[@id='VendorId']"
    chkActive_xpath = "//input[@id='Active']"
    txtAdminContent = "//textarea[@id='AdminComment']"
    btnSave = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def clickOnEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def clickOnPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def clickOnFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def clickOnLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rdGenderMale_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rdGenderFemale_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdGenderMale_xpath).click()

    def clickOnDateOfBirth(self, birthdate):
        self.driver.find_element(By.XPATH, self.txtBirthDate_xpath).send_keys(birthdate)

    def clickOnCompanyName(self, companyname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(companyname)

    def clickOnIsTaxExempt(self):
        self.driver.find_element(By.XPATH, self.chkIsTaxExempt_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRole_xpath).click()
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitmRegistered_xpath)
        elif role == "Administrator":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitmAdministrator_xpath)
        elif role == "Vendor":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitmVendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitmGuest_xpath)

        self.driver.execute_script("arguments[0].click()", self.listitem)

    def setManageOfVendors(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpManageVendors_xpath))
        drp.select_by_visible_text(value)

    def clickOnActivecheck(self):
        self.driver.find_element(By.XPATH, self.chkActive_xpath).click()

    def clickOnAdminComment(self, admincomment):
        self.driver.find_element(By.XPATH, self.txtAdminContent).send_keys(admincomment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave).click()
