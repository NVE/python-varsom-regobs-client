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


class AvalancheActivityObs2Dto(object):
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
        'estimated_num_tid': 'int',
        'dt_start': 'datetime',
        'dt_end': 'datetime',
        'valid_exposition': 'str',
        'exposed_height1': 'int',
        'exposed_height2': 'int',
        'exposed_height_combo_tid': 'int',
        'avalanche_ext_tid': 'int',
        'aval_cause_tid': 'int',
        'aval_trigger_simple_tid': 'int',
        'destructive_size_tid': 'int',
        'aval_propagation_tid': 'int',
        'comment': 'str',
        'usage_flag_tid': 'int'
    }

    attribute_map = {
        'estimated_num_tid': 'EstimatedNumTID',
        'dt_start': 'DtStart',
        'dt_end': 'DtEnd',
        'valid_exposition': 'ValidExposition',
        'exposed_height1': 'ExposedHeight1',
        'exposed_height2': 'ExposedHeight2',
        'exposed_height_combo_tid': 'ExposedHeightComboTID',
        'avalanche_ext_tid': 'AvalancheExtTID',
        'aval_cause_tid': 'AvalCauseTID',
        'aval_trigger_simple_tid': 'AvalTriggerSimpleTID',
        'destructive_size_tid': 'DestructiveSizeTID',
        'aval_propagation_tid': 'AvalPropagationTID',
        'comment': 'Comment',
        'usage_flag_tid': 'UsageFlagTID'
    }

    def __init__(self, estimated_num_tid=None, dt_start=None, dt_end=None, valid_exposition=None, exposed_height1=None, exposed_height2=None, exposed_height_combo_tid=None, avalanche_ext_tid=None, aval_cause_tid=None, aval_trigger_simple_tid=None, destructive_size_tid=None, aval_propagation_tid=None, comment=None, usage_flag_tid=None):  # noqa: E501
        """AvalancheActivityObs2Dto - a model defined in Swagger"""  # noqa: E501
        self._estimated_num_tid = None
        self._dt_start = None
        self._dt_end = None
        self._valid_exposition = None
        self._exposed_height1 = None
        self._exposed_height2 = None
        self._exposed_height_combo_tid = None
        self._avalanche_ext_tid = None
        self._aval_cause_tid = None
        self._aval_trigger_simple_tid = None
        self._destructive_size_tid = None
        self._aval_propagation_tid = None
        self._comment = None
        self._usage_flag_tid = None
        self.discriminator = None
        if estimated_num_tid is not None:
            self.estimated_num_tid = estimated_num_tid
        if dt_start is not None:
            self.dt_start = dt_start
        if dt_end is not None:
            self.dt_end = dt_end
        if valid_exposition is not None:
            self.valid_exposition = valid_exposition
        if exposed_height1 is not None:
            self.exposed_height1 = exposed_height1
        if exposed_height2 is not None:
            self.exposed_height2 = exposed_height2
        if exposed_height_combo_tid is not None:
            self.exposed_height_combo_tid = exposed_height_combo_tid
        if avalanche_ext_tid is not None:
            self.avalanche_ext_tid = avalanche_ext_tid
        if aval_cause_tid is not None:
            self.aval_cause_tid = aval_cause_tid
        if aval_trigger_simple_tid is not None:
            self.aval_trigger_simple_tid = aval_trigger_simple_tid
        if destructive_size_tid is not None:
            self.destructive_size_tid = destructive_size_tid
        if aval_propagation_tid is not None:
            self.aval_propagation_tid = aval_propagation_tid
        if comment is not None:
            self.comment = comment
        if usage_flag_tid is not None:
            self.usage_flag_tid = usage_flag_tid

    @property
    def estimated_num_tid(self):
        """Gets the estimated_num_tid of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The estimated_num_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: int
        """
        return self._estimated_num_tid

    @estimated_num_tid.setter
    def estimated_num_tid(self, estimated_num_tid):
        """Sets the estimated_num_tid of this AvalancheActivityObs2Dto.


        :param estimated_num_tid: The estimated_num_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: int
        """

        self._estimated_num_tid = estimated_num_tid

    @property
    def dt_start(self):
        """Gets the dt_start of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The dt_start of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: datetime
        """
        return self._dt_start

    @dt_start.setter
    def dt_start(self, dt_start):
        """Sets the dt_start of this AvalancheActivityObs2Dto.


        :param dt_start: The dt_start of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: datetime
        """

        self._dt_start = dt_start

    @property
    def dt_end(self):
        """Gets the dt_end of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The dt_end of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: datetime
        """
        return self._dt_end

    @dt_end.setter
    def dt_end(self, dt_end):
        """Sets the dt_end of this AvalancheActivityObs2Dto.


        :param dt_end: The dt_end of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: datetime
        """

        self._dt_end = dt_end

    @property
    def valid_exposition(self):
        """Gets the valid_exposition of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The valid_exposition of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: str
        """
        return self._valid_exposition

    @valid_exposition.setter
    def valid_exposition(self, valid_exposition):
        """Sets the valid_exposition of this AvalancheActivityObs2Dto.


        :param valid_exposition: The valid_exposition of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: str
        """

        self._valid_exposition = valid_exposition

    @property
    def exposed_height1(self):
        """Gets the exposed_height1 of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The exposed_height1 of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height1

    @exposed_height1.setter
    def exposed_height1(self, exposed_height1):
        """Sets the exposed_height1 of this AvalancheActivityObs2Dto.


        :param exposed_height1: The exposed_height1 of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: int
        """

        self._exposed_height1 = exposed_height1

    @property
    def exposed_height2(self):
        """Gets the exposed_height2 of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The exposed_height2 of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height2

    @exposed_height2.setter
    def exposed_height2(self, exposed_height2):
        """Sets the exposed_height2 of this AvalancheActivityObs2Dto.


        :param exposed_height2: The exposed_height2 of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: int
        """

        self._exposed_height2 = exposed_height2

    @property
    def exposed_height_combo_tid(self):
        """Gets the exposed_height_combo_tid of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The exposed_height_combo_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height_combo_tid

    @exposed_height_combo_tid.setter
    def exposed_height_combo_tid(self, exposed_height_combo_tid):
        """Sets the exposed_height_combo_tid of this AvalancheActivityObs2Dto.


        :param exposed_height_combo_tid: The exposed_height_combo_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: int
        """

        self._exposed_height_combo_tid = exposed_height_combo_tid

    @property
    def avalanche_ext_tid(self):
        """Gets the avalanche_ext_tid of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The avalanche_ext_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: int
        """
        return self._avalanche_ext_tid

    @avalanche_ext_tid.setter
    def avalanche_ext_tid(self, avalanche_ext_tid):
        """Sets the avalanche_ext_tid of this AvalancheActivityObs2Dto.


        :param avalanche_ext_tid: The avalanche_ext_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: int
        """

        self._avalanche_ext_tid = avalanche_ext_tid

    @property
    def aval_cause_tid(self):
        """Gets the aval_cause_tid of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The aval_cause_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_tid

    @aval_cause_tid.setter
    def aval_cause_tid(self, aval_cause_tid):
        """Sets the aval_cause_tid of this AvalancheActivityObs2Dto.


        :param aval_cause_tid: The aval_cause_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: int
        """

        self._aval_cause_tid = aval_cause_tid

    @property
    def aval_trigger_simple_tid(self):
        """Gets the aval_trigger_simple_tid of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The aval_trigger_simple_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: int
        """
        return self._aval_trigger_simple_tid

    @aval_trigger_simple_tid.setter
    def aval_trigger_simple_tid(self, aval_trigger_simple_tid):
        """Sets the aval_trigger_simple_tid of this AvalancheActivityObs2Dto.


        :param aval_trigger_simple_tid: The aval_trigger_simple_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: int
        """

        self._aval_trigger_simple_tid = aval_trigger_simple_tid

    @property
    def destructive_size_tid(self):
        """Gets the destructive_size_tid of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The destructive_size_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: int
        """
        return self._destructive_size_tid

    @destructive_size_tid.setter
    def destructive_size_tid(self, destructive_size_tid):
        """Sets the destructive_size_tid of this AvalancheActivityObs2Dto.


        :param destructive_size_tid: The destructive_size_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: int
        """

        self._destructive_size_tid = destructive_size_tid

    @property
    def aval_propagation_tid(self):
        """Gets the aval_propagation_tid of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The aval_propagation_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: int
        """
        return self._aval_propagation_tid

    @aval_propagation_tid.setter
    def aval_propagation_tid(self, aval_propagation_tid):
        """Sets the aval_propagation_tid of this AvalancheActivityObs2Dto.


        :param aval_propagation_tid: The aval_propagation_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: int
        """

        self._aval_propagation_tid = aval_propagation_tid

    @property
    def comment(self):
        """Gets the comment of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The comment of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AvalancheActivityObs2Dto.


        :param comment: The comment of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def usage_flag_tid(self):
        """Gets the usage_flag_tid of this AvalancheActivityObs2Dto.  # noqa: E501


        :return: The usage_flag_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :rtype: int
        """
        return self._usage_flag_tid

    @usage_flag_tid.setter
    def usage_flag_tid(self, usage_flag_tid):
        """Sets the usage_flag_tid of this AvalancheActivityObs2Dto.


        :param usage_flag_tid: The usage_flag_tid of this AvalancheActivityObs2Dto.  # noqa: E501
        :type: int
        """

        self._usage_flag_tid = usage_flag_tid

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
        if issubclass(AvalancheActivityObs2Dto, dict):
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
        if not isinstance(other, AvalancheActivityObs2Dto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
