from behave import when, then, given


@given('Open Gettop Home page')
def open_home_page(context):
    context.app.page.open_page()


@when('Click on Account icon')
def click_account_icon(context):
    context.app.top_menu.click_account_icon()


@then('Login form is opened')
def verify_login_form(context):
    context.app.login_form.verify_login_form_popup()
