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


class IncidentUrlsDto(object):
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
        'url_description': 'str',
        'url_line': 'str'
    }

    attribute_map = {
        'url_description': 'UrlDescription',
        'url_line': 'UrlLine'
    }

    def __init__(self, url_description=None, url_line=None):  # noqa: E501
        """IncidentUrlsDto - a model defined in Swagger"""  # noqa: E501
        self._url_description = None
        self._url_line = None
        self.discriminator = None
        if url_description is not None:
            self.url_description = url_description
        if url_line is not None:
            self.url_line = url_line

    @property
    def url_description(self):
        """Gets the url_description of this IncidentUrlsDto.  # noqa: E501

        UrlDescription  # noqa: E501

        :return: The url_description of this IncidentUrlsDto.  # noqa: E501
        :rtype: str
        """
        return self._url_description

    @url_description.setter
    def url_description(self, url_description):
        """Sets the url_description of this IncidentUrlsDto.

        UrlDescription  # noqa: E501

        :param url_description: The url_description of this IncidentUrlsDto.  # noqa: E501
        :type: str
        """

        self._url_description = url_description

    @property
    def url_line(self):
        """Gets the url_line of this IncidentUrlsDto.  # noqa: E501

        UrlLine  # noqa: E501

        :return: The url_line of this IncidentUrlsDto.  # noqa: E501
        :rtype: str
        """
        return self._url_line

    @url_line.setter
    def url_line(self, url_line):
        """Sets the url_line of this IncidentUrlsDto.

        UrlLine  # noqa: E501

        :param url_line: The url_line of this IncidentUrlsDto.  # noqa: E501
        :type: str
        """

        self._url_line = url_line

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
        if issubclass(IncidentUrlsDto, dict):
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
        if not isinstance(other, IncidentUrlsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
