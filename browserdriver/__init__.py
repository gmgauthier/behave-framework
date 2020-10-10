from selenium import webdriver

from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class BrowserDriver:
    @staticmethod
    def get(browser=None, headless=True):
        if browser == "chrome":
            return chrome(headless)
        elif browser == "firefox":
            return firefox(headless)
        elif browser == "edge":
            return edge(headless)
        elif browser == "safari":
            return safari()
        else:
            raise ValueError("'{}' is not a supported browser".format(browser))


def chrome(headless=True):
    options = webdriver.ChromeOptions()
    options.headless = headless
    options.add_argument('--ignore-certificate-errors')
    return webdriver.Chrome(
        ChromeDriverManager().install(),
        options=options)


def firefox(headless=True):
    options = webdriver.FirefoxOptions()
    options.accept_insecure_certs = True
    options.headless = headless
    gecko_driver = GeckoDriverManager().install()
    return webdriver.Firefox(
        executable_path=gecko_driver,
        options=options)


def edge(headless=True):
    options = EdgeOptions()
    options.use_chromium = True
    options.headless = headless
    edge_driver = EdgeChromiumDriverManager().install()
    driver = Edge(edge_driver, options=options)
    return driver


def safari():
    # Because safari driver is bundled with safari
    return webdriver.Safari()
