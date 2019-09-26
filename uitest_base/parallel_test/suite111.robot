*** Settings ***
Resource          autotest.robot

Suite Setup       Ui Suite Setup
Suite Teardown    Ui Suite Teardown
Test Setup        Ui Test Setup
Test Teardown     Ui Test Teardown


Force Tags    para-test

Test Timeout    150s


***Variable***
@{DATA1}      XYZ   123
@{DEVICE_LIST}    ui    ui

***Test Cases***

Test_001
    [Tags]  test-tag1    test-tag2
    [Timeout]    150s
    log    123
    sleep    130s
    log    ${name}
