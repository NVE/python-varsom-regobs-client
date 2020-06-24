# varsom_regobs_client.KdvElementsApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kdv_elements_get_kdvs**](KdvElementsApi.md#kdv_elements_get_kdvs) | **GET** /KdvElements | Returns values and texts for input fields, dropdowns etc.

# **kdv_elements_get_kdvs**
> KdvElementsResponseDto kdv_elements_get_kdvs(langkey=langkey, is_active=is_active, sort_order=sort_order)

Returns values and texts for input fields, dropdowns etc.

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.KdvElementsApi()
langkey = 56 # int | 1 = norwegian, 2 = english (optional)
is_active = true # bool |  (optional)
sort_order = true # bool |  (optional)

try:
    # Returns values and texts for input fields, dropdowns etc.
    api_response = api_instance.kdv_elements_get_kdvs(langkey=langkey, is_active=is_active, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KdvElementsApi->kdv_elements_get_kdvs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **langkey** | **int**| 1 &#x3D; norwegian, 2 &#x3D; english | [optional] 
 **is_active** | **bool**|  | [optional] 
 **sort_order** | **bool**|  | [optional] 

### Return type

[**KdvElementsResponseDto**](KdvElementsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

