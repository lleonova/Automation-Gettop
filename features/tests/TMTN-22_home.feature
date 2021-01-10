# Created by username at 12/15/20
Feature: Test Scenarios for Gettop Homepage redirection functionality

  "Home" link takes user to the Home Page

  Scenario: Home link takes user to Home Page https://gettop.us/
    Given Open Gettop Home page
    Then Verify Home link takes user to Home Page from every Product Category page

    Given Open Gettop Home page
    Then Verify Home link takes user to Home Page from every Product page