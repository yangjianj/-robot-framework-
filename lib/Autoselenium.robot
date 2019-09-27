*** Settings ***
Documentation    对selenium库的封装，插入元素定位解析
Library            Compute.py
Library            Collections
Resource           Pagehandler.robot
Resource           Resourcessyn.robot

*** Variable ***
${HOST}        127.0.0.1


*** Keywords ***
[Documentation]    对selenium库的封装，插入元素定位解析
Ui Suite Setup
    Run Only Once    Init Resource
    log  ${DEVICE_LIST}
    ${interval}=    return_randint  3  10
    Wait Until Keyword Succeeds  2min  ${interval}s    Acquire Device
    log    ${suite_devices}
