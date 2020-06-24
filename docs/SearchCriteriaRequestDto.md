# SearchCriteriaRequestDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reg_id** | **int** |  | [optional] 
**lang_key** | **int** |  | [optional] 
**location_id** | **int** |  | [optional] 
**observer_id** | **int** |  | [optional] 
**observer_guid** | **str** |  | [optional] 
**group_id** | **int** |  | [optional] 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 
**from_dt_obs_time** | **datetime** |  | [optional] 
**to_dt_obs_time** | **datetime** |  | [optional] 
**from_dt_change_time** | **datetime** |  | [optional] 
**to_dt_change_time** | **datetime** |  | [optional] 
**number_of_records** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**selected_registration_types** | [**list[RegistrationTypeCriteriaDto]**](RegistrationTypeCriteriaDto.md) |  | [optional] 
**selected_regions** | **list[int]** |  | [optional] 
**selected_geo_hazards** | **list[int]** |  | [optional] 
**observer_competence** | **list[int]** |  | [optional] 
**observer_nick_name** | **str** |  | [optional] 
**countries** | **list[int]** |  | [optional] 
**counties** | **list[str]** |  | [optional] 
**text_search** | **str** |  | [optional] 
**radius** | [**WithinRadiusCriteriaDto**](WithinRadiusCriteriaDto.md) |  | [optional] 
**extent** | [**WithinExtentCriteriaDto**](WithinExtentCriteriaDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

