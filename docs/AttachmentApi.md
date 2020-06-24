# varsom_regobs_client.AttachmentApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachment_post**](AttachmentApi.md#attachment_post) | **POST** /Attachment/Upload | 

# **attachment_post**
> str attachment_post(body)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.AttachmentApi()
body = NULL # object | 

try:
    api_response = api_instance.attachment_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->attachment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

