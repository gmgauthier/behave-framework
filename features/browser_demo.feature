Feature: Browser Demo
  Scenario: Load test.io web page with chrome
    Given I have a chrome driver
    When I navigate to test.io
    Then The page is displayed

  Scenario: Load test.io web page with firefox
    Given I have a firefox driver
    When I navigate to test.io
    Then The page is displayed