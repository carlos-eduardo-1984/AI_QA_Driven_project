*** Settings ***
Resource         ../../resources/api_steps.resource
Variables        ../../config/environments/integration.py
Suite Setup      Create API Client
Tags             smoke    api

*** Test Cases ***
Health Endpoint Is Available
    I Request The Health Endpoint
    The Response Status Should Be 200
