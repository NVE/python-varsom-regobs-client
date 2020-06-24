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


class StratProfileLayerDto(object):
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
        'sort_order': 'int',
        'thickness': 'float',
        'hardness_tid': 'int',
        'grain_form_primary_tid': 'int',
        'grain_form_secondary_tid': 'int',
        'grain_size_avg': 'float',
        'grain_size_avg_max': 'float',
        'hardness_bottom_tid': 'int',
        'wetness_tid': 'int',
        'critical_layer_tid': 'int',
        'comment': 'str'
    }

    attribute_map = {
        'sort_order': 'SortOrder',
        'thickness': 'Thickness',
        'hardness_tid': 'HardnessTID',
        'grain_form_primary_tid': 'GrainFormPrimaryTID',
        'grain_form_secondary_tid': 'GrainFormSecondaryTID',
        'grain_size_avg': 'GrainSizeAvg',
        'grain_size_avg_max': 'GrainSizeAvgMax',
        'hardness_bottom_tid': 'HardnessBottomTID',
        'wetness_tid': 'WetnessTID',
        'critical_layer_tid': 'CriticalLayerTID',
        'comment': 'Comment'
    }

    def __init__(self, sort_order=None, thickness=None, hardness_tid=None, grain_form_primary_tid=None, grain_form_secondary_tid=None, grain_size_avg=None, grain_size_avg_max=None, hardness_bottom_tid=None, wetness_tid=None, critical_layer_tid=None, comment=None):  # noqa: E501
        """StratProfileLayerDto - a model defined in Swagger"""  # noqa: E501
        self._sort_order = None
        self._thickness = None
        self._hardness_tid = None
        self._grain_form_primary_tid = None
        self._grain_form_secondary_tid = None
        self._grain_size_avg = None
        self._grain_size_avg_max = None
        self._hardness_bottom_tid = None
        self._wetness_tid = None
        self._critical_layer_tid = None
        self._comment = None
        self.discriminator = None
        if sort_order is not None:
            self.sort_order = sort_order
        if thickness is not None:
            self.thickness = thickness
        if hardness_tid is not None:
            self.hardness_tid = hardness_tid
        if grain_form_primary_tid is not None:
            self.grain_form_primary_tid = grain_form_primary_tid
        if grain_form_secondary_tid is not None:
            self.grain_form_secondary_tid = grain_form_secondary_tid
        if grain_size_avg is not None:
            self.grain_size_avg = grain_size_avg
        if grain_size_avg_max is not None:
            self.grain_size_avg_max = grain_size_avg_max
        if hardness_bottom_tid is not None:
            self.hardness_bottom_tid = hardness_bottom_tid
        if wetness_tid is not None:
            self.wetness_tid = wetness_tid
        if critical_layer_tid is not None:
            self.critical_layer_tid = critical_layer_tid
        if comment is not None:
            self.comment = comment

    @property
    def sort_order(self):
        """Gets the sort_order of this StratProfileLayerDto.  # noqa: E501


        :return: The sort_order of this StratProfileLayerDto.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this StratProfileLayerDto.


        :param sort_order: The sort_order of this StratProfileLayerDto.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def thickness(self):
        """Gets the thickness of this StratProfileLayerDto.  # noqa: E501


        :return: The thickness of this StratProfileLayerDto.  # noqa: E501
        :rtype: float
        """
        return self._thickness

    @thickness.setter
    def thickness(self, thickness):
        """Sets the thickness of this StratProfileLayerDto.


        :param thickness: The thickness of this StratProfileLayerDto.  # noqa: E501
        :type: float
        """

        self._thickness = thickness

    @property
    def hardness_tid(self):
        """Gets the hardness_tid of this StratProfileLayerDto.  # noqa: E501


        :return: The hardness_tid of this StratProfileLayerDto.  # noqa: E501
        :rtype: int
        """
        return self._hardness_tid

    @hardness_tid.setter
    def hardness_tid(self, hardness_tid):
        """Sets the hardness_tid of this StratProfileLayerDto.


        :param hardness_tid: The hardness_tid of this StratProfileLayerDto.  # noqa: E501
        :type: int
        """

        self._hardness_tid = hardness_tid

    @property
    def grain_form_primary_tid(self):
        """Gets the grain_form_primary_tid of this StratProfileLayerDto.  # noqa: E501


        :return: The grain_form_primary_tid of this StratProfileLayerDto.  # noqa: E501
        :rtype: int
        """
        return self._grain_form_primary_tid

    @grain_form_primary_tid.setter
    def grain_form_primary_tid(self, grain_form_primary_tid):
        """Sets the grain_form_primary_tid of this StratProfileLayerDto.


        :param grain_form_primary_tid: The grain_form_primary_tid of this StratProfileLayerDto.  # noqa: E501
        :type: int
        """

        self._grain_form_primary_tid = grain_form_primary_tid

    @property
    def grain_form_secondary_tid(self):
        """Gets the grain_form_secondary_tid of this StratProfileLayerDto.  # noqa: E501


        :return: The grain_form_secondary_tid of this StratProfileLayerDto.  # noqa: E501
        :rtype: int
        """
        return self._grain_form_secondary_tid

    @grain_form_secondary_tid.setter
    def grain_form_secondary_tid(self, grain_form_secondary_tid):
        """Sets the grain_form_secondary_tid of this StratProfileLayerDto.


        :param grain_form_secondary_tid: The grain_form_secondary_tid of this StratProfileLayerDto.  # noqa: E501
        :type: int
        """

        self._grain_form_secondary_tid = grain_form_secondary_tid

    @property
    def grain_size_avg(self):
        """Gets the grain_size_avg of this StratProfileLayerDto.  # noqa: E501


        :return: The grain_size_avg of this StratProfileLayerDto.  # noqa: E501
        :rtype: float
        """
        return self._grain_size_avg

    @grain_size_avg.setter
    def grain_size_avg(self, grain_size_avg):
        """Sets the grain_size_avg of this StratProfileLayerDto.


        :param grain_size_avg: The grain_size_avg of this StratProfileLayerDto.  # noqa: E501
        :type: float
        """

        self._grain_size_avg = grain_size_avg

    @property
    def grain_size_avg_max(self):
        """Gets the grain_size_avg_max of this StratProfileLayerDto.  # noqa: E501


        :return: The grain_size_avg_max of this StratProfileLayerDto.  # noqa: E501
        :rtype: float
        """
        return self._grain_size_avg_max

    @grain_size_avg_max.setter
    def grain_size_avg_max(self, grain_size_avg_max):
        """Sets the grain_size_avg_max of this StratProfileLayerDto.


        :param grain_size_avg_max: The grain_size_avg_max of this StratProfileLayerDto.  # noqa: E501
        :type: float
        """

        self._grain_size_avg_max = grain_size_avg_max

    @property
    def hardness_bottom_tid(self):
        """Gets the hardness_bottom_tid of this StratProfileLayerDto.  # noqa: E501


        :return: The hardness_bottom_tid of this StratProfileLayerDto.  # noqa: E501
        :rtype: int
        """
        return self._hardness_bottom_tid

    @hardness_bottom_tid.setter
    def hardness_bottom_tid(self, hardness_bottom_tid):
        """Sets the hardness_bottom_tid of this StratProfileLayerDto.


        :param hardness_bottom_tid: The hardness_bottom_tid of this StratProfileLayerDto.  # noqa: E501
        :type: int
        """

        self._hardness_bottom_tid = hardness_bottom_tid

    @property
    def wetness_tid(self):
        """Gets the wetness_tid of this StratProfileLayerDto.  # noqa: E501


        :return: The wetness_tid of this StratProfileLayerDto.  # noqa: E501
        :rtype: int
        """
        return self._wetness_tid

    @wetness_tid.setter
    def wetness_tid(self, wetness_tid):
        """Sets the wetness_tid of this StratProfileLayerDto.


        :param wetness_tid: The wetness_tid of this StratProfileLayerDto.  # noqa: E501
        :type: int
        """

        self._wetness_tid = wetness_tid

    @property
    def critical_layer_tid(self):
        """Gets the critical_layer_tid of this StratProfileLayerDto.  # noqa: E501


        :return: The critical_layer_tid of this StratProfileLayerDto.  # noqa: E501
        :rtype: int
        """
        return self._critical_layer_tid

    @critical_layer_tid.setter
    def critical_layer_tid(self, critical_layer_tid):
        """Sets the critical_layer_tid of this StratProfileLayerDto.


        :param critical_layer_tid: The critical_layer_tid of this StratProfileLayerDto.  # noqa: E501
        :type: int
        """

        self._critical_layer_tid = critical_layer_tid

    @property
    def comment(self):
        """Gets the comment of this StratProfileLayerDto.  # noqa: E501


        :return: The comment of this StratProfileLayerDto.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this StratProfileLayerDto.


        :param comment: The comment of this StratProfileLayerDto.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(StratProfileLayerDto, dict):
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
        if not isinstance(other, StratProfileLayerDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
