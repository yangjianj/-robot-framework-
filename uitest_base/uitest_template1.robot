*** Settings ***
Library           SeleniumLibrary
Library           Collections

Suite Setup       Suite Envirment Setup
Suite Teardown    Suite Envirment Teardown
Test Setup        Test Envirment Setup
Test Teardown     Test Envirment Teardown

Force Tags    suit-tag1   suit-tag2
Default Tags    dafault-test1   dafault-test2

Test Timeout    10s


***Variable***
@{DATA1}      W1   Q2   T3


***Test Cases***

Test_001
    [Tags]  test-tag1    test-tag2
    [Timeout]    5s
    [Template]     Template_001
    xxxx    yyyy
    11111    22222

Test_002
    [Tags]  test-tag1    test-tag2
    [Timeout]    5s
    [Template]     Template_001
    :FOR  ${item}  IN    @{ITEMS}
    \    ${item}    1

Test_003
    [Tags]  test-tag1    test-tag2
    [Timeout]    5s
    [Template]     Template_001
    :FOR  ${item}  IN    @{DATA2}
    \    ${item}    1

Test_004
    [Tags]  test-tag1    test-tag2
    [Timeout]    5s
    log    @{DATA2}

*** Keywords ***
Template_001
    [Arguments]    ${username}    ${password}
    Log    ${username} ${password}


Suite Envirment Setup
    #Open Browser    http://baidu.com    Chrome
    set suite variable   @{ITEMS}    x    y    z
    set suite variable   @{DATA2}    ${empty}
    #Remove From List    @{DATA2}    0
    :FOR    ${item}    IN    @{DATA1}
    \    Append To List    ${DATA2}    ${item}_1
    log    ${DATA2}
    Log many    @{DATA2}
    log   in suite setup

Suite Envirment Teardown
    #Close Browser
    log    in suite teardown

Test Envirment Setup
    Log    Test_Envirment_Setup

Test Envirment Teardown
    Log    Test_Envirment_Teardown


