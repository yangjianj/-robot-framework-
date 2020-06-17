*** Settings ***
Library  Collections
Library  pabot.PabotLib
Library  ResourcesSyn.py


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
    ${dev}=    Run Keyword And Return Status     Variable Should Exist    ${DEVICE_LIST}
    Return From Keyword If	    ${dev}==${False}    'devicelist is null'
    ${result}=    search_device    ${DEVICE_LIST}    ${avialable}
    Run Keyword If  ${result}==${False}    Release Lock    'DeviceLock'
    Run Keyword If  ${result}==${False}    Should Be True  ${1} == ${0}
    Set Suite Variable    ${suite_devices}    ${result}[0]
    Set Parallel Value For Key    'avialable_devices'    ${result}[1]
    Release Lock    'DeviceLock'

Release Device
    #Acquire Lock  'DeviceLock'
    ${avialable}=    Get Parallel Value For Key    'avialable_devices'
    ${dev}=    Run Keyword And Return Status     Variable Should Exist    ${DEVICE_LIST}
    Return From Keyword If	    ${dev}==${False}    'devicelist is null'
    FOR  ${device}  IN  @{suite_devices}
        Append To List    ${avialable}    ${device}
    END
    log    ${avialable}
    Set Parallel Value For Key    'avialable_devices'    ${avialable}
    #Release Lock    'DeviceLock'

