# varsom_regobs_client.SearchApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_at_a_glance**](SearchApi.md#search_at_a_glance) | **POST** /Search/AtAGlance | Returns simplified registrations.
[**search_count**](SearchApi.md#search_count) | **POST** /Search/Count | Returns search result count
[**search_search**](SearchApi.md#search_search) | **POST** /Search | Registration search
[**search_search_criteria**](SearchApi.md#search_search_criteria) | **POST** /Search/SearchCriteria | Returns search criteria for the specified hazard type and language.

# **search_at_a_glance**
> list[AtAGlanceViewModel] search_at_a_glance(body)

Returns simplified registrations.

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.SearchApi()
body = varsom_regobs_client.SearchCriteriaRequestDto() # SearchCriteriaRequestDto | Search criteria

try:
    # Returns simplified registrations.
    api_response = api_instance.search_at_a_glance(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_at_a_glance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchCriteriaRequestDto**](SearchCriteriaRequestDto.md)| Search criteria | 

### Return type

[**list[AtAGlanceViewModel]**](AtAGlanceViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_count**
> SearchCountResponseDto search_count(body)

Returns search result count

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.SearchApi()
body = varsom_regobs_client.SearchCriteriaRequestDto() # SearchCriteriaRequestDto | Search criteria

try:
    # Returns search result count
    api_response = api_instance.search_count(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchCriteriaRequestDto**](SearchCriteriaRequestDto.md)| Search criteria | 

### Return type

[**SearchCountResponseDto**](SearchCountResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_search**
> list[RegistrationViewModel] search_search(body)

Registration search

Example critera for returning the 10 newest registrations:  <code>      { \"NumberOfRecords\": 10 }  </code>

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.SearchApi()
body = varsom_regobs_client.SearchCriteriaRequestDto() # SearchCriteriaRequestDto | Search criteria.

try:
    # Registration search
    api_response = api_instance.search_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchCriteriaRequestDto**](SearchCriteriaRequestDto.md)| Search criteria. | 

### Return type

[**list[RegistrationViewModel]**](RegistrationViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_search_criteria**
> SearchSideBarDto search_search_criteria(body)

Returns search criteria for the specified hazard type and language.

### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.SearchApi()
body = varsom_regobs_client.SearchSideBarRequestDto() # SearchSideBarRequestDto | 

try:
    # Returns search criteria for the specified hazard type and language.
    api_response = api_instance.search_search_criteria(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_search_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchSideBarRequestDto**](SearchSideBarRequestDto.md)|  | 

### Return type

[**SearchSideBarDto**](SearchSideBarDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

