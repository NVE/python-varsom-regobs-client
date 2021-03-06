# coding: utf-8

"""
    RegObs API

      ## Introduction    RegObs is a tool for collecting observations and events   related to natural hazards. It is currently used by the   Norwegian flood, landslide and avalanche warning service in   Norway, but the data is openly available for anyone through this API.    Regobs has been developed by the Norwegian Water resources and   Energy Directorate (NVE), in collaboration with the Norwegian   Meteorological Institute (MET) and the Norwegian Public Roads   Administration (NPRA).    You can check out our representation of the data at [regobs.no](http://regobs.no).    ## Authentication    Some endpoints require an api key.  You can get an API key by sending an email to   [raek@nve.no](mailto:raek@nve.no?subject=RegObs%20API%20Key).  To use the api key with the swagger ui, fill in the api\\_key input above.   It should then be included with every request in the   `regObs_apptoken` header.    ## Getting started    Get the last 10 observations using python:    ```python  import requests  r = requests.post('https://api.regobs.no/v4/Search',       data={'NumberOfRecords': 10},      headers={'Content-Type': 'application/json'}  )  data = r.json()  print(len(data))  # 10  ```      # noqa: E501

    OpenAPI spec version: v4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class RegistrationViewModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'reg_id': 'int',
        'geo_hazard_tid': 'int',
        'geo_hazard_name': 'str',
        'lang_key': 'int',
        'dt_obs_time': 'datetime',
        'dt_reg_time': 'datetime',
        'dt_change_time': 'datetime',
        'source_tid': 'int',
        'source_name': 'str',
        'observer': 'ObserverViewModel',
        'obs_location': 'ObsLocationViewModel',
        'attachments': 'list[AttachmentViewModel]',
        'avalanche_activity_obs': 'list[AvalancheActivityObsViewModel]',
        'avalanche_activity_obs2': 'list[AvalancheActivityObs2ViewModel]',
        'avalanche_danger_obs': 'list[AvalancheDangerObsViewModel]',
        'avalanche_eval_problem2': 'list[AvalancheEvalProblem2ViewModel]',
        'avalanche_evaluation3': 'AvalancheEvaluation3ViewModel',
        'avalanche_evaluation': 'AvalancheEvaluationViewModel',
        'avalanche_obs': 'AvalancheObsViewModel',
        'compression_test': 'list[CompressionTestViewModel]',
        'danger_obs': 'list[DangerObsViewModel]',
        'general_observation': 'GeneralObservationViewModel',
        'ice_cover_obs': 'IceCoverViewModel',
        'ice_thickness': 'IceThicknessViewModel',
        'incident': 'IncidentViewModel',
        'snow_profile': 'AttachmentViewModel',
        'land_slide_obs': 'LandslideViewModel',
        'avalanche_eval_problem': 'list[AvalancheEvalProblemViewModel]',
        'snow_cover_obs': 'SnowCoverObsViewModel',
        'snow_profile2': 'SnowProfileViewModel',
        'snow_surface_observation': 'SnowSurfaceViewModel',
        'water_level': 'WaterLevelViewModel',
        'weather_observation': 'WeatherViewModel',
        'water_level2': 'Waterlevel2ViewModel',
        'damage_obs': 'list[DamageObsViewModel]',
        'avalanche_evaluation2': 'AvalancheEvaluation2ViewModel',
        'summaries': 'list[Summary]',
        'attachment_summaries': 'list[Summary]'
    }

    attribute_map = {
        'reg_id': 'RegID',
        'geo_hazard_tid': 'GeoHazardTID',
        'geo_hazard_name': 'GeoHazardName',
        'lang_key': 'LangKey',
        'dt_obs_time': 'DtObsTime',
        'dt_reg_time': 'DtRegTime',
        'dt_change_time': 'DtChangeTime',
        'source_tid': 'SourceTID',
        'source_name': 'SourceName',
        'observer': 'Observer',
        'obs_location': 'ObsLocation',
        'attachments': 'Attachments',
        'avalanche_activity_obs': 'AvalancheActivityObs',
        'avalanche_activity_obs2': 'AvalancheActivityObs2',
        'avalanche_danger_obs': 'AvalancheDangerObs',
        'avalanche_eval_problem2': 'AvalancheEvalProblem2',
        'avalanche_evaluation3': 'AvalancheEvaluation3',
        'avalanche_evaluation': 'AvalancheEvaluation',
        'avalanche_obs': 'AvalancheObs',
        'compression_test': 'CompressionTest',
        'danger_obs': 'DangerObs',
        'general_observation': 'GeneralObservation',
        'ice_cover_obs': 'IceCoverObs',
        'ice_thickness': 'IceThickness',
        'incident': 'Incident',
        'snow_profile': 'SnowProfile',
        'land_slide_obs': 'LandSlideObs',
        'avalanche_eval_problem': 'AvalancheEvalProblem',
        'snow_cover_obs': 'SnowCoverObs',
        'snow_profile2': 'SnowProfile2',
        'snow_surface_observation': 'SnowSurfaceObservation',
        'water_level': 'WaterLevel',
        'weather_observation': 'WeatherObservation',
        'water_level2': 'WaterLevel2',
        'damage_obs': 'DamageObs',
        'avalanche_evaluation2': 'AvalancheEvaluation2',
        'summaries': 'Summaries',
        'attachment_summaries': 'AttachmentSummaries'
    }

    def __init__(self, reg_id=None, geo_hazard_tid=None, geo_hazard_name=None, lang_key=None, dt_obs_time=None, dt_reg_time=None, dt_change_time=None, source_tid=None, source_name=None, observer=None, obs_location=None, attachments=None, avalanche_activity_obs=None, avalanche_activity_obs2=None, avalanche_danger_obs=None, avalanche_eval_problem2=None, avalanche_evaluation3=None, avalanche_evaluation=None, avalanche_obs=None, compression_test=None, danger_obs=None, general_observation=None, ice_cover_obs=None, ice_thickness=None, incident=None, snow_profile=None, land_slide_obs=None, avalanche_eval_problem=None, snow_cover_obs=None, snow_profile2=None, snow_surface_observation=None, water_level=None, weather_observation=None, water_level2=None, damage_obs=None, avalanche_evaluation2=None, summaries=None, attachment_summaries=None):  # noqa: E501
        """RegistrationViewModel - a model defined in Swagger"""  # noqa: E501
        self._reg_id = None
        self._geo_hazard_tid = None
        self._geo_hazard_name = None
        self._lang_key = None
        self._dt_obs_time = None
        self._dt_reg_time = None
        self._dt_change_time = None
        self._source_tid = None
        self._source_name = None
        self._observer = None
        self._obs_location = None
        self._attachments = None
        self._avalanche_activity_obs = None
        self._avalanche_activity_obs2 = None
        self._avalanche_danger_obs = None
        self._avalanche_eval_problem2 = None
        self._avalanche_evaluation3 = None
        self._avalanche_evaluation = None
        self._avalanche_obs = None
        self._compression_test = None
        self._danger_obs = None
        self._general_observation = None
        self._ice_cover_obs = None
        self._ice_thickness = None
        self._incident = None
        self._snow_profile = None
        self._land_slide_obs = None
        self._avalanche_eval_problem = None
        self._snow_cover_obs = None
        self._snow_profile2 = None
        self._snow_surface_observation = None
        self._water_level = None
        self._weather_observation = None
        self._water_level2 = None
        self._damage_obs = None
        self._avalanche_evaluation2 = None
        self._summaries = None
        self._attachment_summaries = None
        self.discriminator = None
        if reg_id is not None:
            self.reg_id = reg_id
        if geo_hazard_tid is not None:
            self.geo_hazard_tid = geo_hazard_tid
        if geo_hazard_name is not None:
            self.geo_hazard_name = geo_hazard_name
        if lang_key is not None:
            self.lang_key = lang_key
        if dt_obs_time is not None:
            self.dt_obs_time = dt_obs_time
        if dt_reg_time is not None:
            self.dt_reg_time = dt_reg_time
        if dt_change_time is not None:
            self.dt_change_time = dt_change_time
        if source_tid is not None:
            self.source_tid = source_tid
        if source_name is not None:
            self.source_name = source_name
        if observer is not None:
            self.observer = observer
        if obs_location is not None:
            self.obs_location = obs_location
        if attachments is not None:
            self.attachments = attachments
        if avalanche_activity_obs is not None:
            self.avalanche_activity_obs = avalanche_activity_obs
        if avalanche_activity_obs2 is not None:
            self.avalanche_activity_obs2 = avalanche_activity_obs2
        if avalanche_danger_obs is not None:
            self.avalanche_danger_obs = avalanche_danger_obs
        if avalanche_eval_problem2 is not None:
            self.avalanche_eval_problem2 = avalanche_eval_problem2
        if avalanche_evaluation3 is not None:
            self.avalanche_evaluation3 = avalanche_evaluation3
        if avalanche_evaluation is not None:
            self.avalanche_evaluation = avalanche_evaluation
        if avalanche_obs is not None:
            self.avalanche_obs = avalanche_obs
        if compression_test is not None:
            self.compression_test = compression_test
        if danger_obs is not None:
            self.danger_obs = danger_obs
        if general_observation is not None:
            self.general_observation = general_observation
        if ice_cover_obs is not None:
            self.ice_cover_obs = ice_cover_obs
        if ice_thickness is not None:
            self.ice_thickness = ice_thickness
        if incident is not None:
            self.incident = incident
        if snow_profile is not None:
            self.snow_profile = snow_profile
        if land_slide_obs is not None:
            self.land_slide_obs = land_slide_obs
        if avalanche_eval_problem is not None:
            self.avalanche_eval_problem = avalanche_eval_problem
        if snow_cover_obs is not None:
            self.snow_cover_obs = snow_cover_obs
        if snow_profile2 is not None:
            self.snow_profile2 = snow_profile2
        if snow_surface_observation is not None:
            self.snow_surface_observation = snow_surface_observation
        if water_level is not None:
            self.water_level = water_level
        if weather_observation is not None:
            self.weather_observation = weather_observation
        if water_level2 is not None:
            self.water_level2 = water_level2
        if damage_obs is not None:
            self.damage_obs = damage_obs
        if avalanche_evaluation2 is not None:
            self.avalanche_evaluation2 = avalanche_evaluation2
        if summaries is not None:
            self.summaries = summaries
        if attachment_summaries is not None:
            self.attachment_summaries = attachment_summaries

    @property
    def reg_id(self):
        """Gets the reg_id of this RegistrationViewModel.  # noqa: E501


        :return: The reg_id of this RegistrationViewModel.  # noqa: E501
        :rtype: int
        """
        return self._reg_id

    @reg_id.setter
    def reg_id(self, reg_id):
        """Sets the reg_id of this RegistrationViewModel.


        :param reg_id: The reg_id of this RegistrationViewModel.  # noqa: E501
        :type: int
        """

        self._reg_id = reg_id

    @property
    def geo_hazard_tid(self):
        """Gets the geo_hazard_tid of this RegistrationViewModel.  # noqa: E501


        :return: The geo_hazard_tid of this RegistrationViewModel.  # noqa: E501
        :rtype: int
        """
        return self._geo_hazard_tid

    @geo_hazard_tid.setter
    def geo_hazard_tid(self, geo_hazard_tid):
        """Sets the geo_hazard_tid of this RegistrationViewModel.


        :param geo_hazard_tid: The geo_hazard_tid of this RegistrationViewModel.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 10, 20, 30, 40, 50, 60, 70, 100, 110, 200, 999]  # noqa: E501
        if geo_hazard_tid not in allowed_values:
            raise ValueError(
                "Invalid value for `geo_hazard_tid` ({0}), must be one of {1}"  # noqa: E501
                .format(geo_hazard_tid, allowed_values)
            )

        self._geo_hazard_tid = geo_hazard_tid

    @property
    def geo_hazard_name(self):
        """Gets the geo_hazard_name of this RegistrationViewModel.  # noqa: E501


        :return: The geo_hazard_name of this RegistrationViewModel.  # noqa: E501
        :rtype: str
        """
        return self._geo_hazard_name

    @geo_hazard_name.setter
    def geo_hazard_name(self, geo_hazard_name):
        """Sets the geo_hazard_name of this RegistrationViewModel.


        :param geo_hazard_name: The geo_hazard_name of this RegistrationViewModel.  # noqa: E501
        :type: str
        """

        self._geo_hazard_name = geo_hazard_name

    @property
    def lang_key(self):
        """Gets the lang_key of this RegistrationViewModel.  # noqa: E501


        :return: The lang_key of this RegistrationViewModel.  # noqa: E501
        :rtype: int
        """
        return self._lang_key

    @lang_key.setter
    def lang_key(self, lang_key):
        """Sets the lang_key of this RegistrationViewModel.


        :param lang_key: The lang_key of this RegistrationViewModel.  # noqa: E501
        :type: int
        """

        self._lang_key = lang_key

    @property
    def dt_obs_time(self):
        """Gets the dt_obs_time of this RegistrationViewModel.  # noqa: E501


        :return: The dt_obs_time of this RegistrationViewModel.  # noqa: E501
        :rtype: datetime
        """
        return self._dt_obs_time

    @dt_obs_time.setter
    def dt_obs_time(self, dt_obs_time):
        """Sets the dt_obs_time of this RegistrationViewModel.


        :param dt_obs_time: The dt_obs_time of this RegistrationViewModel.  # noqa: E501
        :type: datetime
        """

        self._dt_obs_time = dt_obs_time

    @property
    def dt_reg_time(self):
        """Gets the dt_reg_time of this RegistrationViewModel.  # noqa: E501


        :return: The dt_reg_time of this RegistrationViewModel.  # noqa: E501
        :rtype: datetime
        """
        return self._dt_reg_time

    @dt_reg_time.setter
    def dt_reg_time(self, dt_reg_time):
        """Sets the dt_reg_time of this RegistrationViewModel.


        :param dt_reg_time: The dt_reg_time of this RegistrationViewModel.  # noqa: E501
        :type: datetime
        """

        self._dt_reg_time = dt_reg_time

    @property
    def dt_change_time(self):
        """Gets the dt_change_time of this RegistrationViewModel.  # noqa: E501


        :return: The dt_change_time of this RegistrationViewModel.  # noqa: E501
        :rtype: datetime
        """
        return self._dt_change_time

    @dt_change_time.setter
    def dt_change_time(self, dt_change_time):
        """Sets the dt_change_time of this RegistrationViewModel.


        :param dt_change_time: The dt_change_time of this RegistrationViewModel.  # noqa: E501
        :type: datetime
        """

        self._dt_change_time = dt_change_time

    @property
    def source_tid(self):
        """Gets the source_tid of this RegistrationViewModel.  # noqa: E501


        :return: The source_tid of this RegistrationViewModel.  # noqa: E501
        :rtype: int
        """
        return self._source_tid

    @source_tid.setter
    def source_tid(self, source_tid):
        """Sets the source_tid of this RegistrationViewModel.


        :param source_tid: The source_tid of this RegistrationViewModel.  # noqa: E501
        :type: int
        """

        self._source_tid = source_tid

    @property
    def source_name(self):
        """Gets the source_name of this RegistrationViewModel.  # noqa: E501


        :return: The source_name of this RegistrationViewModel.  # noqa: E501
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this RegistrationViewModel.


        :param source_name: The source_name of this RegistrationViewModel.  # noqa: E501
        :type: str
        """

        self._source_name = source_name

    @property
    def observer(self):
        """Gets the observer of this RegistrationViewModel.  # noqa: E501


        :return: The observer of this RegistrationViewModel.  # noqa: E501
        :rtype: ObserverViewModel
        """
        return self._observer

    @observer.setter
    def observer(self, observer):
        """Sets the observer of this RegistrationViewModel.


        :param observer: The observer of this RegistrationViewModel.  # noqa: E501
        :type: ObserverViewModel
        """

        self._observer = observer

    @property
    def obs_location(self):
        """Gets the obs_location of this RegistrationViewModel.  # noqa: E501


        :return: The obs_location of this RegistrationViewModel.  # noqa: E501
        :rtype: ObsLocationViewModel
        """
        return self._obs_location

    @obs_location.setter
    def obs_location(self, obs_location):
        """Sets the obs_location of this RegistrationViewModel.


        :param obs_location: The obs_location of this RegistrationViewModel.  # noqa: E501
        :type: ObsLocationViewModel
        """

        self._obs_location = obs_location

    @property
    def attachments(self):
        """Gets the attachments of this RegistrationViewModel.  # noqa: E501


        :return: The attachments of this RegistrationViewModel.  # noqa: E501
        :rtype: list[AttachmentViewModel]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this RegistrationViewModel.


        :param attachments: The attachments of this RegistrationViewModel.  # noqa: E501
        :type: list[AttachmentViewModel]
        """

        self._attachments = attachments

    @property
    def avalanche_activity_obs(self):
        """Gets the avalanche_activity_obs of this RegistrationViewModel.  # noqa: E501


        :return: The avalanche_activity_obs of this RegistrationViewModel.  # noqa: E501
        :rtype: list[AvalancheActivityObsViewModel]
        """
        return self._avalanche_activity_obs

    @avalanche_activity_obs.setter
    def avalanche_activity_obs(self, avalanche_activity_obs):
        """Sets the avalanche_activity_obs of this RegistrationViewModel.


        :param avalanche_activity_obs: The avalanche_activity_obs of this RegistrationViewModel.  # noqa: E501
        :type: list[AvalancheActivityObsViewModel]
        """

        self._avalanche_activity_obs = avalanche_activity_obs

    @property
    def avalanche_activity_obs2(self):
        """Gets the avalanche_activity_obs2 of this RegistrationViewModel.  # noqa: E501


        :return: The avalanche_activity_obs2 of this RegistrationViewModel.  # noqa: E501
        :rtype: list[AvalancheActivityObs2ViewModel]
        """
        return self._avalanche_activity_obs2

    @avalanche_activity_obs2.setter
    def avalanche_activity_obs2(self, avalanche_activity_obs2):
        """Sets the avalanche_activity_obs2 of this RegistrationViewModel.


        :param avalanche_activity_obs2: The avalanche_activity_obs2 of this RegistrationViewModel.  # noqa: E501
        :type: list[AvalancheActivityObs2ViewModel]
        """

        self._avalanche_activity_obs2 = avalanche_activity_obs2

    @property
    def avalanche_danger_obs(self):
        """Gets the avalanche_danger_obs of this RegistrationViewModel.  # noqa: E501


        :return: The avalanche_danger_obs of this RegistrationViewModel.  # noqa: E501
        :rtype: list[AvalancheDangerObsViewModel]
        """
        return self._avalanche_danger_obs

    @avalanche_danger_obs.setter
    def avalanche_danger_obs(self, avalanche_danger_obs):
        """Sets the avalanche_danger_obs of this RegistrationViewModel.


        :param avalanche_danger_obs: The avalanche_danger_obs of this RegistrationViewModel.  # noqa: E501
        :type: list[AvalancheDangerObsViewModel]
        """

        self._avalanche_danger_obs = avalanche_danger_obs

    @property
    def avalanche_eval_problem2(self):
        """Gets the avalanche_eval_problem2 of this RegistrationViewModel.  # noqa: E501


        :return: The avalanche_eval_problem2 of this RegistrationViewModel.  # noqa: E501
        :rtype: list[AvalancheEvalProblem2ViewModel]
        """
        return self._avalanche_eval_problem2

    @avalanche_eval_problem2.setter
    def avalanche_eval_problem2(self, avalanche_eval_problem2):
        """Sets the avalanche_eval_problem2 of this RegistrationViewModel.


        :param avalanche_eval_problem2: The avalanche_eval_problem2 of this RegistrationViewModel.  # noqa: E501
        :type: list[AvalancheEvalProblem2ViewModel]
        """

        self._avalanche_eval_problem2 = avalanche_eval_problem2

    @property
    def avalanche_evaluation3(self):
        """Gets the avalanche_evaluation3 of this RegistrationViewModel.  # noqa: E501


        :return: The avalanche_evaluation3 of this RegistrationViewModel.  # noqa: E501
        :rtype: AvalancheEvaluation3ViewModel
        """
        return self._avalanche_evaluation3

    @avalanche_evaluation3.setter
    def avalanche_evaluation3(self, avalanche_evaluation3):
        """Sets the avalanche_evaluation3 of this RegistrationViewModel.


        :param avalanche_evaluation3: The avalanche_evaluation3 of this RegistrationViewModel.  # noqa: E501
        :type: AvalancheEvaluation3ViewModel
        """

        self._avalanche_evaluation3 = avalanche_evaluation3

    @property
    def avalanche_evaluation(self):
        """Gets the avalanche_evaluation of this RegistrationViewModel.  # noqa: E501


        :return: The avalanche_evaluation of this RegistrationViewModel.  # noqa: E501
        :rtype: AvalancheEvaluationViewModel
        """
        return self._avalanche_evaluation

    @avalanche_evaluation.setter
    def avalanche_evaluation(self, avalanche_evaluation):
        """Sets the avalanche_evaluation of this RegistrationViewModel.


        :param avalanche_evaluation: The avalanche_evaluation of this RegistrationViewModel.  # noqa: E501
        :type: AvalancheEvaluationViewModel
        """

        self._avalanche_evaluation = avalanche_evaluation

    @property
    def avalanche_obs(self):
        """Gets the avalanche_obs of this RegistrationViewModel.  # noqa: E501


        :return: The avalanche_obs of this RegistrationViewModel.  # noqa: E501
        :rtype: AvalancheObsViewModel
        """
        return self._avalanche_obs

    @avalanche_obs.setter
    def avalanche_obs(self, avalanche_obs):
        """Sets the avalanche_obs of this RegistrationViewModel.


        :param avalanche_obs: The avalanche_obs of this RegistrationViewModel.  # noqa: E501
        :type: AvalancheObsViewModel
        """

        self._avalanche_obs = avalanche_obs

    @property
    def compression_test(self):
        """Gets the compression_test of this RegistrationViewModel.  # noqa: E501


        :return: The compression_test of this RegistrationViewModel.  # noqa: E501
        :rtype: list[CompressionTestViewModel]
        """
        return self._compression_test

    @compression_test.setter
    def compression_test(self, compression_test):
        """Sets the compression_test of this RegistrationViewModel.


        :param compression_test: The compression_test of this RegistrationViewModel.  # noqa: E501
        :type: list[CompressionTestViewModel]
        """

        self._compression_test = compression_test

    @property
    def danger_obs(self):
        """Gets the danger_obs of this RegistrationViewModel.  # noqa: E501


        :return: The danger_obs of this RegistrationViewModel.  # noqa: E501
        :rtype: list[DangerObsViewModel]
        """
        return self._danger_obs

    @danger_obs.setter
    def danger_obs(self, danger_obs):
        """Sets the danger_obs of this RegistrationViewModel.


        :param danger_obs: The danger_obs of this RegistrationViewModel.  # noqa: E501
        :type: list[DangerObsViewModel]
        """

        self._danger_obs = danger_obs

    @property
    def general_observation(self):
        """Gets the general_observation of this RegistrationViewModel.  # noqa: E501


        :return: The general_observation of this RegistrationViewModel.  # noqa: E501
        :rtype: GeneralObservationViewModel
        """
        return self._general_observation

    @general_observation.setter
    def general_observation(self, general_observation):
        """Sets the general_observation of this RegistrationViewModel.


        :param general_observation: The general_observation of this RegistrationViewModel.  # noqa: E501
        :type: GeneralObservationViewModel
        """

        self._general_observation = general_observation

    @property
    def ice_cover_obs(self):
        """Gets the ice_cover_obs of this RegistrationViewModel.  # noqa: E501


        :return: The ice_cover_obs of this RegistrationViewModel.  # noqa: E501
        :rtype: IceCoverViewModel
        """
        return self._ice_cover_obs

    @ice_cover_obs.setter
    def ice_cover_obs(self, ice_cover_obs):
        """Sets the ice_cover_obs of this RegistrationViewModel.


        :param ice_cover_obs: The ice_cover_obs of this RegistrationViewModel.  # noqa: E501
        :type: IceCoverViewModel
        """

        self._ice_cover_obs = ice_cover_obs

    @property
    def ice_thickness(self):
        """Gets the ice_thickness of this RegistrationViewModel.  # noqa: E501


        :return: The ice_thickness of this RegistrationViewModel.  # noqa: E501
        :rtype: IceThicknessViewModel
        """
        return self._ice_thickness

    @ice_thickness.setter
    def ice_thickness(self, ice_thickness):
        """Sets the ice_thickness of this RegistrationViewModel.


        :param ice_thickness: The ice_thickness of this RegistrationViewModel.  # noqa: E501
        :type: IceThicknessViewModel
        """

        self._ice_thickness = ice_thickness

    @property
    def incident(self):
        """Gets the incident of this RegistrationViewModel.  # noqa: E501


        :return: The incident of this RegistrationViewModel.  # noqa: E501
        :rtype: IncidentViewModel
        """
        return self._incident

    @incident.setter
    def incident(self, incident):
        """Sets the incident of this RegistrationViewModel.


        :param incident: The incident of this RegistrationViewModel.  # noqa: E501
        :type: IncidentViewModel
        """

        self._incident = incident

    @property
    def snow_profile(self):
        """Gets the snow_profile of this RegistrationViewModel.  # noqa: E501


        :return: The snow_profile of this RegistrationViewModel.  # noqa: E501
        :rtype: AttachmentViewModel
        """
        return self._snow_profile

    @snow_profile.setter
    def snow_profile(self, snow_profile):
        """Sets the snow_profile of this RegistrationViewModel.


        :param snow_profile: The snow_profile of this RegistrationViewModel.  # noqa: E501
        :type: AttachmentViewModel
        """

        self._snow_profile = snow_profile

    @property
    def land_slide_obs(self):
        """Gets the land_slide_obs of this RegistrationViewModel.  # noqa: E501


        :return: The land_slide_obs of this RegistrationViewModel.  # noqa: E501
        :rtype: LandslideViewModel
        """
        return self._land_slide_obs

    @land_slide_obs.setter
    def land_slide_obs(self, land_slide_obs):
        """Sets the land_slide_obs of this RegistrationViewModel.


        :param land_slide_obs: The land_slide_obs of this RegistrationViewModel.  # noqa: E501
        :type: LandslideViewModel
        """

        self._land_slide_obs = land_slide_obs

    @property
    def avalanche_eval_problem(self):
        """Gets the avalanche_eval_problem of this RegistrationViewModel.  # noqa: E501


        :return: The avalanche_eval_problem of this RegistrationViewModel.  # noqa: E501
        :rtype: list[AvalancheEvalProblemViewModel]
        """
        return self._avalanche_eval_problem

    @avalanche_eval_problem.setter
    def avalanche_eval_problem(self, avalanche_eval_problem):
        """Sets the avalanche_eval_problem of this RegistrationViewModel.


        :param avalanche_eval_problem: The avalanche_eval_problem of this RegistrationViewModel.  # noqa: E501
        :type: list[AvalancheEvalProblemViewModel]
        """

        self._avalanche_eval_problem = avalanche_eval_problem

    @property
    def snow_cover_obs(self):
        """Gets the snow_cover_obs of this RegistrationViewModel.  # noqa: E501


        :return: The snow_cover_obs of this RegistrationViewModel.  # noqa: E501
        :rtype: SnowCoverObsViewModel
        """
        return self._snow_cover_obs

    @snow_cover_obs.setter
    def snow_cover_obs(self, snow_cover_obs):
        """Sets the snow_cover_obs of this RegistrationViewModel.


        :param snow_cover_obs: The snow_cover_obs of this RegistrationViewModel.  # noqa: E501
        :type: SnowCoverObsViewModel
        """

        self._snow_cover_obs = snow_cover_obs

    @property
    def snow_profile2(self):
        """Gets the snow_profile2 of this RegistrationViewModel.  # noqa: E501


        :return: The snow_profile2 of this RegistrationViewModel.  # noqa: E501
        :rtype: SnowProfileViewModel
        """
        return self._snow_profile2

    @snow_profile2.setter
    def snow_profile2(self, snow_profile2):
        """Sets the snow_profile2 of this RegistrationViewModel.


        :param snow_profile2: The snow_profile2 of this RegistrationViewModel.  # noqa: E501
        :type: SnowProfileViewModel
        """

        self._snow_profile2 = snow_profile2

    @property
    def snow_surface_observation(self):
        """Gets the snow_surface_observation of this RegistrationViewModel.  # noqa: E501


        :return: The snow_surface_observation of this RegistrationViewModel.  # noqa: E501
        :rtype: SnowSurfaceViewModel
        """
        return self._snow_surface_observation

    @snow_surface_observation.setter
    def snow_surface_observation(self, snow_surface_observation):
        """Sets the snow_surface_observation of this RegistrationViewModel.


        :param snow_surface_observation: The snow_surface_observation of this RegistrationViewModel.  # noqa: E501
        :type: SnowSurfaceViewModel
        """

        self._snow_surface_observation = snow_surface_observation

    @property
    def water_level(self):
        """Gets the water_level of this RegistrationViewModel.  # noqa: E501


        :return: The water_level of this RegistrationViewModel.  # noqa: E501
        :rtype: WaterLevelViewModel
        """
        return self._water_level

    @water_level.setter
    def water_level(self, water_level):
        """Sets the water_level of this RegistrationViewModel.


        :param water_level: The water_level of this RegistrationViewModel.  # noqa: E501
        :type: WaterLevelViewModel
        """

        self._water_level = water_level

    @property
    def weather_observation(self):
        """Gets the weather_observation of this RegistrationViewModel.  # noqa: E501


        :return: The weather_observation of this RegistrationViewModel.  # noqa: E501
        :rtype: WeatherViewModel
        """
        return self._weather_observation

    @weather_observation.setter
    def weather_observation(self, weather_observation):
        """Sets the weather_observation of this RegistrationViewModel.


        :param weather_observation: The weather_observation of this RegistrationViewModel.  # noqa: E501
        :type: WeatherViewModel
        """

        self._weather_observation = weather_observation

    @property
    def water_level2(self):
        """Gets the water_level2 of this RegistrationViewModel.  # noqa: E501


        :return: The water_level2 of this RegistrationViewModel.  # noqa: E501
        :rtype: Waterlevel2ViewModel
        """
        return self._water_level2

    @water_level2.setter
    def water_level2(self, water_level2):
        """Sets the water_level2 of this RegistrationViewModel.


        :param water_level2: The water_level2 of this RegistrationViewModel.  # noqa: E501
        :type: Waterlevel2ViewModel
        """

        self._water_level2 = water_level2

    @property
    def damage_obs(self):
        """Gets the damage_obs of this RegistrationViewModel.  # noqa: E501


        :return: The damage_obs of this RegistrationViewModel.  # noqa: E501
        :rtype: list[DamageObsViewModel]
        """
        return self._damage_obs

    @damage_obs.setter
    def damage_obs(self, damage_obs):
        """Sets the damage_obs of this RegistrationViewModel.


        :param damage_obs: The damage_obs of this RegistrationViewModel.  # noqa: E501
        :type: list[DamageObsViewModel]
        """

        self._damage_obs = damage_obs

    @property
    def avalanche_evaluation2(self):
        """Gets the avalanche_evaluation2 of this RegistrationViewModel.  # noqa: E501


        :return: The avalanche_evaluation2 of this RegistrationViewModel.  # noqa: E501
        :rtype: AvalancheEvaluation2ViewModel
        """
        return self._avalanche_evaluation2

    @avalanche_evaluation2.setter
    def avalanche_evaluation2(self, avalanche_evaluation2):
        """Sets the avalanche_evaluation2 of this RegistrationViewModel.


        :param avalanche_evaluation2: The avalanche_evaluation2 of this RegistrationViewModel.  # noqa: E501
        :type: AvalancheEvaluation2ViewModel
        """

        self._avalanche_evaluation2 = avalanche_evaluation2

    @property
    def summaries(self):
        """Gets the summaries of this RegistrationViewModel.  # noqa: E501


        :return: The summaries of this RegistrationViewModel.  # noqa: E501
        :rtype: list[Summary]
        """
        return self._summaries

    @summaries.setter
    def summaries(self, summaries):
        """Sets the summaries of this RegistrationViewModel.


        :param summaries: The summaries of this RegistrationViewModel.  # noqa: E501
        :type: list[Summary]
        """

        self._summaries = summaries

    @property
    def attachment_summaries(self):
        """Gets the attachment_summaries of this RegistrationViewModel.  # noqa: E501


        :return: The attachment_summaries of this RegistrationViewModel.  # noqa: E501
        :rtype: list[Summary]
        """
        return self._attachment_summaries

    @attachment_summaries.setter
    def attachment_summaries(self, attachment_summaries):
        """Sets the attachment_summaries of this RegistrationViewModel.


        :param attachment_summaries: The attachment_summaries of this RegistrationViewModel.  # noqa: E501
        :type: list[Summary]
        """

        self._attachment_summaries = attachment_summaries

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RegistrationViewModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RegistrationViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
