from browserdriver import BrowserDriver


def setup_module(module):
    global bd
    bd = BrowserDriver().get("firefox")


def teardown_module(module):
    bd.quit()


def test_load_browser():
    bd.get('https://test.io')
    assert "QA Testing as a Service | test IO" == bd.title
