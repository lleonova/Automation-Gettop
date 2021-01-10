# Created by username at 1/3/21
Feature: Test Scenarios for Browse Our Categories slider functionality
  # "Browse Our Categories" text is shown
  # 4 correct categories are shown
  # Upon clicking on each category, correct page opens

  Scenario: - "Browse Our Categories" text is shown
            - 4 correct categories are shown
            - Upon clicking on each category, correct page opens

    Given Open Gettop Home page
    Then Verify Browse Browse our Categories text is shown

    Given Open Gettop Home page
    When Confirm there are 4 categories under Browse Our Categories

    Given Open Gettop Home page
    Then The categories are: Accessories, iPad, iPhone, MacBook

    Given Open Gettop Home page
    Then Verify User can select trough categories and correct page opens