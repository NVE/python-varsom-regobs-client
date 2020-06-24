# varsom_regobs_client.AccountApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_create_account**](AccountApi.md#account_create_account) | **POST** /Account/Create | 
[**account_get_my_page_data**](AccountApi.md#account_get_my_page_data) | **GET** /Account/Mypage | 
[**account_get_observer**](AccountApi.md#account_get_observer) | **GET** /Account/GetObserver | 
[**account_get_observer_groups**](AccountApi.md#account_get_observer_groups) | **GET** /Account/Groups/{guid} | 
[**account_login**](AccountApi.md#account_login) | **GET** /Account/Login | 

# **account_create_account**
> object account_create_account(body)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.AccountApi()
body = varsom_regobs_client.CreateAccountRequest() # CreateAccountRequest | 

try:
    api_response = api_instance.account_create_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAccountRequest**](CreateAccountRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_my_page_data**
> MyPageData account_get_my_page_data(lang_key=lang_key)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.AccountApi()
lang_key = 56 # int |  (optional)

try:
    api_response = api_instance.account_get_my_page_data(lang_key=lang_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_my_page_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang_key** | **int**|  | [optional] 

### Return type

[**MyPageData**](MyPageData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_observer**
> ObserverResponseDto account_get_observer()



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.AccountApi()

try:
    api_response = api_instance.account_get_observer()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_observer: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ObserverResponseDto**](ObserverResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_observer_groups**
> list[ObserverGroupDto] account_get_observer_groups(guid)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.AccountApi()
guid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.account_get_observer_groups(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_observer_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 

### Return type

[**list[ObserverGroupDto]**](ObserverGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_login**
> ObserverResponseDto account_login()



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.AccountApi()

try:
    api_response = api_instance.account_login()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_login: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ObserverResponseDto**](ObserverResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

