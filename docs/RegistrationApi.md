# varsom_regobs_client.RegistrationApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registration_get**](RegistrationApi.md#registration_get) | **GET** /Registration/{regId}/{langKey} | Get registration by regId.
[**registration_get_caaml**](RegistrationApi.md#registration_get_caaml) | **GET** /Registration/Caaml/{regId} | Get a registration in CAAML format
[**registration_insert**](RegistrationApi.md#registration_insert) | **POST** /Registration | Create a new registration.
[**registration_plot_preview_png**](RegistrationApi.md#registration_plot_preview_png) | **POST** /Registration/PlotPreviewPng | Generate a preview figure for a snow profile registration.
[**registration_validate**](RegistrationApi.md#registration_validate) | **POST** /Registration/Validate | Validate registration data.

# **registration_get**
> RegistrationViewModel registration_get(reg_id, lang_key)

Get registration by regId.

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.RegistrationApi()
reg_id = 56 # int | Registration Id
lang_key = 56 # int | 1 = norwegian, 2 = english

try:
    # Get registration by regId.
    api_response = api_instance.registration_get(reg_id, lang_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->registration_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reg_id** | **int**| Registration Id | 
 **lang_key** | **int**| 1 &#x3D; norwegian, 2 &#x3D; english | 

### Return type

[**RegistrationViewModel**](RegistrationViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_get_caaml**
> object registration_get_caaml(reg_id)

Get a registration in CAAML format

CAAML (Canadian Avalanche Association Markup Language) is a standard   for the electronic representation of information pertinent to avalanche   safety operations. See http://caaml.org/.

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.RegistrationApi()
reg_id = 56 # int | Registration Id

try:
    # Get a registration in CAAML format
    api_response = api_instance.registration_get_caaml(reg_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->registration_get_caaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reg_id** | **int**| Registration Id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_insert**
> CreateRegistrationResponseDto registration_insert(body)

Create a new registration.

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.RegistrationApi()
body = varsom_regobs_client.CreateRegistrationRequestDto() # CreateRegistrationRequestDto | Registration data

try:
    # Create a new registration.
    api_response = api_instance.registration_insert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->registration_insert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRegistrationRequestDto**](CreateRegistrationRequestDto.md)| Registration data | 

### Return type

[**CreateRegistrationResponseDto**](CreateRegistrationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_plot_preview_png**
> object registration_plot_preview_png(body, format, height, width, lang_key=lang_key)

Generate a preview figure for a snow profile registration.

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.RegistrationApi()
body = varsom_regobs_client.CreateRegistrationRequestDto() # CreateRegistrationRequestDto | Snow profile registration
format = 56 # int | 
height = 56 # int | 
width = 56 # int | 
lang_key = 56 # int | 1 = norwegian, 2 = english (optional)

try:
    # Generate a preview figure for a snow profile registration.
    api_response = api_instance.registration_plot_preview_png(body, format, height, width, lang_key=lang_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->registration_plot_preview_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRegistrationRequestDto**](CreateRegistrationRequestDto.md)| Snow profile registration | 
 **format** | **int**|  | 
 **height** | **int**|  | 
 **width** | **int**|  | 
 **lang_key** | **int**| 1 &#x3D; norwegian, 2 &#x3D; english | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_validate**
> CreateRegistrationResponseDto registration_validate(body)

Validate registration data.

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.RegistrationApi()
body = varsom_regobs_client.CreateRegistrationRequestDto() # CreateRegistrationRequestDto | Registration data

try:
    # Validate registration data.
    api_response = api_instance.registration_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->registration_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRegistrationRequestDto**](CreateRegistrationRequestDto.md)| Registration data | 

### Return type

[**CreateRegistrationResponseDto**](CreateRegistrationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

