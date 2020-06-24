# WaterLevelDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**water_level_described** | **str** | Felt for å beskrive vannstanden. Feks relativt et hus eller mot andre faste ting i terrenget. Verdi i meter [m]. | [optional] 
**water_level_value** | **float** | Om vannstanden kan beskrives settes i tallverdi relativt en flomstøtte, metermål eller som meter over havet. | [optional] 
**water_level_ref_tid** | **int** | Vannstand beskrevet i feltene WaterLevelDescribed eller WaterLevelValue er relativt (referanseverdi) noe. Mulige valg gitt i WaterLevelRefKD. &amp;lt; 200 &#x3D; elver, &amp;gt;&#x3D; 200 innsjøer. The WaterLevelRefKD unique identifier | 
**measured_discharge** | **float** | Faktisk vannføring. Dette er verdi målt av en felthydrolog og ikke en som er estimert ut fra vannstand. Verdi i kubikkmeter [m3]. | [optional] 
**usage_flag_tid** | **int** | Bruksflagg er ikke implementert enda. Hensikten er å kunne flagge en observasjon som godkjent,. The UsageFlagKD unique identifier | [optional] 
**comment** | **str** | Comment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

