*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary

*** Variables ***
${login_url}    http://localhost/wp/wp-login.php
${BROWSER}      Chrome

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    admin
    Input Password    admin
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    标题 ‹ 登录

Input Username
    [Arguments]    ${username}
    Input Text    //*[@id="user_login"]    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    //*[@id="user_pass"]    ${password}

Submit Credentials
    Click Button    //*[@id="wp-submit"]

Welcome Page Should Be Open
    Title Should Be    仪表盘 ‹ 标题 — WordPress