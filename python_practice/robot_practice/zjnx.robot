*** Settings ***
Library           Selenium2Library

*** Test Cases ***
Login
    open browser    http://10.75.44.222:3001/#/index    chrome
    sleep    3
    input text    //*[@id="username"]    root
    input text    //*[@id="password"]    Cisco123!
    click button    xpath=/html/body/sdn/login/body/div[2]/div[2]/div[2]/button
    title should be    浙江农信广域网流量调度系统
    sleep    3

new
    sleep    5
    click link    //*[@id="wrapper"]/nav/div[2]/ul[1]/li[3]/a
    sleep    2
    click button    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[1]/div[2]/button
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[1]/div[1]/div/input    robot_test
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[1]/div[2]/div/input    robot_description
    sleep    2
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[1]/div[3]/div[1]/select    1
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[1]/div[3]/div[2]/select    1
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[5]/div/button
    input text    //*[@id="filterCondAddi_1"]/div/div[1]/input    1.1.1.1/24
    input text    //*[@id="filterCondAddi_1"]/div/div[2]/input    2.2.2.2/24
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[2]/div[2]/app-penal/div/div[5]/button[2]
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[3]/div[2]/outin-penal/div[3]/button[2]
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[5]/div[2]/button
    sleep    3
    reload page
    sleep    3
    page should contain    robot_test
    sleep    3

new_arg
    sleep    5
    click link    //*[@id="wrapper"]/nav/div[2]/ul[1]/li[3]/a
    sleep    3
    click button    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[1]/div[2]/button
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[1]/div[1]/div/input    1
    page should contain    格式错误
    sleep    2
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[1]/div[1]/div/input    123
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[1]/div[3]/div[1]/select    1
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[1]/div[3]/div[2]/select    1
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[5]/div/button
    input text    //*[@id="filterCondAddi_1"]/div/div[1]/input    1.1.1.1
    page should contain    省中心IP格式错误
    input text    //*[@id="filterCondAddi_1"]/div/div[2]/input    2.2.2.2
    page should contain    分行IP格式错误
    sleep    3
    input text    //*[@id="filterCondAddi_1"]/div/div[1]/input    3.3.3.3/24
    input text    //*[@id="filterCondAddi_1"]/div/div[2]/input    4.4.4.4/24
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[2]/div[2]/app-penal/div/div[5]/button[2]
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[3]/div[2]/outin-penal/div[1]/div[2]/div/select    1
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[3]/div[2]/outin-penal/div[1]/div[4]/div/select    1
    page should contain    主出口与备份出口相同，请重新选择
    sleep    2
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[3]/div[2]/outin-penal/div[1]/div[4]/div/select    2
    page should not contain    主出口与备份出口相同，请重新选择
    sleep    2
    unselect checkbox    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[3]/div[2]/outin-penal/div[1]/div[6]/div/div[1]/input
    unselect checkbox    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[3]/div[2]/outin-penal/div[1]/div[6]/div/div[2]/input
    unselect checkbox    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[3]/div[2]/outin-penal/div[1]/div[6]/div/div[3]/input
    page should contain    至少选择一个入口路由器
    sleep    2
    select checkbox    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[3]/div[2]/outin-penal/div[1]/div[6]/div/div[3]/input
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/policy-create/div[2]/div[3]/div[2]/outin-penal/div[3]/button[2]
    reload page
    sleep    3

activate
    sleep    5
    click link    //*[@id="wrapper"]/nav/div[2]/ul[1]/li[3]/a
    sleep    3
    select checkbox    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[2]/policy-table/div[2]/table/tbody/tr/td[1]/div/input
    click button    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[1]/div[3]/button
    click button    xpath=/html/body/sdn/alert-content/div/div/div[3]/div[1]/button
    element should contain    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[2]/policy-table/div[2]/table/tbody/tr[1]/td[7]    激活中
    sleep    7
    element should contain    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[2]/policy-table/div[2]/table/tbody/tr[1]/td[7]    运行中
    sleep    3

deactivate
    sleep    3
    select checkbox    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[2]/policy-table/div[2]/table/tbody/tr/td[1]/div/input
    click button    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[1]/div[4]/button
    click button    xpath=/html/body/sdn/alert-content/div/div/div[3]/div[1]/button
    element should contain    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[2]/policy-table/div[2]/table/tbody/tr[1]/td[7]    已退出
    sleep    3

search
    input text    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[2]/policy-table/div[1]/div/div[1]/div/input    robot_test
    sleep    3
    page should contain    robot_test
    sleep    1
    input text    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[2]/policy-table/div[1]/div/div[1]/div/input    2222222222222222
    sleep    3
    page should not contain    robot_test
    sleep    3

delete
    sleep    3
    reload page
    sleep    2
    select checkbox    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[2]/policy-table/div[2]/table/tbody/tr/td[1]/div/input
    click button    //*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[1]/div[5]/button
    click button    xpath=/html/body/sdn/alert-content/div/div/div[3]/div[1]/button
    reload page
    page should not contain    robot_test
    sleep    3

check
    sleep    5
    reload page
    sleep    2
    click link    //*[@id="wrapper"]/nav/div[2]/ul[1]/li[3]/a
    sleep    3
    click link    xpath=//*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[1]/div[2]/div[2]/div[2]/policy-table/div[2]/table/tbody/tr/td[2]/span/a
    element should contain    xpath=//*[@id="page-wrapper"]/div[1]/policymanagementcomponent/div[2]/policy-detail/div/div[2]    演示策略
    sleep    3
    close all browsers
