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


class WaterLevelViewModel(object):
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
        'water_level_described': 'str',
        'water_level_value': 'float',
        'water_level_ref_tid': 'int',
        'water_level_ref_name': 'str',
        'comment': 'str',
        'measured_discharge': 'float',
        'is_river': 'bool'
    }

    attribute_map = {
        'water_level_described': 'WaterLevelDescribed',
        'water_level_value': 'WaterLevelValue',
        'water_level_ref_tid': 'WaterLevelRefTID',
        'water_level_ref_name': 'WaterLevelRefName',
        'comment': 'Comment',
        'measured_discharge': 'MeasuredDischarge',
        'is_river': 'IsRiver'
    }

    def __init__(self, water_level_described=None, water_level_value=None, water_level_ref_tid=None, water_level_ref_name=None, comment=None, measured_discharge=None, is_river=None):  # noqa: E501
        """WaterLevelViewModel - a model defined in Swagger"""  # noqa: E501
        self._water_level_described = None
        self._water_level_value = None
        self._water_level_ref_tid = None
        self._water_level_ref_name = None
        self._comment = None
        self._measured_discharge = None
        self._is_river = None
        self.discriminator = None
        if water_level_described is not None:
            self.water_level_described = water_level_described
        if water_level_value is not None:
            self.water_level_value = water_level_value
        if water_level_ref_tid is not None:
            self.water_level_ref_tid = water_level_ref_tid
        if water_level_ref_name is not None:
            self.water_level_ref_name = water_level_ref_name
        if comment is not None:
            self.comment = comment
        if measured_discharge is not None:
            self.measured_discharge = measured_discharge
        if is_river is not None:
            self.is_river = is_river

    @property
    def water_level_described(self):
        """Gets the water_level_described of this WaterLevelViewModel.  # noqa: E501


        :return: The water_level_described of this WaterLevelViewModel.  # noqa: E501
        :rtype: str
        """
        return self._water_level_described

    @water_level_described.setter
    def water_level_described(self, water_level_described):
        """Sets the water_level_described of this WaterLevelViewModel.


        :param water_level_described: The water_level_described of this WaterLevelViewModel.  # noqa: E501
        :type: str
        """

        self._water_level_described = water_level_described

    @property
    def water_level_value(self):
        """Gets the water_level_value of this WaterLevelViewModel.  # noqa: E501


        :return: The water_level_value of this WaterLevelViewModel.  # noqa: E501
        :rtype: float
        """
        return self._water_level_value

    @water_level_value.setter
    def water_level_value(self, water_level_value):
        """Sets the water_level_value of this WaterLevelViewModel.


        :param water_level_value: The water_level_value of this WaterLevelViewModel.  # noqa: E501
        :type: float
        """

        self._water_level_value = water_level_value

    @property
    def water_level_ref_tid(self):
        """Gets the water_level_ref_tid of this WaterLevelViewModel.  # noqa: E501


        :return: The water_level_ref_tid of this WaterLevelViewModel.  # noqa: E501
        :rtype: int
        """
        return self._water_level_ref_tid

    @water_level_ref_tid.setter
    def water_level_ref_tid(self, water_level_ref_tid):
        """Sets the water_level_ref_tid of this WaterLevelViewModel.


        :param water_level_ref_tid: The water_level_ref_tid of this WaterLevelViewModel.  # noqa: E501
        :type: int
        """

        self._water_level_ref_tid = water_level_ref_tid

    @property
    def water_level_ref_name(self):
        """Gets the water_level_ref_name of this WaterLevelViewModel.  # noqa: E501


        :return: The water_level_ref_name of this WaterLevelViewModel.  # noqa: E501
        :rtype: str
        """
        return self._water_level_ref_name

    @water_level_ref_name.setter
    def water_level_ref_name(self, water_level_ref_name):
        """Sets the water_level_ref_name of this WaterLevelViewModel.


        :param water_level_ref_name: The water_level_ref_name of this WaterLevelViewModel.  # noqa: E501
        :type: str
        """

        self._water_level_ref_name = water_level_ref_name

    @property
    def comment(self):
        """Gets the comment of this WaterLevelViewModel.  # noqa: E501


        :return: The comment of this WaterLevelViewModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this WaterLevelViewModel.


        :param comment: The comment of this WaterLevelViewModel.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def measured_discharge(self):
        """Gets the measured_discharge of this WaterLevelViewModel.  # noqa: E501


        :return: The measured_discharge of this WaterLevelViewModel.  # noqa: E501
        :rtype: float
        """
        return self._measured_discharge

    @measured_discharge.setter
    def measured_discharge(self, measured_discharge):
        """Sets the measured_discharge of this WaterLevelViewModel.


        :param measured_discharge: The measured_discharge of this WaterLevelViewModel.  # noqa: E501
        :type: float
        """

        self._measured_discharge = measured_discharge

    @property
    def is_river(self):
        """Gets the is_river of this WaterLevelViewModel.  # noqa: E501


        :return: The is_river of this WaterLevelViewModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_river

    @is_river.setter
    def is_river(self, is_river):
        """Sets the is_river of this WaterLevelViewModel.


        :param is_river: The is_river of this WaterLevelViewModel.  # noqa: E501
        :type: bool
        """

        self._is_river = is_river

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
        if issubclass(WaterLevelViewModel, dict):
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
        if not isinstance(other, WaterLevelViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
