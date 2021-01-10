from behave import when, then


@when('User can add correct item to Wishlist, remove item and see a confirmation Pop-up')
def add_item_to_wishlist(context):
    context.app.product_page.add_correct_item_to_wishlist()


@when('User can add correct item to Wishlist, see social logos, remove item and see a confirmation Pop-up')
def verify_wishlist_has_social_logos(context):
    context.app.product_page.verify_wishlist_has_social_logos()


@when('User add correct item to Wishlist, verify User can click on wishlist item and is taken to correct product page')
def verify_wishlist_correct_link(context):
    context.app.product_page.verify_wishlist_correct_link()