# varsom_regobs_client.LocationApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**location_within_radius**](LocationApi.md#location_within_radius) | **GET** /Location/WithinRadius | 

# **location_within_radius**
> list[ObsLocationsResponseDtoV2] location_within_radius(latitude, longitude, radius, geo_hazard_type_ids=geo_hazard_type_ids, observer_guid=observer_guid, return_count=return_count)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.LocationApi()
latitude = 1.2 # float | 
longitude = 1.2 # float | 
radius = 56 # int | 
geo_hazard_type_ids = [56] # list[int] |  (optional)
observer_guid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
return_count = 56 # int |  (optional)

try:
    api_response = api_instance.location_within_radius(latitude, longitude, radius, geo_hazard_type_ids=geo_hazard_type_ids, observer_guid=observer_guid, return_count=return_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->location_within_radius: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**|  | 
 **longitude** | **float**|  | 
 **radius** | **int**|  | 
 **geo_hazard_type_ids** | [**list[int]**](int.md)|  | [optional] 
 **observer_guid** | [**str**](.md)|  | [optional] 
 **return_count** | **int**|  | [optional] 

### Return type

[**list[ObsLocationsResponseDtoV2]**](ObsLocationsResponseDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

