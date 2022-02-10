***Settings***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register

***Test Cases***
Register With Valid Username And Password
    Set Username  mikko
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Credentials Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Credentials Register
    Register Should Fail With Message  Username must be a string of at least 3 characters and contains a-z characters 

Register With Valid Username And Too Short Password
    Set Username  moikka
    Set Password  kio
    Set Password Confirmation  kio
    Submit Credentials Register
    Register Should Fail With Message  The password must be at least 8 characters long and cannot consist of letters only

Register With Nonmatching Password And Password Confirmation
    Set Username  moik
    Set Password  kio12345
    Set Password Confirmation  kio12
    Submit Credentials Register
    Register Should Fail With Message  Passwords do not match
Login After Successful Registration
    Set Username  moik
    Set Password  kio12345
    Set Password Confirmation  kio12345
    Submit Credentials Register
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  moik
    Set Password  kio12345
    Submit Credentials Login
    Login Should Succeed
Login After Failed Registration
    Set Username  jk
    Set Password  kio12345
    Set Password Confirmation  kio12345
    Submit Credentials Register
    Register Should Fail With Message  Username must be a string of at least 3 characters and contains a-z characters
    Go To Login Page
    Login Page Should Be Open
    Set Username  jk
    Set Password  kio12345
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password
*** Keywords ***
Go to Register
    Go to Register Page
    Register Page Should Be Open
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
Submit Credentials Register
    Click Button  Register
Submit Credentials Login
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
