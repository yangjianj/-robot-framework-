*** Settings ***
Library  Collections
Library  pabot.PabotLib
Library  Resourcessyn.py

*** Variable ***
${HOST}        127.0.0.1

*** Keywords ***
Init Resource
    log many    @{DEVICE_LIST}
    Acquire Lock    'DeviceLock'
    ${avialable_devices} =  read_resources
    Set Parallel Value For Key    'avialable_devices'    ${avialable_devices}
    Release Lock    'DeviceLock'

Acquire Device
    Acquire Lock  'DeviceLock'
    ${avialable}=    Get Parallel Value For Key    'avialable_devices'
    log    ${avialable}
    ${result}=    search_device    ${DEVICE_LIST}    ${avialable}
    Run Keyword If  ${result}==${False}    Release Lock    'DeviceLock'
    Run Keyword If  ${result}==${False}    Should Be True  ${1} == ${0}
    Set Suite Variable    ${suite_devices}    ${result}[0]
    Set Parallel Value For Key    'avialable_devices'    ${result}[1]
    Release Lock    'DeviceLock'

Release Device
    #Acquire Lock  'DeviceLock'
    ${avialable}=    Get Parallel Value For Key    'avialable_devices'
    :FOR  ${device}  IN  @{suite_devices}
    \    Append To List    ${avialable}    ${device}
    log    ${avialable}
    Set Parallel Value For Key    'avialable_devices'    ${avialable}
    #Release Lock    'DeviceLock'

