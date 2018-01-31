*** Settings ***
Library           Selenium2Library

*** Test Cases ***
Login
    open browser    http://10.75.44.222:3000/#/login    chrome
    maximize browser window
    set selenium timeout    30
    wait until page contains    登录
    input text    //*[@id="username"]    root
    input text    //*[@id="password"]    Cisco123!
    click button    xpath=/html/body/sdn/login/body/div[2]/div[2]/div[2]/button
    title should be    浙江农信广域网流量调度系统
    sleep    5
    go to    http://10.75.44.222:3000/#/index/deviceManagement
    wait until page contains    设备管理

new
    sleep    5
    wait until page contains    新建
    sleep    3
    # 分行设备描述
    click button    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[1]/div[2]/button
    wait until page does not contain    Loading
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[2]/div[1]/div/select    9
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[2]/div[2]/div/select    1
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[2]/div[3]/div/input    700
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[6]/div[1]/button
    # 路由器A
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[3]/div[1]/div/input    RouterA
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[3]/div[2]/div/select    1
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[3]/div[3]/div/input    100
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[3]/div[4]/div/input    12.12.12.120
    Comment    unselect checkbox    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[3]/div[5]/div/div/div/input
    Comment    clear element text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[3]/div[5]/div/input
    Comment    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[3]/div[5]/div/input    12.12.12.20
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[6]/div[2]/button
    # 路由器B
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[4]/div[1]/div/input    RouterB
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[4]/div[2]/div/select    1
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[4]/div[3]/div/input    100
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[4]/div[4]/div/input    13.13.13.130
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[6]/div[2]/button
    # 路由器C
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[5]/div[1]/div/input    RouterC
    select from list by index    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[5]/div[2]/div/select    1
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[5]/div[3]/div/input    100
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[5]/div[4]/div/input    15.15.15.150
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[6]/div[2]/button
    # 验证
    sleep    3
    wait until page contains    椒江
    page should contain    700

edit
    sleep    6
    wait until page contains    设备管理
    sleep    3
    click link    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[2]/branch-basic-info-table/div[2]/table/tbody/tr[2]/td[2]/a
    wait until page does not contain    Loading
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[2]/div[4]/div/textarea    robot description
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[6]/div[1]/button
    # 修改路由器A
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[3]/div[1]/div/input    RouterA1
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[6]/div[2]/button
    # 修改路由器B
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[4]/div[1]/div/input    RouterB2
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[6]/div[2]/button
    # 修改路由器C
    input text    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[5]/div[1]/div/input    RouterC3
    click button    xpath=/html/body/sdn/www-dialog/div/div/div[2]/branchbank-create/div[6]/div[2]/button
    # 验证
    sleep    5
    wait until page contains    robot description
    click link    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[2]/branch-basic-info-table/div[2]/table/tbody/tr[2]/td[10]/a
    element should contain    xpath=/html/body/sdn/www-dialog/div/div/div[2]/head-status-detail/table/tbody/tr[1]    RouterA1
    element should contain    xpath=/html/body/sdn/www-dialog/div/div/div[2]/head-status-detail/table/tbody/tr[2]    RouterB2
    element should contain    xpath=/html/body/sdn/www-dialog/div/div/div[2]/head-status-detail/table/tbody/tr[3]    RouterC3
    # 启动与停止三个探针
    click link    xpath=/html/body/sdn/www-dialog/div/div/div[1]/a
    sleep    5

start
    sleep    3
    select check box    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[2]/branch-basic-info-table/div[2]/table/tbody/tr[2]/td[1]/div/input
    click button    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[1]/div[3]/button
    # 验证
    # 刷新网页
    # reload page

stop
    sleep    8
    select check box    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[2]/branch-basic-info-table/div[2]/table/tbody/tr[2]/td[1]/div/input
    click button    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[1]/div[4]/button
    # 验证

delete
    sleep    7
    wait until page contains    椒江
    select check box    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[2]/branch-basic-info-table/div[2]/table/tbody/tr[2]/td[1]/div/input
    click button    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[1]/div[5]/button
    click button    xpath=/html/body/sdn/alert-content/div/div/div[3]/div[1]/button
    # 验证
    reload page
    wait until page contains    新建
    sleep    5
    wait until page does not contain    椒江

search
    reload page
    sleep    5
    wait until page contains    新建
    input text    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[2]/branch-basic-info-table/div[1]/div/div[1]/div/input    2222222222222222
    wait until page does not contain    查看详情
    clear element text    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[2]/branch-basic-info-table/div[1]/div/div[1]/div/input
    input text    //*[@id="branchbankPart"]/div/branch-part/div[2]/div[2]/branch-basic-info-table/div[1]/div/div[1]/div/input    富阳
    wait until page contains    富阳

close
    close all browsers
