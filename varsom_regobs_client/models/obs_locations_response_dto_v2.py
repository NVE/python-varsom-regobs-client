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


class ObsLocationsResponseDtoV2(object):
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
        'name': 'str',
        'id': 'int',
        'distance': 'float',
        'lat_lng_object': 'LatLngObject',
        'observer_nick_name': 'str',
        'observer_group_name': 'str',
        'observer_group_id': 'int',
        'geo_hazard_id': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'id': 'Id',
        'distance': 'Distance',
        'lat_lng_object': 'LatLngObject',
        'observer_nick_name': 'ObserverNickName',
        'observer_group_name': 'ObserverGroupName',
        'observer_group_id': 'ObserverGroupId',
        'geo_hazard_id': 'GeoHazardId'
    }

    def __init__(self, name=None, id=None, distance=None, lat_lng_object=None, observer_nick_name=None, observer_group_name=None, observer_group_id=None, geo_hazard_id=None):  # noqa: E501
        """ObsLocationsResponseDtoV2 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._distance = None
        self._lat_lng_object = None
        self._observer_nick_name = None
        self._observer_group_name = None
        self._observer_group_id = None
        self._geo_hazard_id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if distance is not None:
            self.distance = distance
        if lat_lng_object is not None:
            self.lat_lng_object = lat_lng_object
        if observer_nick_name is not None:
            self.observer_nick_name = observer_nick_name
        if observer_group_name is not None:
            self.observer_group_name = observer_group_name
        if observer_group_id is not None:
            self.observer_group_id = observer_group_id
        if geo_hazard_id is not None:
            self.geo_hazard_id = geo_hazard_id

    @property
    def name(self):
        """Gets the name of this ObsLocationsResponseDtoV2.  # noqa: E501


        :return: The name of this ObsLocationsResponseDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObsLocationsResponseDtoV2.


        :param name: The name of this ObsLocationsResponseDtoV2.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this ObsLocationsResponseDtoV2.  # noqa: E501


        :return: The id of this ObsLocationsResponseDtoV2.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObsLocationsResponseDtoV2.


        :param id: The id of this ObsLocationsResponseDtoV2.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def distance(self):
        """Gets the distance of this ObsLocationsResponseDtoV2.  # noqa: E501


        :return: The distance of this ObsLocationsResponseDtoV2.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this ObsLocationsResponseDtoV2.


        :param distance: The distance of this ObsLocationsResponseDtoV2.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def lat_lng_object(self):
        """Gets the lat_lng_object of this ObsLocationsResponseDtoV2.  # noqa: E501


        :return: The lat_lng_object of this ObsLocationsResponseDtoV2.  # noqa: E501
        :rtype: LatLngObject
        """
        return self._lat_lng_object

    @lat_lng_object.setter
    def lat_lng_object(self, lat_lng_object):
        """Sets the lat_lng_object of this ObsLocationsResponseDtoV2.


        :param lat_lng_object: The lat_lng_object of this ObsLocationsResponseDtoV2.  # noqa: E501
        :type: LatLngObject
        """

        self._lat_lng_object = lat_lng_object

    @property
    def observer_nick_name(self):
        """Gets the observer_nick_name of this ObsLocationsResponseDtoV2.  # noqa: E501


        :return: The observer_nick_name of this ObsLocationsResponseDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._observer_nick_name

    @observer_nick_name.setter
    def observer_nick_name(self, observer_nick_name):
        """Sets the observer_nick_name of this ObsLocationsResponseDtoV2.


        :param observer_nick_name: The observer_nick_name of this ObsLocationsResponseDtoV2.  # noqa: E501
        :type: str
        """

        self._observer_nick_name = observer_nick_name

    @property
    def observer_group_name(self):
        """Gets the observer_group_name of this ObsLocationsResponseDtoV2.  # noqa: E501


        :return: The observer_group_name of this ObsLocationsResponseDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._observer_group_name

    @observer_group_name.setter
    def observer_group_name(self, observer_group_name):
        """Sets the observer_group_name of this ObsLocationsResponseDtoV2.


        :param observer_group_name: The observer_group_name of this ObsLocationsResponseDtoV2.  # noqa: E501
        :type: str
        """

        self._observer_group_name = observer_group_name

    @property
    def observer_group_id(self):
        """Gets the observer_group_id of this ObsLocationsResponseDtoV2.  # noqa: E501


        :return: The observer_group_id of this ObsLocationsResponseDtoV2.  # noqa: E501
        :rtype: int
        """
        return self._observer_group_id

    @observer_group_id.setter
    def observer_group_id(self, observer_group_id):
        """Sets the observer_group_id of this ObsLocationsResponseDtoV2.


        :param observer_group_id: The observer_group_id of this ObsLocationsResponseDtoV2.  # noqa: E501
        :type: int
        """

        self._observer_group_id = observer_group_id

    @property
    def geo_hazard_id(self):
        """Gets the geo_hazard_id of this ObsLocationsResponseDtoV2.  # noqa: E501


        :return: The geo_hazard_id of this ObsLocationsResponseDtoV2.  # noqa: E501
        :rtype: int
        """
        return self._geo_hazard_id

    @geo_hazard_id.setter
    def geo_hazard_id(self, geo_hazard_id):
        """Sets the geo_hazard_id of this ObsLocationsResponseDtoV2.


        :param geo_hazard_id: The geo_hazard_id of this ObsLocationsResponseDtoV2.  # noqa: E501
        :type: int
        """

        self._geo_hazard_id = geo_hazard_id

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
        if issubclass(ObsLocationsResponseDtoV2, dict):
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
        if not isinstance(other, ObsLocationsResponseDtoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
