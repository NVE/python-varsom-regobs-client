# LandSlideObsDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_lat** | **float** | Latitude start posisjon | [optional] 
**start_long** | **float** | Long start posisjon | [optional] 
**stop_lat** | **float** | Latitude stopp posisjon | [optional] 
**stop_long** | **float** | Long stopp posisjon | [optional] 
**dt_land_slide_time** | **datetime** | Når gikk skredet? Dette er ikke det samme tidspunktet da skredet ble observert. | 
**dt_land_slide_time_end** | **datetime** | Når stoppet skredet? | [optional] 
**utm_north_start** | **int** | Hvor startet skredet? Nordlig UTM sone uten desimaler. | [optional] 
**utm_east_start** | **int** | Hvor startet skredet? Østlig UTM sone uten desimaler. | [optional] 
**utm_zone_start** | **int** | Hvor startet skredet? UTM sone. Merk at kartene i norge ligger mellom UTM32 og 34. | [optional] 
**utm_north_stop** | **int** | Hvor stoppet skredet? Nordlig UTM sone uten desimaler. | [optional] 
**utm_east_stop** | **int** | Hvor stoppet skredet? Østlig UTM sone uten desimaler. | [optional] 
**utm_zone_stop** | **int** | Hvor stoppet skredet? UTM sone. Merk at kartene i norge ligger mellom UTM32 og 34. | [optional] 
**land_slide_tid** | **int** | Hva slags type skred er det snakk om? Valg gitt i LandSlideKD. The LandSlideKD unique identifier | [optional] 
**land_slide_trigger_tid** | **int** | Hva utløste skredet? The LandSlideTriggerKD unique identifier | [optional] 
**land_slide_size_tid** | **int** | Hvor stort er skredet? The LandSlideSizeKD unique identifier | [optional] 
**usage_flag_tid** | **int** | Bruksflagg er ikke implementert enda. Hensikten er å kunne flagge en observasjon som godkjent, underkjent, overført historisk database mm. The UsageFlagKD unique identifier | [optional] 
**geo_hazard_tid** | **int** | Spesifiser skredtype. vått jordskred?, jordskred eller steinskred? GeoHazardTID &#x3D; 20, 30 og 40 er aktuelle. The GeoHazardKD unique identifier | [optional] 
**activity_influenced_tid** | **int** | Hva ble påvirket av hendelsen. Valgene er gitt i ActivityInfluencedKD. The ActivityInfluencedKD unique identifier | [optional] 
**forecast_accurate_tid** | **int** | Var det et varsel utstedt og stemte det? The ForecastAccurateKD unique identifier | [optional] 
**damage_extent_tid** | **int** | Skadeomfang. Hva var konsekvensen av hendelsen. Valgene gitt i DamageExtentKD. The DamageExtentKD unique identifier | [optional] 
**comment** | **str** | Kommentarfelt for å skrive utfyllende tekst om observasjonen. | [optional] 
**urls** | [**list[UrlViewModel]**](UrlViewModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

