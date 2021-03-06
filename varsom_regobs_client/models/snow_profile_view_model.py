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


class SnowProfileViewModel(object):
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
        'total_depth': 'float',
        'attachment_id': 'int',
        'comment': 'str',
        'is_profile_to_ground': 'bool',
        'strat_profile': 'StratProfileViewModel',
        'snow_temp': 'SnowTempViewModel',
        'snow_density': 'list[SnowDensityViewModel]',
        'compression_test': 'list[CompressionTestViewModel]'
    }

    attribute_map = {
        'total_depth': 'TotalDepth',
        'attachment_id': 'AttachmentID',
        'comment': 'Comment',
        'is_profile_to_ground': 'IsProfileToGround',
        'strat_profile': 'StratProfile',
        'snow_temp': 'SnowTemp',
        'snow_density': 'SnowDensity',
        'compression_test': 'CompressionTest'
    }

    def __init__(self, total_depth=None, attachment_id=None, comment=None, is_profile_to_ground=None, strat_profile=None, snow_temp=None, snow_density=None, compression_test=None):  # noqa: E501
        """SnowProfileViewModel - a model defined in Swagger"""  # noqa: E501
        self._total_depth = None
        self._attachment_id = None
        self._comment = None
        self._is_profile_to_ground = None
        self._strat_profile = None
        self._snow_temp = None
        self._snow_density = None
        self._compression_test = None
        self.discriminator = None
        if total_depth is not None:
            self.total_depth = total_depth
        if attachment_id is not None:
            self.attachment_id = attachment_id
        if comment is not None:
            self.comment = comment
        if is_profile_to_ground is not None:
            self.is_profile_to_ground = is_profile_to_ground
        if strat_profile is not None:
            self.strat_profile = strat_profile
        if snow_temp is not None:
            self.snow_temp = snow_temp
        if snow_density is not None:
            self.snow_density = snow_density
        if compression_test is not None:
            self.compression_test = compression_test

    @property
    def total_depth(self):
        """Gets the total_depth of this SnowProfileViewModel.  # noqa: E501


        :return: The total_depth of this SnowProfileViewModel.  # noqa: E501
        :rtype: float
        """
        return self._total_depth

    @total_depth.setter
    def total_depth(self, total_depth):
        """Sets the total_depth of this SnowProfileViewModel.


        :param total_depth: The total_depth of this SnowProfileViewModel.  # noqa: E501
        :type: float
        """

        self._total_depth = total_depth

    @property
    def attachment_id(self):
        """Gets the attachment_id of this SnowProfileViewModel.  # noqa: E501


        :return: The attachment_id of this SnowProfileViewModel.  # noqa: E501
        :rtype: int
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this SnowProfileViewModel.


        :param attachment_id: The attachment_id of this SnowProfileViewModel.  # noqa: E501
        :type: int
        """

        self._attachment_id = attachment_id

    @property
    def comment(self):
        """Gets the comment of this SnowProfileViewModel.  # noqa: E501


        :return: The comment of this SnowProfileViewModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SnowProfileViewModel.


        :param comment: The comment of this SnowProfileViewModel.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def is_profile_to_ground(self):
        """Gets the is_profile_to_ground of this SnowProfileViewModel.  # noqa: E501


        :return: The is_profile_to_ground of this SnowProfileViewModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_profile_to_ground

    @is_profile_to_ground.setter
    def is_profile_to_ground(self, is_profile_to_ground):
        """Sets the is_profile_to_ground of this SnowProfileViewModel.


        :param is_profile_to_ground: The is_profile_to_ground of this SnowProfileViewModel.  # noqa: E501
        :type: bool
        """

        self._is_profile_to_ground = is_profile_to_ground

    @property
    def strat_profile(self):
        """Gets the strat_profile of this SnowProfileViewModel.  # noqa: E501


        :return: The strat_profile of this SnowProfileViewModel.  # noqa: E501
        :rtype: StratProfileViewModel
        """
        return self._strat_profile

    @strat_profile.setter
    def strat_profile(self, strat_profile):
        """Sets the strat_profile of this SnowProfileViewModel.


        :param strat_profile: The strat_profile of this SnowProfileViewModel.  # noqa: E501
        :type: StratProfileViewModel
        """

        self._strat_profile = strat_profile

    @property
    def snow_temp(self):
        """Gets the snow_temp of this SnowProfileViewModel.  # noqa: E501


        :return: The snow_temp of this SnowProfileViewModel.  # noqa: E501
        :rtype: SnowTempViewModel
        """
        return self._snow_temp

    @snow_temp.setter
    def snow_temp(self, snow_temp):
        """Sets the snow_temp of this SnowProfileViewModel.


        :param snow_temp: The snow_temp of this SnowProfileViewModel.  # noqa: E501
        :type: SnowTempViewModel
        """

        self._snow_temp = snow_temp

    @property
    def snow_density(self):
        """Gets the snow_density of this SnowProfileViewModel.  # noqa: E501


        :return: The snow_density of this SnowProfileViewModel.  # noqa: E501
        :rtype: list[SnowDensityViewModel]
        """
        return self._snow_density

    @snow_density.setter
    def snow_density(self, snow_density):
        """Sets the snow_density of this SnowProfileViewModel.


        :param snow_density: The snow_density of this SnowProfileViewModel.  # noqa: E501
        :type: list[SnowDensityViewModel]
        """

        self._snow_density = snow_density

    @property
    def compression_test(self):
        """Gets the compression_test of this SnowProfileViewModel.  # noqa: E501


        :return: The compression_test of this SnowProfileViewModel.  # noqa: E501
        :rtype: list[CompressionTestViewModel]
        """
        return self._compression_test

    @compression_test.setter
    def compression_test(self, compression_test):
        """Sets the compression_test of this SnowProfileViewModel.


        :param compression_test: The compression_test of this SnowProfileViewModel.  # noqa: E501
        :type: list[CompressionTestViewModel]
        """

        self._compression_test = compression_test

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
        if issubclass(SnowProfileViewModel, dict):
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
        if not isinstance(other, SnowProfileViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
