# AvalancheEvalProblem2Dto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avalanche_eval_problem2_id** | **int** | Unik id på denne tabellen da flere er mulig pr RegID. | [optional] 
**avalanche_ext_tid** | **int** | Skredtype. I appen er dette 1. felt under skredproblem. The AvalancheExtKD unique identifier | [optional] 
**aval_probability_tid** | **int** | Sannsynlighet for skred. The AvalProbabilityKD unique identifier | [optional] 
**aval_trigger_simple_tid** | **int** | The AvalTriggerSimpleKD unique identifier | [optional] 
**destructive_size_tid** | **int** | Sannsynlig tilleggsbelastning for å utløse skred. The DestructiveSizeKD unique identifier | [optional] 
**aval_cause_tid** | **int** | Hvilket svakt lag løsner skredet på? The AvalCauseKD unique identifier | [optional] 
**aval_cause_depth_tid** | **int** | Hvor dypt ligger det overnevnte svake laget? The AvalCauseDepthKD unique identifier | [optional] 
**aval_cause_attributes** | **int** | AvalCauseAttributes er flagging. Det som lagres er ugunstige egenskaper til det svake laget i snøen. Dette er flervalgsliste. Om valg 1 og 4 er valgt lagres 9 (binært 1001). Om valg 1 og 2 er valgt lagres 3 (binært 11). Om bare valg 3 er valgt lagres 4 (binært 100) | [optional] 
**valid_exposition** | **str** | Velg utsatte retninger | [optional] 
**exposed_height1** | **int** | Øverste høyde på “utsatt høyde” symbolet. | [optional] 
**exposed_height2** | **int** | Nederste høyde på “utsatt høyde” symbolet. | [optional] 
**exposed_height_combo_tid** | **int** | Hvilket symbol brukes? Er utsatt tereng over ExposedHeight2 eller under den? The ExposedHeightComboKD unique identifier | [optional] 
**aval_propagation_tid** | **int** | TODO | [optional] 
**comment** | **str** | Kommentar til skredproblemet | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

