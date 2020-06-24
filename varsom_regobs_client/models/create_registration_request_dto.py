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


class CreateRegistrationRequestDto(object):
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
        'id': 'str',
        'geo_hazard_tid': 'int',
        'dt_obs_time': 'datetime',
        'observer_guid': 'str',
        'email': 'bool',
        'obs_location_id': 'int',
        'observer_group_id': 'int',
        'comment': 'str',
        'source_tid': 'int',
        'avalanche_activity_obs': 'list[AvalancheActivityObsDto]',
        'avalanche_activity_obs2': 'list[AvalancheActivityObs2Dto]',
        'avalanche_danger_obs': 'list[AvalancheDangerObsDto]',
        'avalanche_eval_problem2': 'list[AvalancheEvalProblem2Dto]',
        'avalanche_evaluation3': 'AvalancheEvaluation3Dto',
        'avalanche_obs': 'AvalancheObsDto',
        'compression_test': 'list[CompressionTestDto]',
        'danger_obs': 'list[DangerObsDto]',
        'general_observation': 'GeneralObservationEditModel',
        'ice_cover_obs': 'IceCoverObsDto',
        'ice_thickness': 'IceThicknessDto',
        'incident': 'IncidentDto',
        'land_slide_obs': 'LandSlideObsDto',
        'obs_location': 'ObsLocationDto',
        'picture': 'list[PictureRequestDto]',
        'snow_cover_obs': 'SnowCoverObsDto',
        'snow_profile': 'PictureRequestDto',
        'snow_profile2': 'SnowProfileDto',
        'snow_surface_observation': 'SnowSurfaceObservationDto',
        'water_level': 'WaterLevelDto',
        'weather_observation': 'WeatherObservationDto',
        'water_level2': 'WaterLevel2Dto',
        'damage_obs': 'list[DamageObsDto]',
        'density_profile': 'DensityProfileDto'
    }

    attribute_map = {
        'id': 'Id',
        'geo_hazard_tid': 'GeoHazardTID',
        'dt_obs_time': 'DtObsTime',
        'observer_guid': 'ObserverGuid',
        'email': 'Email',
        'obs_location_id': 'ObsLocationID',
        'observer_group_id': 'ObserverGroupID',
        'comment': 'Comment',
        'source_tid': 'SourceTID',
        'avalanche_activity_obs': 'AvalancheActivityObs',
        'avalanche_activity_obs2': 'AvalancheActivityObs2',
        'avalanche_danger_obs': 'AvalancheDangerObs',
        'avalanche_eval_problem2': 'AvalancheEvalProblem2',
        'avalanche_evaluation3': 'AvalancheEvaluation3',
        'avalanche_obs': 'AvalancheObs',
        'compression_test': 'CompressionTest',
        'danger_obs': 'DangerObs',
        'general_observation': 'GeneralObservation',
        'ice_cover_obs': 'IceCoverObs',
        'ice_thickness': 'IceThickness',
        'incident': 'Incident',
        'land_slide_obs': 'LandSlideObs',
        'obs_location': 'ObsLocation',
        'picture': 'Picture',
        'snow_cover_obs': 'SnowCoverObs',
        'snow_profile': 'SnowProfile',
        'snow_profile2': 'SnowProfile2',
        'snow_surface_observation': 'SnowSurfaceObservation',
        'water_level': 'WaterLevel',
        'weather_observation': 'WeatherObservation',
        'water_level2': 'WaterLevel2',
        'damage_obs': 'DamageObs',
        'density_profile': 'DensityProfile'
    }

    def __init__(self, id=None, geo_hazard_tid=None, dt_obs_time=None, observer_guid=None, email=None, obs_location_id=None, observer_group_id=None, comment=None, source_tid=None, avalanche_activity_obs=None, avalanche_activity_obs2=None, avalanche_danger_obs=None, avalanche_eval_problem2=None, avalanche_evaluation3=None, avalanche_obs=None, compression_test=None, danger_obs=None, general_observation=None, ice_cover_obs=None, ice_thickness=None, incident=None, land_slide_obs=None, obs_location=None, picture=None, snow_cover_obs=None, snow_profile=None, snow_profile2=None, snow_surface_observation=None, water_level=None, weather_observation=None, water_level2=None, damage_obs=None, density_profile=None):  # noqa: E501
        """CreateRegistrationRequestDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._geo_hazard_tid = None
        self._dt_obs_time = None
        self._observer_guid = None
        self._email = None
        self._obs_location_id = None
        self._observer_group_id = None
        self._comment = None
        self._source_tid = None
        self._avalanche_activity_obs = None
        self._avalanche_activity_obs2 = None
        self._avalanche_danger_obs = None
        self._avalanche_eval_problem2 = None
        self._avalanche_evaluation3 = None
        self._avalanche_obs = None
        self._compression_test = None
        self._danger_obs = None
        self._general_observation = None
        self._ice_cover_obs = None
        self._ice_thickness = None
        self._incident = None
        self._land_slide_obs = None
        self._obs_location = None
        self._picture = None
        self._snow_cover_obs = None
        self._snow_profile = None
        self._snow_profile2 = None
        self._snow_surface_observation = None
        self._water_level = None
        self._weather_observation = None
        self._water_level2 = None
        self._damage_obs = None
        self._density_profile = None
        self.discriminator = None
        self.id = id
        self.geo_hazard_tid = geo_hazard_tid
        self.dt_obs_time = dt_obs_time
        self.observer_guid = observer_guid
        if email is not None:
            self.email = email
        if obs_location_id is not None:
            self.obs_location_id = obs_location_id
        if observer_group_id is not None:
            self.observer_group_id = observer_group_id
        if comment is not None:
            self.comment = comment
        if source_tid is not None:
            self.source_tid = source_tid
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
        if land_slide_obs is not None:
            self.land_slide_obs = land_slide_obs
        if obs_location is not None:
            self.obs_location = obs_location
        if picture is not None:
            self.picture = picture
        if snow_cover_obs is not None:
            self.snow_cover_obs = snow_cover_obs
        if snow_profile is not None:
            self.snow_profile = snow_profile
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
        if density_profile is not None:
            self.density_profile = density_profile

    @property
    def id(self):
        """Gets the id of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The id of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateRegistrationRequestDto.


        :param id: The id of this CreateRegistrationRequestDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def geo_hazard_tid(self):
        """Gets the geo_hazard_tid of this CreateRegistrationRequestDto.  # noqa: E501

        Sett naturfare. Tabellen brukes av alle naturfarer (snø, jord, vann, is). The GeoHazardKD unique identifier  # noqa: E501

        :return: The geo_hazard_tid of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._geo_hazard_tid

    @geo_hazard_tid.setter
    def geo_hazard_tid(self, geo_hazard_tid):
        """Sets the geo_hazard_tid of this CreateRegistrationRequestDto.

        Sett naturfare. Tabellen brukes av alle naturfarer (snø, jord, vann, is). The GeoHazardKD unique identifier  # noqa: E501

        :param geo_hazard_tid: The geo_hazard_tid of this CreateRegistrationRequestDto.  # noqa: E501
        :type: int
        """
        if geo_hazard_tid is None:
            raise ValueError("Invalid value for `geo_hazard_tid`, must not be `None`")  # noqa: E501
        allowed_values = [0, 10, 20, 30, 40, 50, 60, 70, 100, 110, 200, 999]  # noqa: E501
        if geo_hazard_tid not in allowed_values:
            raise ValueError(
                "Invalid value for `geo_hazard_tid` ({0}), must be one of {1}"  # noqa: E501
                .format(geo_hazard_tid, allowed_values)
            )

        self._geo_hazard_tid = geo_hazard_tid

    @property
    def dt_obs_time(self):
        """Gets the dt_obs_time of this CreateRegistrationRequestDto.  # noqa: E501

        Tiden da observasjonen ble gjort.  # noqa: E501

        :return: The dt_obs_time of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: datetime
        """
        return self._dt_obs_time

    @dt_obs_time.setter
    def dt_obs_time(self, dt_obs_time):
        """Sets the dt_obs_time of this CreateRegistrationRequestDto.

        Tiden da observasjonen ble gjort.  # noqa: E501

        :param dt_obs_time: The dt_obs_time of this CreateRegistrationRequestDto.  # noqa: E501
        :type: datetime
        """
        if dt_obs_time is None:
            raise ValueError("Invalid value for `dt_obs_time`, must not be `None`")  # noqa: E501

        self._dt_obs_time = dt_obs_time

    @property
    def observer_guid(self):
        """Gets the observer_guid of this CreateRegistrationRequestDto.  # noqa: E501

        Unik ID for observatører (brukere). Denne lages av regObs systemet.  # noqa: E501

        :return: The observer_guid of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._observer_guid

    @observer_guid.setter
    def observer_guid(self, observer_guid):
        """Sets the observer_guid of this CreateRegistrationRequestDto.

        Unik ID for observatører (brukere). Denne lages av regObs systemet.  # noqa: E501

        :param observer_guid: The observer_guid of this CreateRegistrationRequestDto.  # noqa: E501
        :type: str
        """
        if observer_guid is None:
            raise ValueError("Invalid value for `observer_guid`, must not be `None`")  # noqa: E501

        self._observer_guid = observer_guid

    @property
    def email(self):
        """Gets the email of this CreateRegistrationRequestDto.  # noqa: E501

        Wether or not a confirmation email should be sent to user for this registration.  # noqa: E501

        :return: The email of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateRegistrationRequestDto.

        Wether or not a confirmation email should be sent to user for this registration.  # noqa: E501

        :param email: The email of this CreateRegistrationRequestDto.  # noqa: E501
        :type: bool
        """

        self._email = email

    @property
    def obs_location_id(self):
        """Gets the obs_location_id of this CreateRegistrationRequestDto.  # noqa: E501

        Unik ID på ulike observasjonssteder.  # noqa: E501

        :return: The obs_location_id of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._obs_location_id

    @obs_location_id.setter
    def obs_location_id(self, obs_location_id):
        """Sets the obs_location_id of this CreateRegistrationRequestDto.

        Unik ID på ulike observasjonssteder.  # noqa: E501

        :param obs_location_id: The obs_location_id of this CreateRegistrationRequestDto.  # noqa: E501
        :type: int
        """

        self._obs_location_id = obs_location_id

    @property
    def observer_group_id(self):
        """Gets the observer_group_id of this CreateRegistrationRequestDto.  # noqa: E501

        Hvis en bruker registrerer en observasjon på vegne av en gruppe legges det til her.  # noqa: E501

        :return: The observer_group_id of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._observer_group_id

    @observer_group_id.setter
    def observer_group_id(self, observer_group_id):
        """Sets the observer_group_id of this CreateRegistrationRequestDto.

        Hvis en bruker registrerer en observasjon på vegne av en gruppe legges det til her.  # noqa: E501

        :param observer_group_id: The observer_group_id of this CreateRegistrationRequestDto.  # noqa: E501
        :type: int
        """

        self._observer_group_id = observer_group_id

    @property
    def comment(self):
        """Gets the comment of this CreateRegistrationRequestDto.  # noqa: E501

        Kommentarfelt brukt av systemet.  # noqa: E501

        :return: The comment of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreateRegistrationRequestDto.

        Kommentarfelt brukt av systemet.  # noqa: E501

        :param comment: The comment of this CreateRegistrationRequestDto.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def source_tid(self):
        """Gets the source_tid of this CreateRegistrationRequestDto.  # noqa: E501

        Kildereferanse på en registrering. F.eks. har brukeren sette dette selv eller er det referert til fra nyheter. The SourceKD unique identifier  # noqa: E501

        :return: The source_tid of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._source_tid

    @source_tid.setter
    def source_tid(self, source_tid):
        """Sets the source_tid of this CreateRegistrationRequestDto.

        Kildereferanse på en registrering. F.eks. har brukeren sette dette selv eller er det referert til fra nyheter. The SourceKD unique identifier  # noqa: E501

        :param source_tid: The source_tid of this CreateRegistrationRequestDto.  # noqa: E501
        :type: int
        """

        self._source_tid = source_tid

    @property
    def avalanche_activity_obs(self):
        """Gets the avalanche_activity_obs of this CreateRegistrationRequestDto.  # noqa: E501

        Tabell for skredaktivitet.  # noqa: E501

        :return: The avalanche_activity_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: list[AvalancheActivityObsDto]
        """
        return self._avalanche_activity_obs

    @avalanche_activity_obs.setter
    def avalanche_activity_obs(self, avalanche_activity_obs):
        """Sets the avalanche_activity_obs of this CreateRegistrationRequestDto.

        Tabell for skredaktivitet.  # noqa: E501

        :param avalanche_activity_obs: The avalanche_activity_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :type: list[AvalancheActivityObsDto]
        """

        self._avalanche_activity_obs = avalanche_activity_obs

    @property
    def avalanche_activity_obs2(self):
        """Gets the avalanche_activity_obs2 of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The avalanche_activity_obs2 of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: list[AvalancheActivityObs2Dto]
        """
        return self._avalanche_activity_obs2

    @avalanche_activity_obs2.setter
    def avalanche_activity_obs2(self, avalanche_activity_obs2):
        """Sets the avalanche_activity_obs2 of this CreateRegistrationRequestDto.


        :param avalanche_activity_obs2: The avalanche_activity_obs2 of this CreateRegistrationRequestDto.  # noqa: E501
        :type: list[AvalancheActivityObs2Dto]
        """

        self._avalanche_activity_obs2 = avalanche_activity_obs2

    @property
    def avalanche_danger_obs(self):
        """Gets the avalanche_danger_obs of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The avalanche_danger_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: list[AvalancheDangerObsDto]
        """
        return self._avalanche_danger_obs

    @avalanche_danger_obs.setter
    def avalanche_danger_obs(self, avalanche_danger_obs):
        """Sets the avalanche_danger_obs of this CreateRegistrationRequestDto.


        :param avalanche_danger_obs: The avalanche_danger_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :type: list[AvalancheDangerObsDto]
        """

        self._avalanche_danger_obs = avalanche_danger_obs

    @property
    def avalanche_eval_problem2(self):
        """Gets the avalanche_eval_problem2 of this CreateRegistrationRequestDto.  # noqa: E501

        Tabell for skredproblemet. Denne har vært under skredfarevurderingsskjema.  # noqa: E501

        :return: The avalanche_eval_problem2 of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: list[AvalancheEvalProblem2Dto]
        """
        return self._avalanche_eval_problem2

    @avalanche_eval_problem2.setter
    def avalanche_eval_problem2(self, avalanche_eval_problem2):
        """Sets the avalanche_eval_problem2 of this CreateRegistrationRequestDto.

        Tabell for skredproblemet. Denne har vært under skredfarevurderingsskjema.  # noqa: E501

        :param avalanche_eval_problem2: The avalanche_eval_problem2 of this CreateRegistrationRequestDto.  # noqa: E501
        :type: list[AvalancheEvalProblem2Dto]
        """

        self._avalanche_eval_problem2 = avalanche_eval_problem2

    @property
    def avalanche_evaluation3(self):
        """Gets the avalanche_evaluation3 of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The avalanche_evaluation3 of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: AvalancheEvaluation3Dto
        """
        return self._avalanche_evaluation3

    @avalanche_evaluation3.setter
    def avalanche_evaluation3(self, avalanche_evaluation3):
        """Sets the avalanche_evaluation3 of this CreateRegistrationRequestDto.


        :param avalanche_evaluation3: The avalanche_evaluation3 of this CreateRegistrationRequestDto.  # noqa: E501
        :type: AvalancheEvaluation3Dto
        """

        self._avalanche_evaluation3 = avalanche_evaluation3

    @property
    def avalanche_obs(self):
        """Gets the avalanche_obs of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The avalanche_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: AvalancheObsDto
        """
        return self._avalanche_obs

    @avalanche_obs.setter
    def avalanche_obs(self, avalanche_obs):
        """Sets the avalanche_obs of this CreateRegistrationRequestDto.


        :param avalanche_obs: The avalanche_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :type: AvalancheObsDto
        """

        self._avalanche_obs = avalanche_obs

    @property
    def compression_test(self):
        """Gets the compression_test of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The compression_test of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: list[CompressionTestDto]
        """
        return self._compression_test

    @compression_test.setter
    def compression_test(self, compression_test):
        """Sets the compression_test of this CreateRegistrationRequestDto.


        :param compression_test: The compression_test of this CreateRegistrationRequestDto.  # noqa: E501
        :type: list[CompressionTestDto]
        """

        self._compression_test = compression_test

    @property
    def danger_obs(self):
        """Gets the danger_obs of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The danger_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: list[DangerObsDto]
        """
        return self._danger_obs

    @danger_obs.setter
    def danger_obs(self, danger_obs):
        """Sets the danger_obs of this CreateRegistrationRequestDto.


        :param danger_obs: The danger_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :type: list[DangerObsDto]
        """

        self._danger_obs = danger_obs

    @property
    def general_observation(self):
        """Gets the general_observation of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The general_observation of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: GeneralObservationEditModel
        """
        return self._general_observation

    @general_observation.setter
    def general_observation(self, general_observation):
        """Sets the general_observation of this CreateRegistrationRequestDto.


        :param general_observation: The general_observation of this CreateRegistrationRequestDto.  # noqa: E501
        :type: GeneralObservationEditModel
        """

        self._general_observation = general_observation

    @property
    def ice_cover_obs(self):
        """Gets the ice_cover_obs of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The ice_cover_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: IceCoverObsDto
        """
        return self._ice_cover_obs

    @ice_cover_obs.setter
    def ice_cover_obs(self, ice_cover_obs):
        """Sets the ice_cover_obs of this CreateRegistrationRequestDto.


        :param ice_cover_obs: The ice_cover_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :type: IceCoverObsDto
        """

        self._ice_cover_obs = ice_cover_obs

    @property
    def ice_thickness(self):
        """Gets the ice_thickness of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The ice_thickness of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: IceThicknessDto
        """
        return self._ice_thickness

    @ice_thickness.setter
    def ice_thickness(self, ice_thickness):
        """Sets the ice_thickness of this CreateRegistrationRequestDto.


        :param ice_thickness: The ice_thickness of this CreateRegistrationRequestDto.  # noqa: E501
        :type: IceThicknessDto
        """

        self._ice_thickness = ice_thickness

    @property
    def incident(self):
        """Gets the incident of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The incident of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: IncidentDto
        """
        return self._incident

    @incident.setter
    def incident(self, incident):
        """Sets the incident of this CreateRegistrationRequestDto.


        :param incident: The incident of this CreateRegistrationRequestDto.  # noqa: E501
        :type: IncidentDto
        """

        self._incident = incident

    @property
    def land_slide_obs(self):
        """Gets the land_slide_obs of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The land_slide_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: LandSlideObsDto
        """
        return self._land_slide_obs

    @land_slide_obs.setter
    def land_slide_obs(self, land_slide_obs):
        """Sets the land_slide_obs of this CreateRegistrationRequestDto.


        :param land_slide_obs: The land_slide_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :type: LandSlideObsDto
        """

        self._land_slide_obs = land_slide_obs

    @property
    def obs_location(self):
        """Gets the obs_location of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The obs_location of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: ObsLocationDto
        """
        return self._obs_location

    @obs_location.setter
    def obs_location(self, obs_location):
        """Sets the obs_location of this CreateRegistrationRequestDto.


        :param obs_location: The obs_location of this CreateRegistrationRequestDto.  # noqa: E501
        :type: ObsLocationDto
        """

        self._obs_location = obs_location

    @property
    def picture(self):
        """Gets the picture of this CreateRegistrationRequestDto.  # noqa: E501

        Tabell for bilder.  # noqa: E501

        :return: The picture of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: list[PictureRequestDto]
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this CreateRegistrationRequestDto.

        Tabell for bilder.  # noqa: E501

        :param picture: The picture of this CreateRegistrationRequestDto.  # noqa: E501
        :type: list[PictureRequestDto]
        """

        self._picture = picture

    @property
    def snow_cover_obs(self):
        """Gets the snow_cover_obs of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The snow_cover_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: SnowCoverObsDto
        """
        return self._snow_cover_obs

    @snow_cover_obs.setter
    def snow_cover_obs(self, snow_cover_obs):
        """Sets the snow_cover_obs of this CreateRegistrationRequestDto.


        :param snow_cover_obs: The snow_cover_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :type: SnowCoverObsDto
        """

        self._snow_cover_obs = snow_cover_obs

    @property
    def snow_profile(self):
        """Gets the snow_profile of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The snow_profile of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: PictureRequestDto
        """
        return self._snow_profile

    @snow_profile.setter
    def snow_profile(self, snow_profile):
        """Sets the snow_profile of this CreateRegistrationRequestDto.


        :param snow_profile: The snow_profile of this CreateRegistrationRequestDto.  # noqa: E501
        :type: PictureRequestDto
        """

        self._snow_profile = snow_profile

    @property
    def snow_profile2(self):
        """Gets the snow_profile2 of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The snow_profile2 of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: SnowProfileDto
        """
        return self._snow_profile2

    @snow_profile2.setter
    def snow_profile2(self, snow_profile2):
        """Sets the snow_profile2 of this CreateRegistrationRequestDto.


        :param snow_profile2: The snow_profile2 of this CreateRegistrationRequestDto.  # noqa: E501
        :type: SnowProfileDto
        """

        self._snow_profile2 = snow_profile2

    @property
    def snow_surface_observation(self):
        """Gets the snow_surface_observation of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The snow_surface_observation of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: SnowSurfaceObservationDto
        """
        return self._snow_surface_observation

    @snow_surface_observation.setter
    def snow_surface_observation(self, snow_surface_observation):
        """Sets the snow_surface_observation of this CreateRegistrationRequestDto.


        :param snow_surface_observation: The snow_surface_observation of this CreateRegistrationRequestDto.  # noqa: E501
        :type: SnowSurfaceObservationDto
        """

        self._snow_surface_observation = snow_surface_observation

    @property
    def water_level(self):
        """Gets the water_level of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The water_level of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: WaterLevelDto
        """
        return self._water_level

    @water_level.setter
    def water_level(self, water_level):
        """Sets the water_level of this CreateRegistrationRequestDto.


        :param water_level: The water_level of this CreateRegistrationRequestDto.  # noqa: E501
        :type: WaterLevelDto
        """

        self._water_level = water_level

    @property
    def weather_observation(self):
        """Gets the weather_observation of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The weather_observation of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: WeatherObservationDto
        """
        return self._weather_observation

    @weather_observation.setter
    def weather_observation(self, weather_observation):
        """Sets the weather_observation of this CreateRegistrationRequestDto.


        :param weather_observation: The weather_observation of this CreateRegistrationRequestDto.  # noqa: E501
        :type: WeatherObservationDto
        """

        self._weather_observation = weather_observation

    @property
    def water_level2(self):
        """Gets the water_level2 of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The water_level2 of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: WaterLevel2Dto
        """
        return self._water_level2

    @water_level2.setter
    def water_level2(self, water_level2):
        """Sets the water_level2 of this CreateRegistrationRequestDto.


        :param water_level2: The water_level2 of this CreateRegistrationRequestDto.  # noqa: E501
        :type: WaterLevel2Dto
        """

        self._water_level2 = water_level2

    @property
    def damage_obs(self):
        """Gets the damage_obs of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The damage_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: list[DamageObsDto]
        """
        return self._damage_obs

    @damage_obs.setter
    def damage_obs(self, damage_obs):
        """Sets the damage_obs of this CreateRegistrationRequestDto.


        :param damage_obs: The damage_obs of this CreateRegistrationRequestDto.  # noqa: E501
        :type: list[DamageObsDto]
        """

        self._damage_obs = damage_obs

    @property
    def density_profile(self):
        """Gets the density_profile of this CreateRegistrationRequestDto.  # noqa: E501


        :return: The density_profile of this CreateRegistrationRequestDto.  # noqa: E501
        :rtype: DensityProfileDto
        """
        return self._density_profile

    @density_profile.setter
    def density_profile(self, density_profile):
        """Sets the density_profile of this CreateRegistrationRequestDto.


        :param density_profile: The density_profile of this CreateRegistrationRequestDto.  # noqa: E501
        :type: DensityProfileDto
        """

        self._density_profile = density_profile

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
        if issubclass(CreateRegistrationRequestDto, dict):
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
        if not isinstance(other, CreateRegistrationRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other