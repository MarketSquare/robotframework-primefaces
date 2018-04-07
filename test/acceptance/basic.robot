*** Settings ***
Library    SeleniumLibrary
Library    PrimeFacesLibrary

TestTeardown    Close All Browsers

*** Test Cases ***
Test Implicit Wait Using PF Showcase - Ajax Framework - Basic
    Open Browser  https://www.primefaces.org/showcase/ui/ajax/basic.xhtml
    Input Text  j_idt116:name  RF Tester
    Click Element  j_idt116:j_idt119
    ${DisplayText}=    Get Text  j_idt116:display
    Should Be Equal  ${DisplayText}  RF Tester

Test Implicit Wait Using PF Showcase - Ajax Framework - Partial Process
    Open Browser  https://www.primefaces.org/showcase/ui/ajax/process.xhtml
    Input Text  j_idt116:firstname  Robot
    Input Text  j_idt116:surname  Framework
    Click Element  j_idt116:btnAll
    ${AlertText}=    Get Text  //*[@id='j_idt116:msgs']//ul/li[1]
    Should Be Equal  ${AlertText}    Welcome Robot Framework

Test Implicit Wait Using PF Showcase - Ajax Framework - Status
    Open Browser  https://www.primefaces.org/showcase/ui/ajax/status.xhtml
    ${InitialText}=  Get Text  j_idt116
    Should Be Equal  ${InitialText}  Status: StandBy
    Click Element  j_idt123:j_idt124
    ${PostClickText}=  Get Text  j_idt116
    Should Be Equal  ${PostClickText}  Status: Completed
    