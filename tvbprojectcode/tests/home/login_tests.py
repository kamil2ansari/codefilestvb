# from selenium import webdriver
# from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=7)
    def test_validLogin(self):
        # self.lp.clearFields()
        # time.sleep(2)
        self.lp.closeLoginForm()
        # self.driver.get(self.baseURL)
        self.lp.signInLink()
        self.lp.login("kamil@vintagebardev.com", "KaA2018!")
        time.sleep(3)
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verified")
        # assert result2 == True
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "login successful")
        # assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.signInLink()
        self.lp.login("sellertesting@mailinator.com", "123456")
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_invalidNotLoginBlank(self):
        self.lp.refreshBrowser()
        # self.lp.closeLoginForm()
        self.lp.signInLink()
        # self.driver.refresh()
        # self.driver.get(self.baseURL)
        time.sleep(2)
        self.lp.login("", "")
        result = self.lp.verifyNotLoginBlank()
        assert result == True

    @pytest.mark.run(order=3)
    def test_invalidNotLoginBlankPass(self):
        self.lp.closeLoginForm()
        self.lp.signInLink()
        # self.driver.get(self.baseURL)
        self.lp.login("standard_user", "")
        result = self.lp.verifyNotLoginBlankPass()
        assert result == True

    @pytest.mark.run(order=4)
    def test_invalidNotLoginBlankMailId(self):
        # self.driver.refresh()
        # self.driver.get(self.baseURL)
        self.lp.closeLoginForm()
        self.lp.signInLink()
        self.lp.login("", "secret_sauce")
        result = self.lp.verifyNotLoginBlankNMailId()
        assert result == True

    @pytest.mark.run(order=5)
    def test_maskedPassword(self):
        self.lp.closeLoginForm()
        self.lp.signInLink()
        # self.driver.get(self.baseURL)
        self.lp.login("", "testingmasked")
        result = self.lp.verifyPassMasked()
        assert result == True

    @pytest.mark.run(order=6)
    def test_verifyLoginPages(self):
        # time.sleep(5)
        self.lp.closeLoginForm()
        self.lp.signInLink()
        # self.driver.get(self.baseURL)
        result = self.lp.verifyLoginPage()
        assert result == True

    @pytest.mark.run(order=8)
    def test_verifyLogin2(self):
        # time.sleep(2)
        self.lp.refreshBrowser()
        self.lp.signInLink()
        # self.driver.refresh()
        # self.driver.get(self.baseURL)
        self.lp.login("sellertesting@mailinator.com", "1234567890")
        result = self.lp.verifyLoginPage2()
        assert result == True

    @pytest.mark.run(order=9)
    def test_verifyLogout(self):
        time.sleep(4)
        result = self.lp.verifyLogout()
        assert result == True
        # time.sleep(10)
        # self.driver.quit()

    # @pytest.mark.run(order=4)
    # def test_verifyLoginBlanksPass(self):
    # self.lp.login("Testing", "")
    # alert_msg2 = self.driver.switch_to.alert
    # msg2 = alert_msg2.text
    # time.sleep(3)
    # print(msg2)
    # alert_msg2.accept()
    # result = self.lp.verifyLoginBlankPass()
    # assert result == True

# @pytest.mark.run(order=2)
# def test_invalidLogin(self):
# self.driver.get(self.baseURL)
# self.lp.login("test@email.com", "abcabcvfdh")
# result = self.lp.verifyLoginFailed()
# assert result == True

# @pytest.mark.run(order=3)
# def test_invalidLoginBlank(self):
# self.lp.login("", "")
# alert_msg = self.driver.switch_to.alert
# msg = alert_msg.text
# time.sleep(2)
# print(msg)
# alert_msg.accept()
# result = self.lp.verifyLoginFailedBlank()
# assert result == True
