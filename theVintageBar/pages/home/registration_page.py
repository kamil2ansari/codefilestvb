from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class RegistrationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  locators for Registration Page
    _registration_button = "//ul[contains(@class,'cart-sign')]//span[2]"
    _emailRegistration_field = "//div[contains(@class,'register-form')]//div[2]/input"
    _join_us_button = "//button[contains(text(),' JOIN US NOW ')]"
    _passwordRegistration_field = "//input[contains(@placeholder,'Password *')]"
    _name_field = "//input[contains(@placeholder,'Name *')]"
    _create_an_account = "// button[contains(text(),'CREATE AN ACCOUNT ')]"
    _cancel_icon = "//i[contains(@class,'material-icons')]"

    def registrationLink(self):
        self.elementClick(self._registration_button, locatorType="xpath")

    def enterNewMail(self, emailReg):
        self.sendKeys(emailReg, self._emailRegistration_field, locatorType="xpath")

    def joinButtonClick(self):
        self.elementClick(self._join_us_button, locatorType="xpath")

    def enterRegistrationPass(self, passwordRegistration):
        self.sendKeys(passwordRegistration, self._passwordRegistration_field, locatorType="xpath")

    def enterRegistrationName(self, nameRegistration):
        self.sendKeys(nameRegistration, self._name_field, locatorType="xpath")

    def createAnAccount(self):
        self.elementClick(self._create_an_account, locatorType="xpath")

    def cancelIconButton(self):
        self.elementClick(self._cancel_icon, locatorType="xpath")

    def registration(self, emailReg="", passwordRegistration="", nameRegistration=""):
        self.enterNewMail(emailReg)
        self.joinButtonClick()
        self.enterRegistrationPass(passwordRegistration)
        self.enterRegistrationName(nameRegistration)
        self.createAnAccount()

    def verifyRegistrationSuccessful(self):
        result = self.isElementPresent("//ul[contains(@class,'cart-sign')]/li/a/i", locatorType="xpath")
        return result

    def verifyValidationMessageForEmail(self):
        result = self.isElementPresent("//div[contains(@class,'form-group')]//div[1]/span", locatorType="xpath")
        return result
