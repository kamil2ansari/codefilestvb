import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # if browser == 'firefox':
    #     baseURL = "http://dev.thevintagebardev.com/"
    #     driver = webdriver.Firefox(executable_path=r'C:\Users\kamil\projects\letskodeit\drivers\geckodriver'
    #                                                r'.exe')
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     driver.implicitly_wait(3)
    #     print("Running tests on FF")
    #
    # else:
    #     baseURL = "http://dev.thevintagebardev.com/"
    #     driver = webdriver.Chrome()
    #     driver.get(baseURL)
    #     print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    # driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")