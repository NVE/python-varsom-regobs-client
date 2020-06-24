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


class CompressionTestDto(object):
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
        'compression_test_tid': 'int',
        'taps_fracture': 'int',
        'taps_full_propagation': 'int',
        'propagation_tid': 'int',
        'fracture_depth': 'float',
        'stability_eval_tid': 'int',
        'usage_flag_tid': 'int',
        'compr_test_fracture_tid': 'int',
        'comment': 'str',
        'include_in_snow_profile': 'bool'
    }

    attribute_map = {
        'compression_test_tid': 'CompressionTestTID',
        'taps_fracture': 'TapsFracture',
        'taps_full_propagation': 'TapsFullPropagation',
        'propagation_tid': 'PropagationTID',
        'fracture_depth': 'FractureDepth',
        'stability_eval_tid': 'StabilityEvalTID',
        'usage_flag_tid': 'UsageFlagTID',
        'compr_test_fracture_tid': 'ComprTestFractureTID',
        'comment': 'Comment',
        'include_in_snow_profile': 'IncludeInSnowProfile'
    }

    def __init__(self, compression_test_tid=None, taps_fracture=None, taps_full_propagation=None, propagation_tid=None, fracture_depth=None, stability_eval_tid=None, usage_flag_tid=None, compr_test_fracture_tid=None, comment=None, include_in_snow_profile=None):  # noqa: E501
        """CompressionTestDto - a model defined in Swagger"""  # noqa: E501
        self._compression_test_tid = None
        self._taps_fracture = None
        self._taps_full_propagation = None
        self._propagation_tid = None
        self._fracture_depth = None
        self._stability_eval_tid = None
        self._usage_flag_tid = None
        self._compr_test_fracture_tid = None
        self._comment = None
        self._include_in_snow_profile = None
        self.discriminator = None
        if compression_test_tid is not None:
            self.compression_test_tid = compression_test_tid
        if taps_fracture is not None:
            self.taps_fracture = taps_fracture
        if taps_full_propagation is not None:
            self.taps_full_propagation = taps_full_propagation
        if propagation_tid is not None:
            self.propagation_tid = propagation_tid
        if fracture_depth is not None:
            self.fracture_depth = fracture_depth
        if stability_eval_tid is not None:
            self.stability_eval_tid = stability_eval_tid
        if usage_flag_tid is not None:
            self.usage_flag_tid = usage_flag_tid
        if compr_test_fracture_tid is not None:
            self.compr_test_fracture_tid = compr_test_fracture_tid
        if comment is not None:
            self.comment = comment
        if include_in_snow_profile is not None:
            self.include_in_snow_profile = include_in_snow_profile

    @property
    def compression_test_tid(self):
        """Gets the compression_test_tid of this CompressionTestDto.  # noqa: E501

        The CompressionTestKDV unique identifier  # noqa: E501

        :return: The compression_test_tid of this CompressionTestDto.  # noqa: E501
        :rtype: int
        """
        return self._compression_test_tid

    @compression_test_tid.setter
    def compression_test_tid(self, compression_test_tid):
        """Sets the compression_test_tid of this CompressionTestDto.

        The CompressionTestKDV unique identifier  # noqa: E501

        :param compression_test_tid: The compression_test_tid of this CompressionTestDto.  # noqa: E501
        :type: int
        """

        self._compression_test_tid = compression_test_tid

    @property
    def taps_fracture(self):
        """Gets the taps_fracture of this CompressionTestDto.  # noqa: E501

        TapsFracture  # noqa: E501

        :return: The taps_fracture of this CompressionTestDto.  # noqa: E501
        :rtype: int
        """
        return self._taps_fracture

    @taps_fracture.setter
    def taps_fracture(self, taps_fracture):
        """Sets the taps_fracture of this CompressionTestDto.

        TapsFracture  # noqa: E501

        :param taps_fracture: The taps_fracture of this CompressionTestDto.  # noqa: E501
        :type: int
        """

        self._taps_fracture = taps_fracture

    @property
    def taps_full_propagation(self):
        """Gets the taps_full_propagation of this CompressionTestDto.  # noqa: E501

        TapsFullPropagation  # noqa: E501

        :return: The taps_full_propagation of this CompressionTestDto.  # noqa: E501
        :rtype: int
        """
        return self._taps_full_propagation

    @taps_full_propagation.setter
    def taps_full_propagation(self, taps_full_propagation):
        """Sets the taps_full_propagation of this CompressionTestDto.

        TapsFullPropagation  # noqa: E501

        :param taps_full_propagation: The taps_full_propagation of this CompressionTestDto.  # noqa: E501
        :type: int
        """

        self._taps_full_propagation = taps_full_propagation

    @property
    def propagation_tid(self):
        """Gets the propagation_tid of this CompressionTestDto.  # noqa: E501

        The PropagationKD unique identifier  # noqa: E501

        :return: The propagation_tid of this CompressionTestDto.  # noqa: E501
        :rtype: int
        """
        return self._propagation_tid

    @propagation_tid.setter
    def propagation_tid(self, propagation_tid):
        """Sets the propagation_tid of this CompressionTestDto.

        The PropagationKD unique identifier  # noqa: E501

        :param propagation_tid: The propagation_tid of this CompressionTestDto.  # noqa: E501
        :type: int
        """

        self._propagation_tid = propagation_tid

    @property
    def fracture_depth(self):
        """Gets the fracture_depth of this CompressionTestDto.  # noqa: E501

        FractureDepth  # noqa: E501

        :return: The fracture_depth of this CompressionTestDto.  # noqa: E501
        :rtype: float
        """
        return self._fracture_depth

    @fracture_depth.setter
    def fracture_depth(self, fracture_depth):
        """Sets the fracture_depth of this CompressionTestDto.

        FractureDepth  # noqa: E501

        :param fracture_depth: The fracture_depth of this CompressionTestDto.  # noqa: E501
        :type: float
        """

        self._fracture_depth = fracture_depth

    @property
    def stability_eval_tid(self):
        """Gets the stability_eval_tid of this CompressionTestDto.  # noqa: E501

        The StabilityEvalKD unique identifier  # noqa: E501

        :return: The stability_eval_tid of this CompressionTestDto.  # noqa: E501
        :rtype: int
        """
        return self._stability_eval_tid

    @stability_eval_tid.setter
    def stability_eval_tid(self, stability_eval_tid):
        """Sets the stability_eval_tid of this CompressionTestDto.

        The StabilityEvalKD unique identifier  # noqa: E501

        :param stability_eval_tid: The stability_eval_tid of this CompressionTestDto.  # noqa: E501
        :type: int
        """

        self._stability_eval_tid = stability_eval_tid

    @property
    def usage_flag_tid(self):
        """Gets the usage_flag_tid of this CompressionTestDto.  # noqa: E501

        The UsageFlagKD unique identifier  # noqa: E501

        :return: The usage_flag_tid of this CompressionTestDto.  # noqa: E501
        :rtype: int
        """
        return self._usage_flag_tid

    @usage_flag_tid.setter
    def usage_flag_tid(self, usage_flag_tid):
        """Sets the usage_flag_tid of this CompressionTestDto.

        The UsageFlagKD unique identifier  # noqa: E501

        :param usage_flag_tid: The usage_flag_tid of this CompressionTestDto.  # noqa: E501
        :type: int
        """

        self._usage_flag_tid = usage_flag_tid

    @property
    def compr_test_fracture_tid(self):
        """Gets the compr_test_fracture_tid of this CompressionTestDto.  # noqa: E501

        The ComprTestFractureKD unique identifier  # noqa: E501

        :return: The compr_test_fracture_tid of this CompressionTestDto.  # noqa: E501
        :rtype: int
        """
        return self._compr_test_fracture_tid

    @compr_test_fracture_tid.setter
    def compr_test_fracture_tid(self, compr_test_fracture_tid):
        """Sets the compr_test_fracture_tid of this CompressionTestDto.

        The ComprTestFractureKD unique identifier  # noqa: E501

        :param compr_test_fracture_tid: The compr_test_fracture_tid of this CompressionTestDto.  # noqa: E501
        :type: int
        """

        self._compr_test_fracture_tid = compr_test_fracture_tid

    @property
    def comment(self):
        """Gets the comment of this CompressionTestDto.  # noqa: E501

        Comment  # noqa: E501

        :return: The comment of this CompressionTestDto.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CompressionTestDto.

        Comment  # noqa: E501

        :param comment: The comment of this CompressionTestDto.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def include_in_snow_profile(self):
        """Gets the include_in_snow_profile of this CompressionTestDto.  # noqa: E501

        Include in snow profile  # noqa: E501

        :return: The include_in_snow_profile of this CompressionTestDto.  # noqa: E501
        :rtype: bool
        """
        return self._include_in_snow_profile

    @include_in_snow_profile.setter
    def include_in_snow_profile(self, include_in_snow_profile):
        """Sets the include_in_snow_profile of this CompressionTestDto.

        Include in snow profile  # noqa: E501

        :param include_in_snow_profile: The include_in_snow_profile of this CompressionTestDto.  # noqa: E501
        :type: bool
        """

        self._include_in_snow_profile = include_in_snow_profile

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
        if issubclass(CompressionTestDto, dict):
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
        if not isinstance(other, CompressionTestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other