*** Settings ***
Library  Collections
Library  pabot.PabotLib
Library  ResourcesSyn.py

*** Variable ***
${HOST}        127.0.0.1

*** Keywords ***
Init Resource
    log    ${SLAVE_LIST}
    Acquire Lock    avialable_salves_lock
    ${avialable_salves} =  read_resources
    Set Parallel Value For Key    'avialable_salves'    ${avialable_salves}
    Release Lock    avialable_salves_lock

Acquire Slave
    [Arguments]    ${typelist}
    Acquire Lock  'SlaveLock'
    ${avialable}=    Get Parallel Value For Key    'avialable_salves'
    log    ${avialable}
    ${result}=    search_slave    ${typelist}    ${avialable}
    Run Keyword If  ${result}==${False}    Release Lock    'SlaveLock'
    Run Keyword If  ${result}==${False}    Should Be True  ${1} == ${0}
    Set Suite Variable    ${suite_salves}    ${result}[0]
    Set Parallel Value For Key    'avialable_salves'    ${result}[1]
    Release Lock    'SlaveLock'

Release Slave
    #Acquire Lock  'SlaveLock'
    ${avialable}=    Get Parallel Value For Key    'avialable_salves'
    :FOR  ${slave}  IN  ${suite_salves}
    \    Append To List    ${avialable}    ${slave}
    Set Parallel Value For Key    'avialable_salves'    ${avialable}
    log    ${avialable}
    #Release Lock    'SlaveLock'

