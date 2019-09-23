*** Settings ***
Resource           PageHandler.robot

*** Variable ***
${HOST}        127.0.0.1


*** Keywords ***
Ui Suite Setup
    [Arguments]    ${name}
    Input Text    ${name}

Ui Suite Teardown
    [Arguments]    ${name}
    Input Text    ${name}

Ui Test Teardown
    [Arguments]    ${name}
    Input Text    ${name}

Ui Test Teardown
    [Arguments]    ${name}
    Input Text    ${name}

Api Suite Setup
    [Arguments]    ${name}
    Input Text    ${name}

Api Suite Teardown
    [Arguments]    ${name}
    Input Text    ${name}

Api Test Teardown
    [Arguments]    ${name}
    Input Text    ${name}

Api Test Teardown
    [Arguments]    ${name}
    Input Text    ${name}