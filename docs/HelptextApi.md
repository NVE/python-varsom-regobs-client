# varsom_regobs_client.HelptextApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**helptext_get**](HelptextApi.md#helptext_get) | **GET** /HelpText | Get a list of helptext objects.

# **helptext_get**
> list[HelptextDto] helptext_get(lang_key)

Get a list of helptext objects.

Used by the app and regobs.no web for displaying help texts.

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.HelptextApi()
lang_key = 56 # int | Specify 1 for norwegian or 2 for english

try:
    # Get a list of helptext objects.
    api_response = api_instance.helptext_get(lang_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelptextApi->helptext_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang_key** | **int**| Specify 1 for norwegian or 2 for english | 

### Return type

[**list[HelptextDto]**](HelptextDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

