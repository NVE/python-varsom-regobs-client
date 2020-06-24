# DangerObsDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**danger_obs_id** | **int** | Settes av systemet. Teller fra 0 og opp pr RegID | [optional] 
**geo_hazard_tid** | **int** | Sett naturfare. Tabellen brukes av alle naturfarer (snø, jord, vann, is). The GeoHazardKD unique identifier | [optional] 
**danger_sign_tid** | **int** | Faretegn er listet i tabellen DangerSignKD. The DangerSignKD unique identifier | 
**usage_flag_tid** | **int** | Bruksflagg er ikke implementert enda. Hensikten er å kunne flagge en observasjon som godkjent, underkjent, overført historisk database mm. The UsageFlagKD unique identifier | [optional] 
**comment** | **str** | Kommentarfelt for å skrive utfyllende tekst om faretegnet. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

