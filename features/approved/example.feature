@smoke @api
Feature: Service health

  Scenario: Health endpoint is available
    Given the API service is available
    When I request the health endpoint
    Then the response status should be 200
