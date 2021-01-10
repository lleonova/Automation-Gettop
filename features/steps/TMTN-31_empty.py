from behave import given, then


@given('Open Gettop Wishlist page')
def open_wishlist_page(context):
    context.app.page.open_page('my-account/wishlist/')


@then("Verify 'No products added to the wishlist' pop-up is shown")
def verify_empty_wishlist_message(context):
    context.app.wish_list.verify_empty_wishlist_message()
