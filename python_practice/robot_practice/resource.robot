*** Settings ***
Documentation    Suite description
Library     Selenium2Library


*** Variables ***
${SERVER}         http://localhost/wp
${BROWSER}        Chrome
${DELAY}          0
${VALID USER}     admin
${VALID PASSWORD}    admin
${LOGIN URL}      ${SERVER}/wp-admin
${NEW URL}      ${SERVER}/wp-admin/post-new.php


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