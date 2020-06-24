# CreateRegistrationRequestDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**geo_hazard_tid** | **int** | Sett naturfare. Tabellen brukes av alle naturfarer (snø, jord, vann, is). The GeoHazardKD unique identifier | 
**dt_obs_time** | **datetime** | Tiden da observasjonen ble gjort. | 
**observer_guid** | **str** | Unik ID for observatører (brukere). Denne lages av regObs systemet. | 
**email** | **bool** | Wether or not a confirmation email should be sent to user for this registration. | [optional] 
**obs_location_id** | **int** | Unik ID på ulike observasjonssteder. | [optional] 
**observer_group_id** | **int** | Hvis en bruker registrerer en observasjon på vegne av en gruppe legges det til her. | [optional] 
**comment** | **str** | Kommentarfelt brukt av systemet. | [optional] 
**source_tid** | **int** | Kildereferanse på en registrering. F.eks. har brukeren sette dette selv eller er det referert til fra nyheter. The SourceKD unique identifier | [optional] 
**avalanche_activity_obs** | [**list[AvalancheActivityObsDto]**](AvalancheActivityObsDto.md) | Tabell for skredaktivitet. | [optional] 
**avalanche_activity_obs2** | [**list[AvalancheActivityObs2Dto]**](AvalancheActivityObs2Dto.md) |  | [optional] 
**avalanche_danger_obs** | [**list[AvalancheDangerObsDto]**](AvalancheDangerObsDto.md) |  | [optional] 
**avalanche_eval_problem2** | [**list[AvalancheEvalProblem2Dto]**](AvalancheEvalProblem2Dto.md) | Tabell for skredproblemet. Denne har vært under skredfarevurderingsskjema. | [optional] 
**avalanche_evaluation3** | [**AvalancheEvaluation3Dto**](AvalancheEvaluation3Dto.md) |  | [optional] 
**avalanche_obs** | [**AvalancheObsDto**](AvalancheObsDto.md) |  | [optional] 
**compression_test** | [**list[CompressionTestDto]**](CompressionTestDto.md) |  | [optional] 
**danger_obs** | [**list[DangerObsDto]**](DangerObsDto.md) |  | [optional] 
**general_observation** | [**GeneralObservationEditModel**](GeneralObservationEditModel.md) |  | [optional] 
**ice_cover_obs** | [**IceCoverObsDto**](IceCoverObsDto.md) |  | [optional] 
**ice_thickness** | [**IceThicknessDto**](IceThicknessDto.md) |  | [optional] 
**incident** | [**IncidentDto**](IncidentDto.md) |  | [optional] 
**land_slide_obs** | [**LandSlideObsDto**](LandSlideObsDto.md) |  | [optional] 
**obs_location** | [**ObsLocationDto**](ObsLocationDto.md) |  | [optional] 
**picture** | [**list[PictureRequestDto]**](PictureRequestDto.md) | Tabell for bilder. | [optional] 
**snow_cover_obs** | [**SnowCoverObsDto**](SnowCoverObsDto.md) |  | [optional] 
**snow_profile** | [**PictureRequestDto**](PictureRequestDto.md) |  | [optional] 
**snow_profile2** | [**SnowProfileDto**](SnowProfileDto.md) |  | [optional] 
**snow_surface_observation** | [**SnowSurfaceObservationDto**](SnowSurfaceObservationDto.md) |  | [optional] 
**water_level** | [**WaterLevelDto**](WaterLevelDto.md) |  | [optional] 
**weather_observation** | [**WeatherObservationDto**](WeatherObservationDto.md) |  | [optional] 
**water_level2** | [**WaterLevel2Dto**](WaterLevel2Dto.md) |  | [optional] 
**damage_obs** | [**list[DamageObsDto]**](DamageObsDto.md) |  | [optional] 
**density_profile** | [**DensityProfileDto**](DensityProfileDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

