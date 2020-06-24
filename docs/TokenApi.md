# varsom_regobs_client.TokenApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_get**](TokenApi.md#token_get) | **POST** /Token/Get | 

# **token_get**
> GetTokenResponseDto token_get(body)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.TokenApi()
body = varsom_regobs_client.GetTokenRequestDto() # GetTokenRequestDto | 

try:
    api_response = api_instance.token_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetTokenRequestDto**](GetTokenRequestDto.md)|  | 

### Return type

[**GetTokenResponseDto**](GetTokenResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

