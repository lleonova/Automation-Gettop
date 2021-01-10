from behave import when, then


@when('Check every product page')
def open_product_pages(context):
    context.app.product_page.open_product_pages()


@then('Description block is shown')
def verify_description(context):
    context.app.product_page.verify_description()
