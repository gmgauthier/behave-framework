from browserdriver import BrowserDriver


def test_firefox_browser(headless):
    bd = BrowserDriver().get("firefox", headless=headless)
    bd.get('https://test.io')
    print(bd.current_url, bd.title)
    assert "QA Testing as a Service | test IO" == bd.title
    bd.quit()


def test_chrome_browser(headless):
    bd = BrowserDriver().get("chrome", headless=headless)
    bd.get('https://test.io')
    print(bd.current_url, bd.title)
    assert "QA Testing as a Service | test IO" == bd.title
    bd.quit()


def test_edge_browser(headless):
    bd = BrowserDriver().get("edge", headless=headless)
    bd.get('https://test.io')
    print(bd.current_url, bd.title)
    assert "QA Testing as a Service | test IO" == bd.title
    bd.quit()
