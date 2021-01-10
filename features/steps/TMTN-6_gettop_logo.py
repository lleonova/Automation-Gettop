from behave import when, given, then


@given('Open Gettop Shopping Cart page')
def open_ipad_page(context):
    context.app.page.open_page('cart/')


@when('Click on Logo Icon')
def click_logo_icon(context):
    context.app.top_menu.click_logo_icon()


@then('Verify Home Page is opened')
def verify_home_page(context):
    context.app.top_menu.verify_home_page()


@then('Verify clicking Logo Icon takes user to Home Page from every Product page')
def verify_return_to_home_page_from_every_product_pages(context):
    context.app.product_page.verify_return_to_home_page_from_every_product_pages()


@then('Verify clicking Logo Icon takes user to Home Page from every Category page')
def verify_logo_icon_from_every_category_page(context):
    context.app.top_menu.verify_logo_icon_from_every_category_page()
