from behave import then, when


@when("User can open every category and open product's Quick View by clicking Quick View pop up button and close by clicking X")
def open_quick_view(context):
    context.app.top_menu.open_quick_view()

#
# @then('User can click trough multiple product pages by clicking 1, 2 for page number')
# def clicks_through_product_pages_with_1_2(context):
#     context.app.product_page.clicks_through_product_pages_with_1_2()
#
#
# @then('User can click trough multiple product pages by clicking > and <')
# def clicks_through_product_pages_with_arrows(context):
#     context.app.product_page.clicks_through_product_pages_with_arrows()
