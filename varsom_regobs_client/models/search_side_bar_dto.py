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


class SearchSideBarDto(object):
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
        'registration_types': 'object',
        'observer_competence_levels': 'object',
        'areas': 'list[AreasDto]'
    }

    attribute_map = {
        'registration_types': 'RegistrationTypes',
        'observer_competence_levels': 'ObserverCompetenceLevels',
        'areas': 'Areas'
    }

    def __init__(self, registration_types=None, observer_competence_levels=None, areas=None):  # noqa: E501
        """SearchSideBarDto - a model defined in Swagger"""  # noqa: E501
        self._registration_types = None
        self._observer_competence_levels = None
        self._areas = None
        self.discriminator = None
        if registration_types is not None:
            self.registration_types = registration_types
        if observer_competence_levels is not None:
            self.observer_competence_levels = observer_competence_levels
        if areas is not None:
            self.areas = areas

    @property
    def registration_types(self):
        """Gets the registration_types of this SearchSideBarDto.  # noqa: E501


        :return: The registration_types of this SearchSideBarDto.  # noqa: E501
        :rtype: object
        """
        return self._registration_types

    @registration_types.setter
    def registration_types(self, registration_types):
        """Sets the registration_types of this SearchSideBarDto.


        :param registration_types: The registration_types of this SearchSideBarDto.  # noqa: E501
        :type: object
        """

        self._registration_types = registration_types

    @property
    def observer_competence_levels(self):
        """Gets the observer_competence_levels of this SearchSideBarDto.  # noqa: E501


        :return: The observer_competence_levels of this SearchSideBarDto.  # noqa: E501
        :rtype: object
        """
        return self._observer_competence_levels

    @observer_competence_levels.setter
    def observer_competence_levels(self, observer_competence_levels):
        """Sets the observer_competence_levels of this SearchSideBarDto.


        :param observer_competence_levels: The observer_competence_levels of this SearchSideBarDto.  # noqa: E501
        :type: object
        """

        self._observer_competence_levels = observer_competence_levels

    @property
    def areas(self):
        """Gets the areas of this SearchSideBarDto.  # noqa: E501


        :return: The areas of this SearchSideBarDto.  # noqa: E501
        :rtype: list[AreasDto]
        """
        return self._areas

    @areas.setter
    def areas(self, areas):
        """Sets the areas of this SearchSideBarDto.


        :param areas: The areas of this SearchSideBarDto.  # noqa: E501
        :type: list[AreasDto]
        """

        self._areas = areas

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
        if issubclass(SearchSideBarDto, dict):
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
        if not isinstance(other, SearchSideBarDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other