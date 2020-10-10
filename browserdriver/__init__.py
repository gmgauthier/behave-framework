from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class BrowserDriver:
    @staticmethod
    def get(browser=None):
        if browser == "chrome":
            return chrome()
        elif browser == "firefox":
            return firefox()
        elif browser == "edge":
            return edge()
        elif browser == "safari":
            return safari()
        else:
            raise ValueError("'{}' is not a supported browser".format(browser))


def chrome():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--ignore-certificate-errors')
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)


def firefox():
    options = webdriver.FirefoxOptions()
    options.accept_insecure_certs = True
    options.headless = True
    gecko_driver = GeckoDriverManager().install()
    return webdriver.Firefox(executable_path=gecko_driver, firefox_options=options)


def edge():
    return webdriver.Edge(DesiredCapabilities.EDGE)


def safari():
    # Because safari driver is bundled with safari
    return webdriver.Safari()
