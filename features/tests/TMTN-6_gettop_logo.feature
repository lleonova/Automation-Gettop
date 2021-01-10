# Created by username at 12/15/20
Feature: Test Scenarios for Gettop redirecting functionality
  # GetTop logo is clickable and takes to https://gettop.us/

 Scenario: Gettop logo is clickable and redirects to the Homepage https://gettop.us/

    Given Open Gettop Shopping Cart page
    When Click on Logo Icon
    Then Verify Home Page is opened

    Given Open Gettop Home page
    Then Verify clicking Logo Icon takes user to Home Page from every Product page

    Given Open Gettop Home page
    Then Verify clicking Logo Icon takes user to Home Page from every Category page

