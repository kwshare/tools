*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    admin
    Input Password    admin
    Submit Credentials
    Welcome Page Should Be Open

Publish post
    Navigate To Post
    Enter Title
    Change To Pure Text
    Enter Content
    Publish Post
    Check Publish
    [Teardown]    Close Browser

*** Keywords ***
Navigate To Post
    Click Link    ${NEW_URL}
    Title Should Be     撰写新文章 ‹ 标题 — WordPress
Enter Title
    Input Text    //*[@id="title"]    robot文章标题
Change To Pure Text
    Click Button    //*[@id="content-html"]
Enter Content
    Input Text    //*[@id="content"]   robot文章内容
Publish Post
    Sleep   5s
    Click Button    //*[@id="publish"]
Check Publish
    Title Should Be     编辑文章 ‹ 标题 — WordPress