# from selenium import webdriver
from base.basepage import BasePage
# from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


'''
Registration link x-path: //ul[contains(@class,'cart-sign')]//span[2]
Email input x-path: //div[contains(@class,'register-form')]//div[2]/input
Join us button x-path: //button[contains(text(),' JOIN US NOW ')]
NEXT FORM
Password field x-path: //input[contains(@placeholder,'Password *')]
Name field x-path: //input[contains(@placeholder,'Name *')]
Create an Account X: // button[contains(text(),'CREATE AN ACCOUNT ')]
'''

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for login page
    _sign_in_button = "//div[contains(@class,'right-top')]//a/span[contains(text(),'Sign')]"
    _email_field = "//div[contains(@class,'create-account')]//input[contains(@placeholder,'Email *')]"
    _password_field = "//div[contains(@class,'create-account')]//input[contains(@placeholder,'Password *')]"
    _login_button = "//button[contains(text(),'SIGN')]"
    _close_icon = "//button/i[contains(@class,'material-icons')]"

    # def waiting(self):
    #   self.waitForElement(self._login_link, locatorType="xpath")

    # def clickLoginLink(self):
    #  self.elementClick(self._login_link, locatorType="xpath")

    def signInLink(self):
        self.elementClick(self._sign_in_button, locatorType="xpath")

    # def jumpToPopUP(self):
    #    self.driver.switch_window

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def closeLoginForm(self):
        self.elementClick(self._close_icon, locatorType="xpath")

    def login(self, email="", password=""):
        # self.waiting()
        # self.clickLoginLink()
        # self.clearFields()
        # time.sleep(3)
        # self.signInLink()
        # self
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//li/a/i", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Invalid credentials')]", locatorType="xpath")
        return result

    def verifyNotLoginBlank(self):
        result = self.isElementPresent("//span[contains(text(),'Password is required')]", locatorType="xpath")
        return result

    def verifyNotLoginBlankPass(self):
        result = self.isElementPresent("//span[contains(text(),'Password is required')]", locatorType="xpath")
        return result

    def verifyNotLoginBlankNMailId(self):
        result = self.isElementPresent("//span[contains(text(),'Email address is required')]", locatorType="xpath")
        return result

    def verifyPassMasked(self):
        result = self.isElementDisplayed("//input[contains(@type,'password')]", locatorType="xpath")
        return result

    def verifyLoginPage(self):
        result = self.isElementPresent("//h3[contains(text(),'MEMBER SIGN IN')]", locatorType="xpath")
        return result

    def verifyLoginPage2(self):
        result = self.isElementPresent("//li/a/i", locatorType="xpath")
        return result

    def verifyLogout(self):
        # menu_button = self.elementClick('//button[contains(@id, "react-burger-menu-btn")]', locatorType="xpath")
        # time.sleep(7)
        menu_list = self.elementClick("//ul[contains(@class,'cart-sign')]//a[2]", locatorType="xpath")
        result = self.isElementPresent("//ul[contains(@class,'cart-sign')]//span[2]", locatorType="xpath")
        return result

    def refreshBrowser(self):
        return self.driver.refresh()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Testing the login")

    # def verifyPassMasked(self):
    #   result = self.

    # def verifyLoginFailedBlank(self):
    # result = self.isElementPresent("//center/b", locatorType="xpath")
    # return result

    # def verifyLoginBlankPass(self):
    #  result = self.isElementPresent("//center/b", locatorType="xpath")
    #  return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

# //div[contains(text(),'Invalid email or password.')]
# //center/b[contains(text(),'**Failed Login**')]
