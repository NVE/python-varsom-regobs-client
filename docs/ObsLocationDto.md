# ObsLocationDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude | [optional] 
**longitude** | **float** | Longitude | [optional] 
**obs_location_id** | **int** | ObsLocationID | [optional] 
**location_name** | **str** | Navn på stedet | [optional] 
**utm_zone** | **int** | UTM sone. Merk at kartene i norge ligger mellom UTM32 og 34 | [optional] 
**utm_east** | **int** | Østlig UTM sone uten desimaler | [optional] 
**utm_north** | **int** | Nordlig UTM sone uten desimaler | [optional] 
**utm_source_tid** | **int** | Kildehenvisning på hvordan koordinaten er satt. (GPS i tlf, klikk i kart, osv). Verdier gitt i UTMSourceKD | [optional] 
**forecast_region_tid** | **int** | Anngir varslingsregion stedet tilhører. Varslingsregioner gitt i ForecastRegionKD. The ForecastRegionKD unique identifier | [optional] 
**municipal_no** | **str** | Kommune nr stedet tilhører | [optional] 
**location_description** | **str** | Beskriver stedet. | [optional] 
**comment** | **str** | Kommentarfelt brukt av systemet. Altså vises ikke til brukerne. | [optional] 
**uncertainty** | **int** | Usikkerhet i posisjon i meter. Anslås på web og i app hentes det fra gps. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

