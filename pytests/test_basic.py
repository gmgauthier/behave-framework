from browserdriver import BrowserDriver
import pytest


def test_firefox_browser(headless):
    bd = BrowserDriver().get("firefox", headless=headless)
    bd.get('https://test.io')
    assert "QA Testing as a Service | test IO" == bd.title
    bd.quit()


def test_chrome_browser(headless):
    bd = BrowserDriver().get("chrome", headless=headless)
    bd.get('https://test.io')
    assert "QA Testing as a Service | test IO" == bd.title
    bd.quit()


def test_safari_browser(headless):
    bd = BrowserDriver().get("safari", headless=False)
    bd.get('https://test.io')
    assert "QA Testing as a Service | test IO" == bd.title
    bd.quit()


@pytest.mark.skip(reason="inconsistent implementations across platforms")
def test_edge_browser(headless):
    bd = BrowserDriver().get("edge", headless=headless)
    bd.get('https://test.io')
    assert "QA Testing as a Service | test IO" == bd.title
    bd.quit()
