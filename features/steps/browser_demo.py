from behave import then, when, given

from browserdriver import BrowserDriver


@given('I have a firefox driver')
def step_impl(context):
    context.driver = BrowserDriver.get("firefox")


@given('I have a chrome driver')
def step_impl(context):
    context.driver = BrowserDriver.get("chrome")


@when('I navigate to test.io')
def step_impl(context):
    context.driver.get("https://test.io")
    print(context.driver.title)


@then('The page is displayed')
def step_impl(context):
    assert context.driver.title == "QA Testing as a Service | test IO"
