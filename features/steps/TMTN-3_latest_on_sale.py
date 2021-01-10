from behave import when, then


@then('Verify Sale {text} text is shown')
def verify_sale_text(context, text):
    context.app.latest_sale.verify_sale_text(text)


@then('Every product has Sale icon, image, product category, name, price, and star-rating')
def verify_product_attributes(context):
    context.app.latest_sale.verify_sale_products_attributes()


@when('Every product has Heart Icon and {text} Pop-up text')
def verify_add_to_wishlist_pop_up(context, text):
    context.app.latest_sale.verify_add_to_wishlist_pop_up(text)


@when('User click on heart icon to add to wishlist, verify Pop-up message {text} and correct item is added to Wishlist')
def verify_adding_to_wishlist(context, text: str):
    context.app.latest_sale.verify_adding_to_wishlist(text)


@when('User can open product from Sale and see product price and description')
def sale_product_click(context):
    context.app.latest_sale.sale_product_click()


@when('User can open every product from Sale, add it to cart, verify items in cart counter become equal 1, verify sale item was added to the cart and remove product from cart')
def add_sale_item_to_cart(context):
    context.app.latest_sale.add_sale_item_to_cart()


@when('User can open Quick View by clicking Quick View pop up button and close by clicking X')
def open_qv_window(context):
    context.app.quick_view.open_and_closing_window()


@when('User can click Quick View, add product to cart and verify adding exact item on cart counter and Cart Page')
def add_product_to_cart(context):
    context.app.quick_view.add_product_to_cart()


@then('User can click Quick View and click through product images')
def click_through_images(context):
    context.app.quick_view.click_through_images()
