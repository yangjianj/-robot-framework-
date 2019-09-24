*** Settings ***
Library            Collections
Resource           PageHandler.robot
Resource           ResourcesSyn.robot

*** Variable ***
${HOST}        127.0.0.1


*** Keywords ***
Ui Suite Setup
    Run Only Once    Init Resource
    log  ${SLAVE_LIST}
    Wait Until Keyword Succeeds  2min  5s    Acquire Slave  ${SLAVE_LIST}
    log    ${suite_salves}
    

Ui Suite Teardown
    Release Slave

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