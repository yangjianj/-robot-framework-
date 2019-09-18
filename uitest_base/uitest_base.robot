*** Settings ***
Library           SeleniumLibrary
Library           Collections
Resource           PageHandler.robot

Suite Setup       Suite Envirment Setup
Suite Teardown    Suite Envirment Teardown
Test Setup        Test Envirment Setup
Test Teardown     Test Envirment Teardown

#Resource          resource.txt

Force Tags    suit-tag1   suit-tag2
Default Tags    dafault-test1   dafault-test2

Test Timeout    10s


***Variable***
@{DATA1}      XYZ   123

***Test Cases***

Test_001
    [Tags]  test-tag1    test-tag2
    [Timeout]    5s
    log    123
    log    ${name}



*** Keywords ***
Template_001
    [Arguments]    ${username}    ${password}
    Log    ${username}
    Log    ${password}


Suite Envirment Setup
    log  in suite setup

Suite Envirment Teardown
    #Close Browser
    log  in suite teardown

Test Envirment Setup
    Log    Test_Envirment_Setup

Test Envirment Teardown
    Log    Test_Envirment_Teardown


