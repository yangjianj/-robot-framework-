*** Settings ***
Library  pabot.PabotLib
Library  ResourcesSyn.py

*** Variable ***
${HOST}        127.0.0.1

*** Keywords ***
init resource
    Acquire Lock    avialable_salves_lock
    ${avialable_salves} = read_resources
    Set Parallel Value For Key    avialable_salves    ${avialable_salves}
    Release Lock    avialable_salves_lock

Acquire Slave
    [Arguments]    ${type}    ${suite_slaves}
    Wait Until Keyword Succeeds  5min  2s  Acquire Lock  slave
    ${avialable}=    Get Parallel Value For Key    ${slaves}
    :FOR  ${item}  IN    ${avialable}
    \    ${match}=  Run Keyword And Return Status    Should Be True    ${item}['type'] == ${type}
    \

Release Slave
    [Arguments]    ${suite_slaves}
