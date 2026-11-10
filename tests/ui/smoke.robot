*** Settings ***
Resource         ../../resources/common.resource
Variables        ../../config/environments/integration.py
Suite Setup      Open Application
Suite Teardown   Close Application
Tags             smoke    ui

*** Test Cases ***
Application Opens
    Get Url    ==    ${WEB_BASE_URL}/
