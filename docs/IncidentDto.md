# IncidentDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_hazard_tid** | **int** | Sett naturfare. Tabellen brukes av alle naturfarer (snø, jord, vann, is). | [optional] 
**activity_influenced_tid** | **int** | Hva ble påvirket av hendelsen. Valgene er gitt i ActivityInfluencedKD. The ActivityInfluencedKD unique identifier | [optional] 
**damage_extent_tid** | **int** | Skadeomfang. Hva var konsekvensen av hendelsen. Valgene gitt i DamageExtentKD. The DamageExtentKD unique identifier | [optional] 
**forecast_accurate_tid** | **int** | Var det et varsel utstedt og stemte det? The ForecastAccurateKD unique identifier | [optional] 
**dt_end_time** | **datetime** | Om hendelsen strakte seg ut i tid, når sluttet den å gjelde? Feks, når åpnet veien igjen etter raset? | [optional] 
**incident_header** | **str** | Hendelsen beskrives med overskrift .. | [optional] 
**incident_ingress** | **str** | .. med ingress eller sammendrag .. | [optional] 
**incident_text** | **str** | .. og teksten eller artikkelen. | [optional] 
**sensitive_text** | **str** | Vi har lagt opp til et felt for internkommentar. Denne kolonnen vises ikke på tjenestelaget og i view. | [optional] 
**usage_flag_tid** | **int** | Bruksflagg er ikke implementert enda. Hensikten er å kunne flagge en observasjon som godkjent, underkjent, overført historisk database mm. The UsageFlagKD unique identifier | [optional] 
**comment** | **str** | Comment. | [optional] 
**incident_ur_ls** | [**list[IncidentUrlsDto]**](IncidentUrlsDto.md) | Provide description for IncidentURLs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

