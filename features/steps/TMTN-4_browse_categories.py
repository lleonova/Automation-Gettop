from behave import when, then


@then('Verify Browse {text} text is shown')
def verify_browse_text(context, text: str):
    context.app.browse_our_categories.verify_browse_text(text)

@when('Confirm there are {number} categories under Browse Our Categories')
def verify_number_of_categories(context, number: str):
    context.app.browse_our_categories.verify_number_of_categories(number)

@then('The categories are: {array}')
def verify_category_names_under_browse(context, array):
    new_array = array.split(',')
    context.app.browse_our_categories.verify_category_names(new_array)

@then('Verify User can select trough categories and correct page opens')
def verify_correct_category(context):
    context.app.browse_our_categories.verify_correct_category()