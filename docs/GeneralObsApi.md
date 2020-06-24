# varsom_regobs_client.GeneralObsApi

All URIs are relative to *https://api.regobs.no/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_general_obs**](GeneralObsApi.md#delete_general_obs) | **DELETE** /GeneralObs/{regId} | 
[**get_general_obs**](GeneralObsApi.md#get_general_obs) | **GET** /GeneralObs/{regId} | 
[**post_general_obs**](GeneralObsApi.md#post_general_obs) | **POST** /GeneralObs/{regId} | 
[**put_general_obs**](GeneralObsApi.md#put_general_obs) | **PUT** /GeneralObs/{regId} | 

# **delete_general_obs**
> object delete_general_obs(reg_id)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.GeneralObsApi()
reg_id = 56 # int | 

try:
    api_response = api_instance.delete_general_obs(reg_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralObsApi->delete_general_obs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reg_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_general_obs**
> get_general_obs(reg_id)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.GeneralObsApi()
reg_id = 56 # int | 

try:
    api_instance.get_general_obs(reg_id)
except ApiException as e:
    print("Exception when calling GeneralObsApi->get_general_obs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reg_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_general_obs**
> object post_general_obs(body, reg_id)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.GeneralObsApi()
body = varsom_regobs_client.GeneralObservationEditModel() # GeneralObservationEditModel | 
reg_id = 56 # int | 

try:
    api_response = api_instance.post_general_obs(body, reg_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralObsApi->post_general_obs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeneralObservationEditModel**](GeneralObservationEditModel.md)|  | 
 **reg_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_general_obs**
> put_general_obs(body, reg_id)



### Example
```python
from __future__ import print_function
import time
import varsom_regobs_client
from varsom_regobs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_regobs_client.GeneralObsApi()
body = varsom_regobs_client.GeneralObservationEditModel() # GeneralObservationEditModel | 
reg_id = 56 # int | 

try:
    api_instance.put_general_obs(body, reg_id)
except ApiException as e:
    print("Exception when calling GeneralObsApi->put_general_obs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeneralObservationEditModel**](GeneralObservationEditModel.md)|  | 
 **reg_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

