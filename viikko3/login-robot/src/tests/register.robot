*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kal  qwer12qwer
    Output Should Contain  New user registered

Register With Too Short Username And Valid Password
    Input Credentials  ka  qwer12qwer
    Output Should Contain  Username must be a string of at least 3 characters and contains a-z characters

Register With Valid Username And Too Short Password
    Input Credentials  kal  qwe
    Output Should Contain  The password must be at least 8 characters long and cannot consist of letters only

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kall  kall1234
    Output Should Contain  New user registered

***Keywords***
Input New Command And Create User

    Input New Command
