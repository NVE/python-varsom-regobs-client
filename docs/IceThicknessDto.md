# IceThicknessDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snow_depth** | **float** | Mengden tørr snø oppå isen. Verdi i meter [m]. | [optional] 
**slush_snow** | **float** | Mengden sørpe oppå isen. Verdi i meter [m]. | [optional] 
**ice_thickness_sum** | **float** | Total istykkelse. I tabellen IceThicknessLayer kan individuelle islag registreres. Summen av dem skal samsvare med IceThickenssSum. Verdi i meter [m]. | [optional] 
**ice_height_before** | **float** | Isen kan være presset under vannspeilet eller flyte oppå. Her registreres denne høyden før borring. IceHeightBefore &#x3D; 0 betyr at isen er tørr og negative verdier angir overvann. Verdi i meter [m]. | [optional] 
**ice_height_after** | **float** | Isen kan være presset under vannspeilet eller flyte oppå. Her registreres denne høyden etter borring. IPositive verdier angir at vannet står nedi hulet og og negative verdier angir overvann. Verdi i meter [m]. | [optional] 
**usage_flag_tid** | **int** | Bruksflagg er ikke implementert enda. Hensikten er å kunne flagge en observasjon som godkjent, underkjent, overført historisk database mm. The UsageFlagKD unique identifier | [optional] 
**comment** | **str** | Comment | [optional] 
**ice_thickness_layer** | [**list[IceThicknessLayerDto]**](IceThicknessLayerDto.md) | Provide description for IceThicknessLayer | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

