class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        ## Objects
        self.signin1_button_xpath = "//span[contains(text(),'Sign in')]"
        self.username_text_id = "username"
        self.continue_button_xpath = "//button[@type='submit']"
        self.password_text_id = "password"
        self.signinToHome_button_xpath = "//button[@type='submit']"

    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin1_button_xpath).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_text_id).clear()
        self.driver.find_element_by_id(self.username_text_id).send_keys(username)

    def continue_topassword(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_text_id).clear()
        self.driver.find_element_by_id(self.password_text_id).send_keys(password)

    def signinToHome(self):
        self.driver.find_element_by_xpath(self.signinToHome_button_xpath).click()
