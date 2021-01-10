# Created by username at 12/20/20
Feature: Test Scenarios for Latest On Sale slider functionality
  # "Latest Products on Sale" text is show
  #  Every product has Sale icon, image, product category, name, price, and star-rating
  #  User can click on heart icon to add to wishlist
  #  User can open product from Sale and add it to cart
  #  User can open product from Sale and see product price and description
  #  User can open and close Quick View by clicking on closing X
  #  User can click Quick View and add product to cart
  #  User can click Quick View and click through product images

  Scenario:   - Latest Products on Sale" text is shown
              - Every product has Sale icon, image, product category, name, price, and star-rating
              - User can click on heart icon to add to wishlist
              - User can open product from Sale and add it to cart
              - User can open product from Sale and see product price and description
              - User can open and close Quick View by clicking on closing X
              - User can click Quick View and add product to cart
              - User can click Quick View and click through product images

    Given Open Gettop Home page
#    Then Verify Sale Latest products on sale text is shown
#    And Every product has Sale icon, image, product category, name, price, and star-rating
#    When Every product has Heart Icon and Add to wishlist Pop-up text
#    When User click on heart icon to add to wishlist, verify Pop-up message Product added! and correct item is added to Wishlist
#    And User can open product from Sale and see product price and description
#    When User can open every product from Sale, add it to cart, verify items in cart counter become equal 1, verify sale item was added to the cart and remove product from cart
    When User can open Quick View by clicking Quick View pop up button and close by clicking X
    When User can click Quick View, add product to cart and verify adding exact item on cart counter and Cart Page
    Then User can click Quick View and click through product images

