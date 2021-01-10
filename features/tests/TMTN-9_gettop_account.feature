# Created by username at 12/16/20
Feature: Test Scenarios for User Account functionality
  # Clicking on Account icon opens Login form

Scenario: Clicking on Account icon opens Login form
    Given Open Gettop Home page
    When Click on Account icon
    Then Login form is opened