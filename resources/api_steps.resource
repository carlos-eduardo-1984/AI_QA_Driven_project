*** Settings ***
Resource    common.resource

*** Keywords ***
I Request The Health Endpoint
    ${response}=    GET On Session    service    /health    expected_status=any
    Set Test Variable    ${RESPONSE}    ${response}

The Response Status Should Be ${expected_status}
    Should Be Equal As Integers    ${RESPONSE.status_code}    ${expected_status}
