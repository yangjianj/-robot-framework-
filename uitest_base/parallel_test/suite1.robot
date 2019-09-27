*** Settings ***
Resource          autotest.robot
Library       Remote    http://${ADDRESS}:${PORT}
Library           ResourcesSyn.py
Suite Setup       Ui Suite Setup
Suite Teardown    Ui Suite Teardown
Test Setup        Ui Test Setup
Test Teardown     Ui Test Teardown

Force Tags    para-test
Test Timeout    150s

***Variable***
@{DATA1}      XYZ   123
@{DEVICE_LIST}    ui    ui
${ADDRESS}    10.134.170.223
${PORT}       8765

***Test Cases***

Test_001
    [Tags]  test-tag1    test-tag2
    [Timeout]    150s
    log    123
    remote_keyword1
    sleep    130s
    log    ${name}

*** Keywords ***
Ui Suite Setup1
    log  111