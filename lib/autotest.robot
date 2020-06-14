*** Settings ***
Library            Compute.py
Library            Collections
Resource           PageHandler.robot
Resource           ResourcesSyn.robot

*** Variable ***
${HOST}        127.0.0.1


*** Keywords ***
Ui Suite Setup
    Run Only Once    Init Resource
    log  ${DEVICE_LIST}
    ${interval}=    return_randint  3  10
    Wait Until Keyword Succeeds  2min  ${interval}s    Acquire Device
    log    ${suite_devices}
    

Ui Suite Teardown
    Release Device

Ui Test Setup
    log    1

Ui Test Teardown
    log    1

Api Suite Setup
    log    1

Api Suite Teardown
    log    1

Api Test Setup
    log    1

Api Test Teardown
    log    1