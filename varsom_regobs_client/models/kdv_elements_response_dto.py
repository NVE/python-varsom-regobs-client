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


class KdvElementsResponseDto(object):
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
        'kdv_repositories': 'dict(str, list[KdvElement])',
        'view_repositories': 'object'
    }

    attribute_map = {
        'kdv_repositories': 'KdvRepositories',
        'view_repositories': 'ViewRepositories'
    }

    def __init__(self, kdv_repositories=None, view_repositories=None):  # noqa: E501
        """KdvElementsResponseDto - a model defined in Swagger"""  # noqa: E501
        self._kdv_repositories = None
        self._view_repositories = None
        self.discriminator = None
        if kdv_repositories is not None:
            self.kdv_repositories = kdv_repositories
        if view_repositories is not None:
            self.view_repositories = view_repositories

    @property
    def kdv_repositories(self):
        """Gets the kdv_repositories of this KdvElementsResponseDto.  # noqa: E501


        :return: The kdv_repositories of this KdvElementsResponseDto.  # noqa: E501
        :rtype: dict(str, list[KdvElement])
        """
        return self._kdv_repositories

    @kdv_repositories.setter
    def kdv_repositories(self, kdv_repositories):
        """Sets the kdv_repositories of this KdvElementsResponseDto.


        :param kdv_repositories: The kdv_repositories of this KdvElementsResponseDto.  # noqa: E501
        :type: dict(str, list[KdvElement])
        """

        self._kdv_repositories = kdv_repositories

    @property
    def view_repositories(self):
        """Gets the view_repositories of this KdvElementsResponseDto.  # noqa: E501


        :return: The view_repositories of this KdvElementsResponseDto.  # noqa: E501
        :rtype: object
        """
        return self._view_repositories

    @view_repositories.setter
    def view_repositories(self, view_repositories):
        """Sets the view_repositories of this KdvElementsResponseDto.


        :param view_repositories: The view_repositories of this KdvElementsResponseDto.  # noqa: E501
        :type: object
        """

        self._view_repositories = view_repositories

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
        if issubclass(KdvElementsResponseDto, dict):
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
        if not isinstance(other, KdvElementsResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
