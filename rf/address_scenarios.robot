*** Settings ***
Library  Collections
Library  rf.AddressBook
Suite Setup  Init Fixtures
Suite TearDown  Destroy Fixtures


*** Test Cases ***
Add new address
    ${old_list}=  Get Address List
    ${address}=  New Address  first_name1  middle_name1  last_name1  address1
    Create Address  ${address}
    ${new_list}=  Get Address List
    Append To List  ${old_list}  ${address}
    Address Lists Should Be Equal  ${new_list}  ${old_list}

Delete address
    ${old_list}=  Get Not_empty Address List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${address}=  Get From List  ${old_list}  ${index}
    Delete Address  ${address}
    ${new_list}=  Get Address List
    Remove Values From List  ${old_list}  ${address}
    Address Lists Should Be Equal  ${old_list}  ${new_list}

Modify address
    ${old_list}=  Get Not_empty Address List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${id}=  Get Address Id By Index From The List  ${index}  ${old_list}
    ${address}=  New Address With Id  ${id}  new_first_name  new_middle_name  new_last_name  new_address
    Modify Address  ${address}
    ${new_list}=  Get Address List
    Set List Value  ${old_list}  ${index}  ${address}
    Address Lists Should Be Equal  ${old_list}  ${new_list}
