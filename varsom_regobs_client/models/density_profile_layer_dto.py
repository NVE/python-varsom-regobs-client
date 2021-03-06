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


class DensityProfileLayerDto(object):
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
        'depth': 'float',
        'thickness': 'float',
        'density': 'float',
        'weight': 'float',
        'comment': 'str',
        'sort_order': 'int'
    }

    attribute_map = {
        'depth': 'Depth',
        'thickness': 'Thickness',
        'density': 'Density',
        'weight': 'Weight',
        'comment': 'Comment',
        'sort_order': 'SortOrder'
    }

    def __init__(self, depth=None, thickness=None, density=None, weight=None, comment=None, sort_order=None):  # noqa: E501
        """DensityProfileLayerDto - a model defined in Swagger"""  # noqa: E501
        self._depth = None
        self._thickness = None
        self._density = None
        self._weight = None
        self._comment = None
        self._sort_order = None
        self.discriminator = None
        if depth is not None:
            self.depth = depth
        if thickness is not None:
            self.thickness = thickness
        if density is not None:
            self.density = density
        if weight is not None:
            self.weight = weight
        if comment is not None:
            self.comment = comment
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def depth(self):
        """Gets the depth of this DensityProfileLayerDto.  # noqa: E501


        :return: The depth of this DensityProfileLayerDto.  # noqa: E501
        :rtype: float
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this DensityProfileLayerDto.


        :param depth: The depth of this DensityProfileLayerDto.  # noqa: E501
        :type: float
        """

        self._depth = depth

    @property
    def thickness(self):
        """Gets the thickness of this DensityProfileLayerDto.  # noqa: E501

        thickness in m  # noqa: E501

        :return: The thickness of this DensityProfileLayerDto.  # noqa: E501
        :rtype: float
        """
        return self._thickness

    @thickness.setter
    def thickness(self, thickness):
        """Sets the thickness of this DensityProfileLayerDto.

        thickness in m  # noqa: E501

        :param thickness: The thickness of this DensityProfileLayerDto.  # noqa: E501
        :type: float
        """

        self._thickness = thickness

    @property
    def density(self):
        """Gets the density of this DensityProfileLayerDto.  # noqa: E501

        Density in kg/m^3  # noqa: E501

        :return: The density of this DensityProfileLayerDto.  # noqa: E501
        :rtype: float
        """
        return self._density

    @density.setter
    def density(self, density):
        """Sets the density of this DensityProfileLayerDto.

        Density in kg/m^3  # noqa: E501

        :param density: The density of this DensityProfileLayerDto.  # noqa: E501
        :type: float
        """

        self._density = density

    @property
    def weight(self):
        """Gets the weight of this DensityProfileLayerDto.  # noqa: E501

        Weight in KG  # noqa: E501

        :return: The weight of this DensityProfileLayerDto.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this DensityProfileLayerDto.

        Weight in KG  # noqa: E501

        :param weight: The weight of this DensityProfileLayerDto.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def comment(self):
        """Gets the comment of this DensityProfileLayerDto.  # noqa: E501


        :return: The comment of this DensityProfileLayerDto.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this DensityProfileLayerDto.


        :param comment: The comment of this DensityProfileLayerDto.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def sort_order(self):
        """Gets the sort_order of this DensityProfileLayerDto.  # noqa: E501


        :return: The sort_order of this DensityProfileLayerDto.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this DensityProfileLayerDto.


        :param sort_order: The sort_order of this DensityProfileLayerDto.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

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
        if issubclass(DensityProfileLayerDto, dict):
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
        if not isinstance(other, DensityProfileLayerDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
