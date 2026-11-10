*** Settings ***
Library    Browser
Library    RequestsLibrary

*** Keywords ***
Open Application
    New Browser    ${BROWSER}    headless=${HEADLESS}
    New Context
    New Page    ${WEB_BASE_URL}

Close Application
    Close Browser

Create API Client
    Create Session    service    ${API_BASE_URL}    verify=${True}    timeout=${API_TIMEOUT}
