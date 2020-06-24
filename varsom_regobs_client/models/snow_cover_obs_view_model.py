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


class SnowCoverObsViewModel(object):
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
        'depth_hoar_thickness': 'float',
        'critical_layer_exists': 'bool',
        'critical_layer_location': 'float',
        'critical_layer_tid': 'int',
        'snow_pilot_ref': 'str',
        'comment': 'str',
        'critical_layer_name': 'str'
    }

    attribute_map = {
        'depth_hoar_thickness': 'DepthHoarThickness',
        'critical_layer_exists': 'CriticalLayerExists',
        'critical_layer_location': 'CriticalLayerLocation',
        'critical_layer_tid': 'CriticalLayerTID',
        'snow_pilot_ref': 'SnowPilotRef',
        'comment': 'Comment',
        'critical_layer_name': 'CriticalLayerName'
    }

    def __init__(self, depth_hoar_thickness=None, critical_layer_exists=None, critical_layer_location=None, critical_layer_tid=None, snow_pilot_ref=None, comment=None, critical_layer_name=None):  # noqa: E501
        """SnowCoverObsViewModel - a model defined in Swagger"""  # noqa: E501
        self._depth_hoar_thickness = None
        self._critical_layer_exists = None
        self._critical_layer_location = None
        self._critical_layer_tid = None
        self._snow_pilot_ref = None
        self._comment = None
        self._critical_layer_name = None
        self.discriminator = None
        if depth_hoar_thickness is not None:
            self.depth_hoar_thickness = depth_hoar_thickness
        if critical_layer_exists is not None:
            self.critical_layer_exists = critical_layer_exists
        if critical_layer_location is not None:
            self.critical_layer_location = critical_layer_location
        if critical_layer_tid is not None:
            self.critical_layer_tid = critical_layer_tid
        if snow_pilot_ref is not None:
            self.snow_pilot_ref = snow_pilot_ref
        if comment is not None:
            self.comment = comment
        if critical_layer_name is not None:
            self.critical_layer_name = critical_layer_name

    @property
    def depth_hoar_thickness(self):
        """Gets the depth_hoar_thickness of this SnowCoverObsViewModel.  # noqa: E501


        :return: The depth_hoar_thickness of this SnowCoverObsViewModel.  # noqa: E501
        :rtype: float
        """
        return self._depth_hoar_thickness

    @depth_hoar_thickness.setter
    def depth_hoar_thickness(self, depth_hoar_thickness):
        """Sets the depth_hoar_thickness of this SnowCoverObsViewModel.


        :param depth_hoar_thickness: The depth_hoar_thickness of this SnowCoverObsViewModel.  # noqa: E501
        :type: float
        """

        self._depth_hoar_thickness = depth_hoar_thickness

    @property
    def critical_layer_exists(self):
        """Gets the critical_layer_exists of this SnowCoverObsViewModel.  # noqa: E501


        :return: The critical_layer_exists of this SnowCoverObsViewModel.  # noqa: E501
        :rtype: bool
        """
        return self._critical_layer_exists

    @critical_layer_exists.setter
    def critical_layer_exists(self, critical_layer_exists):
        """Sets the critical_layer_exists of this SnowCoverObsViewModel.


        :param critical_layer_exists: The critical_layer_exists of this SnowCoverObsViewModel.  # noqa: E501
        :type: bool
        """

        self._critical_layer_exists = critical_layer_exists

    @property
    def critical_layer_location(self):
        """Gets the critical_layer_location of this SnowCoverObsViewModel.  # noqa: E501


        :return: The critical_layer_location of this SnowCoverObsViewModel.  # noqa: E501
        :rtype: float
        """
        return self._critical_layer_location

    @critical_layer_location.setter
    def critical_layer_location(self, critical_layer_location):
        """Sets the critical_layer_location of this SnowCoverObsViewModel.


        :param critical_layer_location: The critical_layer_location of this SnowCoverObsViewModel.  # noqa: E501
        :type: float
        """

        self._critical_layer_location = critical_layer_location

    @property
    def critical_layer_tid(self):
        """Gets the critical_layer_tid of this SnowCoverObsViewModel.  # noqa: E501


        :return: The critical_layer_tid of this SnowCoverObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._critical_layer_tid

    @critical_layer_tid.setter
    def critical_layer_tid(self, critical_layer_tid):
        """Sets the critical_layer_tid of this SnowCoverObsViewModel.


        :param critical_layer_tid: The critical_layer_tid of this SnowCoverObsViewModel.  # noqa: E501
        :type: int
        """

        self._critical_layer_tid = critical_layer_tid

    @property
    def snow_pilot_ref(self):
        """Gets the snow_pilot_ref of this SnowCoverObsViewModel.  # noqa: E501


        :return: The snow_pilot_ref of this SnowCoverObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._snow_pilot_ref

    @snow_pilot_ref.setter
    def snow_pilot_ref(self, snow_pilot_ref):
        """Sets the snow_pilot_ref of this SnowCoverObsViewModel.


        :param snow_pilot_ref: The snow_pilot_ref of this SnowCoverObsViewModel.  # noqa: E501
        :type: str
        """

        self._snow_pilot_ref = snow_pilot_ref

    @property
    def comment(self):
        """Gets the comment of this SnowCoverObsViewModel.  # noqa: E501


        :return: The comment of this SnowCoverObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SnowCoverObsViewModel.


        :param comment: The comment of this SnowCoverObsViewModel.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def critical_layer_name(self):
        """Gets the critical_layer_name of this SnowCoverObsViewModel.  # noqa: E501


        :return: The critical_layer_name of this SnowCoverObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._critical_layer_name

    @critical_layer_name.setter
    def critical_layer_name(self, critical_layer_name):
        """Sets the critical_layer_name of this SnowCoverObsViewModel.


        :param critical_layer_name: The critical_layer_name of this SnowCoverObsViewModel.  # noqa: E501
        :type: str
        """

        self._critical_layer_name = critical_layer_name

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
        if issubclass(SnowCoverObsViewModel, dict):
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
        if not isinstance(other, SnowCoverObsViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
