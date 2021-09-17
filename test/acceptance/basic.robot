*** Settings ***
Library    SeleniumLibrary
Library    PrimeFacesLibrary

Test Teardown    Close All Browsers

*** Test Cases ***
Test Implicit Wait Using PF Showcase - Ajax Framework - Basic
    Open Browser  https://www.primefaces.org/showcase/ui/ajax/basic.xhtml    chrome
    Input Text  j_idt303:name  RF Tester
    Click Element  j_idt303:j_idt307
    ${DisplayText}=    Get Text  j_idt303:display
    Should Be Equal  ${DisplayText}  RF Tester

Test Implicit Wait Using PF Showcase - Ajax Framework - Partial Process
    Open Browser  https://www.primefaces.org/showcase/ui/ajax/process.xhtml    chrome
    Input Text  j_idt303:firstname  Robot
    Input Text  j_idt303:surname  Framework
    Click Element  j_idt303:btnAll
    ${AlertText}=    Get Text  //*[@id='j_idt303:msgs']//ul/li[1]
    Should Be Equal  ${AlertText}    Welcome Robot Framework

Test Implicit Wait Using PF Showcase - Ajax Framework - Status
    Open Browser  https://www.primefaces.org/showcase/ui/ajax/status.xhtml    chrome
    ${InitialText}=  Get Text  j_idt304_default
    Should Be Equal  ${InitialText}  Status: StandBy
    Click Element  j_idt311:j_idt312
    ${PostClickText}=  Get Text  j_idt304_complete
    Should Be Equal  ${PostClickText}  Status: Completed
