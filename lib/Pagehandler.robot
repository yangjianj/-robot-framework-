*** Settings ***
Library           Seleniumlibrary
Library           Elementidentify.py

*** Variable ***
${HOST}        127.0.0.1


*** Keywords ***
OPEN LOGIN PAGE
    [Arguments]    ${name}
    Input Text    ${name}