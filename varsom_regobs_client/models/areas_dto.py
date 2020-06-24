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


class AreasDto(object):
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
        'country_id': 'int',
        'country_name': 'str',
        'country_description': 'str',
        'sort_order': 'int',
        'forecast_regions': 'object',
        'counties': 'list[CountyDto]'
    }

    attribute_map = {
        'country_id': 'CountryId',
        'country_name': 'CountryName',
        'country_description': 'CountryDescription',
        'sort_order': 'SortOrder',
        'forecast_regions': 'ForecastRegions',
        'counties': 'Counties'
    }

    def __init__(self, country_id=None, country_name=None, country_description=None, sort_order=None, forecast_regions=None, counties=None):  # noqa: E501
        """AreasDto - a model defined in Swagger"""  # noqa: E501
        self._country_id = None
        self._country_name = None
        self._country_description = None
        self._sort_order = None
        self._forecast_regions = None
        self._counties = None
        self.discriminator = None
        if country_id is not None:
            self.country_id = country_id
        if country_name is not None:
            self.country_name = country_name
        if country_description is not None:
            self.country_description = country_description
        if sort_order is not None:
            self.sort_order = sort_order
        if forecast_regions is not None:
            self.forecast_regions = forecast_regions
        if counties is not None:
            self.counties = counties

    @property
    def country_id(self):
        """Gets the country_id of this AreasDto.  # noqa: E501


        :return: The country_id of this AreasDto.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this AreasDto.


        :param country_id: The country_id of this AreasDto.  # noqa: E501
        :type: int
        """

        self._country_id = country_id

    @property
    def country_name(self):
        """Gets the country_name of this AreasDto.  # noqa: E501


        :return: The country_name of this AreasDto.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this AreasDto.


        :param country_name: The country_name of this AreasDto.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def country_description(self):
        """Gets the country_description of this AreasDto.  # noqa: E501


        :return: The country_description of this AreasDto.  # noqa: E501
        :rtype: str
        """
        return self._country_description

    @country_description.setter
    def country_description(self, country_description):
        """Sets the country_description of this AreasDto.


        :param country_description: The country_description of this AreasDto.  # noqa: E501
        :type: str
        """

        self._country_description = country_description

    @property
    def sort_order(self):
        """Gets the sort_order of this AreasDto.  # noqa: E501


        :return: The sort_order of this AreasDto.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this AreasDto.


        :param sort_order: The sort_order of this AreasDto.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def forecast_regions(self):
        """Gets the forecast_regions of this AreasDto.  # noqa: E501


        :return: The forecast_regions of this AreasDto.  # noqa: E501
        :rtype: object
        """
        return self._forecast_regions

    @forecast_regions.setter
    def forecast_regions(self, forecast_regions):
        """Sets the forecast_regions of this AreasDto.


        :param forecast_regions: The forecast_regions of this AreasDto.  # noqa: E501
        :type: object
        """

        self._forecast_regions = forecast_regions

    @property
    def counties(self):
        """Gets the counties of this AreasDto.  # noqa: E501


        :return: The counties of this AreasDto.  # noqa: E501
        :rtype: list[CountyDto]
        """
        return self._counties

    @counties.setter
    def counties(self, counties):
        """Sets the counties of this AreasDto.


        :param counties: The counties of this AreasDto.  # noqa: E501
        :type: list[CountyDto]
        """

        self._counties = counties

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
        if issubclass(AreasDto, dict):
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
        if not isinstance(other, AreasDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other