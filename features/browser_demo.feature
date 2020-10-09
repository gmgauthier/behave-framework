Feature: Browser Demo
  Scenario: Load test.io web page
    Given I have a chrome driver
    When I navigate to test.io
    Then The page is displayed
