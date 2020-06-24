# varsom_regobs_client.TripApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trip_post**](TripApi.md#trip_post) | **POST** /Trip | 
[**trip_put**](TripApi.md#trip_put) | **PUT** /Trip | 

# **trip_post**
> object trip_post(body)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.TripApi()
body = varsom_regobs_client.CreateTripDto() # CreateTripDto | 

try:
    api_response = api_instance.trip_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripApi->trip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTripDto**](CreateTripDto.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trip_put**
> trip_put(body)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.TripApi()
body = varsom_regobs_client.FinishTripDto() # FinishTripDto | 

try:
    api_instance.trip_put(body)
except ApiException as e:
    print("Exception when calling TripApi->trip_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FinishTripDto**](FinishTripDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

