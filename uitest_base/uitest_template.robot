*** Settings ***
Library           SeleniumLibrary

Suite Setup       Suite Envirment Setup
Suite Teardown    Suite Envirment Teardown
Test Setup        Test Envirment Setup
Test Teardown     Test Envirment Teardown

Test Template     Template_001
#Resource          resource.txt

Force Tags    suit-tag1   suit-tag2
Default Tags    dafault-test1   dafault-test2

Test Timeout    10s

***Test Cases***

Test_001
    [Tags]  test-tag1    test-tag2
    [Timeout]    5s
    xxxx    yyyy
    11111    22222

Test_002
    [Tags]  test-tag1    test-tag2
    [Timeout]    5s
    xxxx    yyyy
    11111    22222


*** Keywords ***
Template_001
    [Arguments]    ${username}    ${password}
    Log    ${username} ${password}
    sleep    2


Suite Envirment Setup
    #Open Browser    http://baidu.com    Chrome
    log   in suite setup

Suite Envirment Teardown
    #Close Browser
    log    in suite teardown

Test Envirment Setup
    Log    Test_Envirment_Setup

Test Envirment Teardown
    Log    Test_Envirment_Teardown


