# AvalancheActivityObsDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avalanche_activity_obs_id** | **int** | Unik id på denne tabellen da flere er mulig pr RegID. | 
**aspect** | **int** | Hvilken side av fjellene har skredene gått? Gis i grader slik gitt på kompass. 0 er nord og 90 er øst osv. | 
**heigth_start_zone** | **int** | Meter over havet på løsneområdet. | 
**dt_avalanche_time** | **datetime** | Når gikk skredene? Her bruker vi feltet som en ca. tid og brukerene oppfordres til å anta best mulig. | 
**destructive_size_tid** | **int** | Hvor store er skredene?. The DestructiveSizeKD unique identifier | [optional] 
**estimated_num_tid** | **int** | Hvor mange skred er gått? The EstimatedNumKD unique identifier | [optional] 
**avalanche_tid** | **int** | Typen skred som er gått. The AvalancheKD unique identifier | [optional] 
**avalanche_trigger_tid** | **int** | Hva utløste skredet? Det er ofte beskrevet som det svake laget i snødekket. The AvalancheTriggerKD unique identifier | [optional] 
**terrain_start_zone_tid** | **int** | Hva slags terrengtype var det i løsneområdet. The TerrainStartZoneKD unique identifier | [optional] 
**snow_line** | **int** | Hvor går snøgrensa i området? | [optional] 
**usage_flag_tid** | **int** | Bruksflagg er ikke implementert enda. Hensikten er å kunne flagge en observasjon som godkjent, underkjent, overført historisk database mm. | [optional] 
**comment** | **str** | Kommentarfelt for å skrive utfyllende tekst om observasjonen. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

