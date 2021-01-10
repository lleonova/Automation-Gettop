# Created by username at 1/7/21
Feature: Test Scenarios for Gettop Wishlist functionality
  # "No products added to the wishlist'" shown if no product were added to the list

  Scenario: "No products added to the wishlist'" shown if no product were added to the list
    Given Open Gettop Wishlist page
    Then Verify 'No products added to the wishlist' pop-up is shown