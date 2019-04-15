from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.logoutPage import LogoutPage
from utils import utils as utils
import allure

@pytest.mark.usefixtures("test_setup")
class TestLogin():


    def test_login(self):
        driver = self.driver
        try:
            driver.get(utils.URL)

            login = LoginPage(driver)
            login.click_signin()
            login.enter_username(utils.USERNAME)
            login.continue_topassword()
            login.enter_password(utils.PASSWORD)
            login.signinToHome()
            x = driver.title
            assert x == "abc"
        except AssertionError as error:
            print("Assertion error accrued")
            print(error)

            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise

        # driver.get("https://www.booking.com/")
        # driver.find_element_by_xpath("//span[contains(text(),'Sign in')]").click()
        # driver.find_element_by_id("username").send_keys("bremoo872@hotmail.com")
        # driver.find_element_by_xpath("//button[@type='submit']").click()
        # driver.find_element_by_id("password").send_keys("ibrahem123")
        # driver.find_element_by_xpath("//button[@type='submit']").click()

    def test_logout(self):
        driver = self.driver
        logout = LogoutPage(driver)
        logout.click_accountLink()
        logout.click_signout()
        # driver.find_element_by_id("current_account").click()
        # driver.find_element_by_xpath("//input[@value='Sign out']").click()

