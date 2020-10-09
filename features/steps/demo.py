from behave import then, when, given


@given('A sentence')
def step_impl(context):
    return True


@when('The sentence is inspected')
def step_impl(context):
    return True


@then('The word "the" should be found')
def step_impl(context):
    return True
