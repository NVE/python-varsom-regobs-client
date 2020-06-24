# PictureRequestDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photographer** | **str** | Navn på fotograf. | [optional] 
**copyright** | **str** | Rettigheter til bilde. | [optional] 
**aspect** | **int** | Hvilken himmelretning peker bilde. Gis i grader slik gitt på kompass. 0 er nord og 90 er øst osv. | [optional] 
**geo_hazard_tid** | **int** | Sett naturfare. Tabellen brukes av alle naturfarer (snø, jord, vann, is). The GeoHazardKD unique identifier | [optional] 
**usage_flag_tid** | **int** | Bruksflagg er ikke implementert enda. Hensikten er å kunne flagge en observasjon som godkjent, underkjent, overført historisk database mm. The UsageFlagKD unique identifier | [optional] 
**registration_tid** | **int** | Hva er bildet av. Dette feltet relaterer bildet til en observasjonstype. Feks værobservasjon, faretegn, osv. The RegistrationKD unique identifier | [optional] 
**picture_comment** | **str** | Kommentarfelt for bildet. F.eks for å beskrive det. | [optional] 
**picture_image_base64** | **str** | Billed objektet. | [optional] 
**attachment_upload_id** | **str** | If attachment is uploaded before sending registration, set AttachmentUploadId | [optional] 
**is_main_attachment** | **bool** | Om bildet skal vises først i registreringen, eller ikke | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

