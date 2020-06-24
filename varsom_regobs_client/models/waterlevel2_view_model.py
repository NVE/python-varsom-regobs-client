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


class Waterlevel2ViewModel(object):
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
        'water_level_state_name': 'str',
        'water_astray_name': 'str',
        'observation_timing_name': 'str',
        'measurement_reference_name': 'str',
        'measurement_type_name': 'str',
        'water_level_method_name': 'str',
        'marking_reference_name': 'str',
        'water_astray_tid': 'int',
        'observation_timing_tid': 'int',
        'measurement_reference_tid': 'int',
        'measurement_type_tid': 'int',
        'water_level_method_tid': 'int',
        'marking_reference_tid': 'int',
        'water_level_state_tid': 'int',
        'marking_type_tid': 'int',
        'marking_type_name': 'str',
        'measuring_tool_description': 'str',
        'water_level_measurement': 'list[WaterLevelMeasurementViewModel]',
        'comment': 'str'
    }

    attribute_map = {
        'water_level_state_name': 'WaterLevelStateName',
        'water_astray_name': 'WaterAstrayName',
        'observation_timing_name': 'ObservationTimingName',
        'measurement_reference_name': 'MeasurementReferenceName',
        'measurement_type_name': 'MeasurementTypeName',
        'water_level_method_name': 'WaterLevelMethodName',
        'marking_reference_name': 'MarkingReferenceName',
        'water_astray_tid': 'WaterAstrayTID',
        'observation_timing_tid': 'ObservationTimingTID',
        'measurement_reference_tid': 'MeasurementReferenceTID',
        'measurement_type_tid': 'MeasurementTypeTID',
        'water_level_method_tid': 'WaterLevelMethodTID',
        'marking_reference_tid': 'MarkingReferenceTID',
        'water_level_state_tid': 'WaterLevelStateTID',
        'marking_type_tid': 'MarkingTypeTID',
        'marking_type_name': 'MarkingTypeName',
        'measuring_tool_description': 'MeasuringToolDescription',
        'water_level_measurement': 'WaterLevelMeasurement',
        'comment': 'Comment'
    }

    def __init__(self, water_level_state_name=None, water_astray_name=None, observation_timing_name=None, measurement_reference_name=None, measurement_type_name=None, water_level_method_name=None, marking_reference_name=None, water_astray_tid=None, observation_timing_tid=None, measurement_reference_tid=None, measurement_type_tid=None, water_level_method_tid=None, marking_reference_tid=None, water_level_state_tid=None, marking_type_tid=None, marking_type_name=None, measuring_tool_description=None, water_level_measurement=None, comment=None):  # noqa: E501
        """Waterlevel2ViewModel - a model defined in Swagger"""  # noqa: E501
        self._water_level_state_name = None
        self._water_astray_name = None
        self._observation_timing_name = None
        self._measurement_reference_name = None
        self._measurement_type_name = None
        self._water_level_method_name = None
        self._marking_reference_name = None
        self._water_astray_tid = None
        self._observation_timing_tid = None
        self._measurement_reference_tid = None
        self._measurement_type_tid = None
        self._water_level_method_tid = None
        self._marking_reference_tid = None
        self._water_level_state_tid = None
        self._marking_type_tid = None
        self._marking_type_name = None
        self._measuring_tool_description = None
        self._water_level_measurement = None
        self._comment = None
        self.discriminator = None
        if water_level_state_name is not None:
            self.water_level_state_name = water_level_state_name
        if water_astray_name is not None:
            self.water_astray_name = water_astray_name
        if observation_timing_name is not None:
            self.observation_timing_name = observation_timing_name
        if measurement_reference_name is not None:
            self.measurement_reference_name = measurement_reference_name
        if measurement_type_name is not None:
            self.measurement_type_name = measurement_type_name
        if water_level_method_name is not None:
            self.water_level_method_name = water_level_method_name
        if marking_reference_name is not None:
            self.marking_reference_name = marking_reference_name
        if water_astray_tid is not None:
            self.water_astray_tid = water_astray_tid
        if observation_timing_tid is not None:
            self.observation_timing_tid = observation_timing_tid
        if measurement_reference_tid is not None:
            self.measurement_reference_tid = measurement_reference_tid
        if measurement_type_tid is not None:
            self.measurement_type_tid = measurement_type_tid
        if water_level_method_tid is not None:
            self.water_level_method_tid = water_level_method_tid
        if marking_reference_tid is not None:
            self.marking_reference_tid = marking_reference_tid
        if water_level_state_tid is not None:
            self.water_level_state_tid = water_level_state_tid
        if marking_type_tid is not None:
            self.marking_type_tid = marking_type_tid
        if marking_type_name is not None:
            self.marking_type_name = marking_type_name
        if measuring_tool_description is not None:
            self.measuring_tool_description = measuring_tool_description
        if water_level_measurement is not None:
            self.water_level_measurement = water_level_measurement
        if comment is not None:
            self.comment = comment

    @property
    def water_level_state_name(self):
        """Gets the water_level_state_name of this Waterlevel2ViewModel.  # noqa: E501


        :return: The water_level_state_name of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._water_level_state_name

    @water_level_state_name.setter
    def water_level_state_name(self, water_level_state_name):
        """Sets the water_level_state_name of this Waterlevel2ViewModel.


        :param water_level_state_name: The water_level_state_name of this Waterlevel2ViewModel.  # noqa: E501
        :type: str
        """

        self._water_level_state_name = water_level_state_name

    @property
    def water_astray_name(self):
        """Gets the water_astray_name of this Waterlevel2ViewModel.  # noqa: E501


        :return: The water_astray_name of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._water_astray_name

    @water_astray_name.setter
    def water_astray_name(self, water_astray_name):
        """Sets the water_astray_name of this Waterlevel2ViewModel.


        :param water_astray_name: The water_astray_name of this Waterlevel2ViewModel.  # noqa: E501
        :type: str
        """

        self._water_astray_name = water_astray_name

    @property
    def observation_timing_name(self):
        """Gets the observation_timing_name of this Waterlevel2ViewModel.  # noqa: E501


        :return: The observation_timing_name of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._observation_timing_name

    @observation_timing_name.setter
    def observation_timing_name(self, observation_timing_name):
        """Sets the observation_timing_name of this Waterlevel2ViewModel.


        :param observation_timing_name: The observation_timing_name of this Waterlevel2ViewModel.  # noqa: E501
        :type: str
        """

        self._observation_timing_name = observation_timing_name

    @property
    def measurement_reference_name(self):
        """Gets the measurement_reference_name of this Waterlevel2ViewModel.  # noqa: E501


        :return: The measurement_reference_name of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._measurement_reference_name

    @measurement_reference_name.setter
    def measurement_reference_name(self, measurement_reference_name):
        """Sets the measurement_reference_name of this Waterlevel2ViewModel.


        :param measurement_reference_name: The measurement_reference_name of this Waterlevel2ViewModel.  # noqa: E501
        :type: str
        """

        self._measurement_reference_name = measurement_reference_name

    @property
    def measurement_type_name(self):
        """Gets the measurement_type_name of this Waterlevel2ViewModel.  # noqa: E501


        :return: The measurement_type_name of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._measurement_type_name

    @measurement_type_name.setter
    def measurement_type_name(self, measurement_type_name):
        """Sets the measurement_type_name of this Waterlevel2ViewModel.


        :param measurement_type_name: The measurement_type_name of this Waterlevel2ViewModel.  # noqa: E501
        :type: str
        """

        self._measurement_type_name = measurement_type_name

    @property
    def water_level_method_name(self):
        """Gets the water_level_method_name of this Waterlevel2ViewModel.  # noqa: E501


        :return: The water_level_method_name of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._water_level_method_name

    @water_level_method_name.setter
    def water_level_method_name(self, water_level_method_name):
        """Sets the water_level_method_name of this Waterlevel2ViewModel.


        :param water_level_method_name: The water_level_method_name of this Waterlevel2ViewModel.  # noqa: E501
        :type: str
        """

        self._water_level_method_name = water_level_method_name

    @property
    def marking_reference_name(self):
        """Gets the marking_reference_name of this Waterlevel2ViewModel.  # noqa: E501


        :return: The marking_reference_name of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._marking_reference_name

    @marking_reference_name.setter
    def marking_reference_name(self, marking_reference_name):
        """Sets the marking_reference_name of this Waterlevel2ViewModel.


        :param marking_reference_name: The marking_reference_name of this Waterlevel2ViewModel.  # noqa: E501
        :type: str
        """

        self._marking_reference_name = marking_reference_name

    @property
    def water_astray_tid(self):
        """Gets the water_astray_tid of this Waterlevel2ViewModel.  # noqa: E501


        :return: The water_astray_tid of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._water_astray_tid

    @water_astray_tid.setter
    def water_astray_tid(self, water_astray_tid):
        """Sets the water_astray_tid of this Waterlevel2ViewModel.


        :param water_astray_tid: The water_astray_tid of this Waterlevel2ViewModel.  # noqa: E501
        :type: int
        """

        self._water_astray_tid = water_astray_tid

    @property
    def observation_timing_tid(self):
        """Gets the observation_timing_tid of this Waterlevel2ViewModel.  # noqa: E501


        :return: The observation_timing_tid of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._observation_timing_tid

    @observation_timing_tid.setter
    def observation_timing_tid(self, observation_timing_tid):
        """Sets the observation_timing_tid of this Waterlevel2ViewModel.


        :param observation_timing_tid: The observation_timing_tid of this Waterlevel2ViewModel.  # noqa: E501
        :type: int
        """

        self._observation_timing_tid = observation_timing_tid

    @property
    def measurement_reference_tid(self):
        """Gets the measurement_reference_tid of this Waterlevel2ViewModel.  # noqa: E501


        :return: The measurement_reference_tid of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._measurement_reference_tid

    @measurement_reference_tid.setter
    def measurement_reference_tid(self, measurement_reference_tid):
        """Sets the measurement_reference_tid of this Waterlevel2ViewModel.


        :param measurement_reference_tid: The measurement_reference_tid of this Waterlevel2ViewModel.  # noqa: E501
        :type: int
        """

        self._measurement_reference_tid = measurement_reference_tid

    @property
    def measurement_type_tid(self):
        """Gets the measurement_type_tid of this Waterlevel2ViewModel.  # noqa: E501


        :return: The measurement_type_tid of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._measurement_type_tid

    @measurement_type_tid.setter
    def measurement_type_tid(self, measurement_type_tid):
        """Sets the measurement_type_tid of this Waterlevel2ViewModel.


        :param measurement_type_tid: The measurement_type_tid of this Waterlevel2ViewModel.  # noqa: E501
        :type: int
        """

        self._measurement_type_tid = measurement_type_tid

    @property
    def water_level_method_tid(self):
        """Gets the water_level_method_tid of this Waterlevel2ViewModel.  # noqa: E501


        :return: The water_level_method_tid of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._water_level_method_tid

    @water_level_method_tid.setter
    def water_level_method_tid(self, water_level_method_tid):
        """Sets the water_level_method_tid of this Waterlevel2ViewModel.


        :param water_level_method_tid: The water_level_method_tid of this Waterlevel2ViewModel.  # noqa: E501
        :type: int
        """

        self._water_level_method_tid = water_level_method_tid

    @property
    def marking_reference_tid(self):
        """Gets the marking_reference_tid of this Waterlevel2ViewModel.  # noqa: E501


        :return: The marking_reference_tid of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._marking_reference_tid

    @marking_reference_tid.setter
    def marking_reference_tid(self, marking_reference_tid):
        """Sets the marking_reference_tid of this Waterlevel2ViewModel.


        :param marking_reference_tid: The marking_reference_tid of this Waterlevel2ViewModel.  # noqa: E501
        :type: int
        """

        self._marking_reference_tid = marking_reference_tid

    @property
    def water_level_state_tid(self):
        """Gets the water_level_state_tid of this Waterlevel2ViewModel.  # noqa: E501


        :return: The water_level_state_tid of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._water_level_state_tid

    @water_level_state_tid.setter
    def water_level_state_tid(self, water_level_state_tid):
        """Sets the water_level_state_tid of this Waterlevel2ViewModel.


        :param water_level_state_tid: The water_level_state_tid of this Waterlevel2ViewModel.  # noqa: E501
        :type: int
        """

        self._water_level_state_tid = water_level_state_tid

    @property
    def marking_type_tid(self):
        """Gets the marking_type_tid of this Waterlevel2ViewModel.  # noqa: E501


        :return: The marking_type_tid of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._marking_type_tid

    @marking_type_tid.setter
    def marking_type_tid(self, marking_type_tid):
        """Sets the marking_type_tid of this Waterlevel2ViewModel.


        :param marking_type_tid: The marking_type_tid of this Waterlevel2ViewModel.  # noqa: E501
        :type: int
        """

        self._marking_type_tid = marking_type_tid

    @property
    def marking_type_name(self):
        """Gets the marking_type_name of this Waterlevel2ViewModel.  # noqa: E501


        :return: The marking_type_name of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._marking_type_name

    @marking_type_name.setter
    def marking_type_name(self, marking_type_name):
        """Sets the marking_type_name of this Waterlevel2ViewModel.


        :param marking_type_name: The marking_type_name of this Waterlevel2ViewModel.  # noqa: E501
        :type: str
        """

        self._marking_type_name = marking_type_name

    @property
    def measuring_tool_description(self):
        """Gets the measuring_tool_description of this Waterlevel2ViewModel.  # noqa: E501


        :return: The measuring_tool_description of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._measuring_tool_description

    @measuring_tool_description.setter
    def measuring_tool_description(self, measuring_tool_description):
        """Sets the measuring_tool_description of this Waterlevel2ViewModel.


        :param measuring_tool_description: The measuring_tool_description of this Waterlevel2ViewModel.  # noqa: E501
        :type: str
        """

        self._measuring_tool_description = measuring_tool_description

    @property
    def water_level_measurement(self):
        """Gets the water_level_measurement of this Waterlevel2ViewModel.  # noqa: E501


        :return: The water_level_measurement of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: list[WaterLevelMeasurementViewModel]
        """
        return self._water_level_measurement

    @water_level_measurement.setter
    def water_level_measurement(self, water_level_measurement):
        """Sets the water_level_measurement of this Waterlevel2ViewModel.


        :param water_level_measurement: The water_level_measurement of this Waterlevel2ViewModel.  # noqa: E501
        :type: list[WaterLevelMeasurementViewModel]
        """

        self._water_level_measurement = water_level_measurement

    @property
    def comment(self):
        """Gets the comment of this Waterlevel2ViewModel.  # noqa: E501


        :return: The comment of this Waterlevel2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Waterlevel2ViewModel.


        :param comment: The comment of this Waterlevel2ViewModel.  # noqa: E501
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
        if issubclass(Waterlevel2ViewModel, dict):
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
        if not isinstance(other, Waterlevel2ViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
