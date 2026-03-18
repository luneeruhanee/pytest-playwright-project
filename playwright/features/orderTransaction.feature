Feature: Order Transaction
  Test relate to Order Transactions

  Scenario Outline: Verify order success message show in detail page
    Given place the item with <username> and <password>
    And the user is on landing page
    When I login with portal with <username> and <password>
    And navigate to order page
    And select the orderID
    Then order message is successful display
    Examples:
      | username           | password       |
      | tohlee89@gmail.com | Lunee@07081995 |
