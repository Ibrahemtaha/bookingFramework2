class LogoutPage():

    def __init__(self, driver):
        self.driver = driver

        ## Objects
        self.account_link_id = "current_account"
        self.signout_link_xpath = "//input[@value='Sign out']"

    def click_accountLink(self):
        self.driver.find_element_by_id(self.account_link_id).click()

    def click_signout(self):
        self.driver.find_element_by_xpath(self.signout_link_xpath).click()
