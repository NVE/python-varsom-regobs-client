# varsom_regobs_client.GeoCodeApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geo_code_location_info**](GeoCodeApi.md#geo_code_location_info) | **GET** /GeoCode/LocationInfo | 

# **geo_code_location_info**
> GeoLocationInfo geo_code_location_info(latitude, longitude, geo_hazard_id)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.GeoCodeApi()
latitude = 1.2 # float | 
longitude = 1.2 # float | 
geo_hazard_id = 56 # int | 

try:
    api_response = api_instance.geo_code_location_info(latitude, longitude, geo_hazard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoCodeApi->geo_code_location_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**|  | 
 **longitude** | **float**|  | 
 **geo_hazard_id** | **int**|  | 

### Return type

[**GeoLocationInfo**](GeoLocationInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

