from behave import then


@then('Verify Home link takes user to Home Page from every Product Category page')
def verify_return_to_home_page_from_every_category_pages(context):
    context.app.top_menu.verify_home_link_from_every_category_page()


@then('Verify Home link takes user to Home Page from every Product page')
def verify_return_to_home_page_from_every_product_pages(context):
    context.app.product_page.verify_home_link_from_every_product_page()
