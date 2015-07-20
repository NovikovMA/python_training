Scenario Outline: Add new address
  Given a address list
  Given a address with <first_name>, <middle_name>, <last_name> and <address>
  When I add address to the list
  Then the new address list is equal to the old list with the added address

  Examples:
  | first_name  | middle_name   | last_name     | address   |
  | first_name1 | middle_name1  | last_name1    | address1  |
  | first_name2 | middle_name2  | last_name2    | address2  |
  | first_name3 | middle_name3  | last_name3    | address3  |


Scenario: Delete a address
  Given a non-empty address list
  Given a random address from the list
  When I delete the address from the list
  Then the new address list is equal to the old list with the deleted address


Scenario Outline: Modify a address
  Given a non-empty address list
  Given a random address from the list for modify
  Given a address with <first_name>, <middle_name>, <last_name> and <address>
  When I modify the address from the list
  Then the new address list is equal to the old list with the modified address

  Examples:
  | first_name  | middle_name   | last_name     | address   |
  | first_name4 | middle_name4  | last_name4    | address4  |
