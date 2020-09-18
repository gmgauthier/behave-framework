@given(u'A sentence')
def step_impl(context):
    return True


@when(u'The sentence is inspected')
def step_impl(context):
    return True


@then(u'The word "the" should be found')
def step_impl(context):
    return True