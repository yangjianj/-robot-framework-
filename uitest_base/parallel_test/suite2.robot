*** Settings ***
Resource          autotest.robot

Suite Setup       Ui Suite Setup
Suite Teardown    Ui Suite Teardown
Test Setup        Ui Test Setup
Test Teardown     Ui Test Teardown


Force Tags    para-test

Test Timeout    30s


***Variable***
@{DATA1}      XYZ   123
@{SLAVE_LIST}    ui    api

***Test Cases***

Test_001
    [Tags]  test-tag1    test-tag2
    [Timeout]    10s
    log    123
    sleep    5s
    log    ${name}
