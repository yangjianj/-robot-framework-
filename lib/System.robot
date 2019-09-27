*** Settings ***
Resource           Pagehandler.robot

*** Variable ***
${HOST}        127.0.0.1


*** Keywords ***
system1
    [Arguments]    ${name}
    log    ${name}