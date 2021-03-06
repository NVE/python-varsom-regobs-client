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


class GeneralObservationEditModel(object):
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
        'geo_hazard_tid': 'int',
        'obs_comment': 'str',
        'obs_header': 'str',
        'usage_flag_tid': 'int',
        'comment': 'str',
        'urls': 'list[UrlViewModel]'
    }

    attribute_map = {
        'geo_hazard_tid': 'GeoHazardTID',
        'obs_comment': 'ObsComment',
        'obs_header': 'ObsHeader',
        'usage_flag_tid': 'UsageFlagTID',
        'comment': 'Comment',
        'urls': 'Urls'
    }

    def __init__(self, geo_hazard_tid=None, obs_comment=None, obs_header=None, usage_flag_tid=None, comment=None, urls=None):  # noqa: E501
        """GeneralObservationEditModel - a model defined in Swagger"""  # noqa: E501
        self._geo_hazard_tid = None
        self._obs_comment = None
        self._obs_header = None
        self._usage_flag_tid = None
        self._comment = None
        self._urls = None
        self.discriminator = None
        if geo_hazard_tid is not None:
            self.geo_hazard_tid = geo_hazard_tid
        if obs_comment is not None:
            self.obs_comment = obs_comment
        if obs_header is not None:
            self.obs_header = obs_header
        if usage_flag_tid is not None:
            self.usage_flag_tid = usage_flag_tid
        if comment is not None:
            self.comment = comment
        if urls is not None:
            self.urls = urls

    @property
    def geo_hazard_tid(self):
        """Gets the geo_hazard_tid of this GeneralObservationEditModel.  # noqa: E501


        :return: The geo_hazard_tid of this GeneralObservationEditModel.  # noqa: E501
        :rtype: int
        """
        return self._geo_hazard_tid

    @geo_hazard_tid.setter
    def geo_hazard_tid(self, geo_hazard_tid):
        """Sets the geo_hazard_tid of this GeneralObservationEditModel.


        :param geo_hazard_tid: The geo_hazard_tid of this GeneralObservationEditModel.  # noqa: E501
        :type: int
        """

        self._geo_hazard_tid = geo_hazard_tid

    @property
    def obs_comment(self):
        """Gets the obs_comment of this GeneralObservationEditModel.  # noqa: E501


        :return: The obs_comment of this GeneralObservationEditModel.  # noqa: E501
        :rtype: str
        """
        return self._obs_comment

    @obs_comment.setter
    def obs_comment(self, obs_comment):
        """Sets the obs_comment of this GeneralObservationEditModel.


        :param obs_comment: The obs_comment of this GeneralObservationEditModel.  # noqa: E501
        :type: str
        """

        self._obs_comment = obs_comment

    @property
    def obs_header(self):
        """Gets the obs_header of this GeneralObservationEditModel.  # noqa: E501


        :return: The obs_header of this GeneralObservationEditModel.  # noqa: E501
        :rtype: str
        """
        return self._obs_header

    @obs_header.setter
    def obs_header(self, obs_header):
        """Sets the obs_header of this GeneralObservationEditModel.


        :param obs_header: The obs_header of this GeneralObservationEditModel.  # noqa: E501
        :type: str
        """

        self._obs_header = obs_header

    @property
    def usage_flag_tid(self):
        """Gets the usage_flag_tid of this GeneralObservationEditModel.  # noqa: E501


        :return: The usage_flag_tid of this GeneralObservationEditModel.  # noqa: E501
        :rtype: int
        """
        return self._usage_flag_tid

    @usage_flag_tid.setter
    def usage_flag_tid(self, usage_flag_tid):
        """Sets the usage_flag_tid of this GeneralObservationEditModel.


        :param usage_flag_tid: The usage_flag_tid of this GeneralObservationEditModel.  # noqa: E501
        :type: int
        """

        self._usage_flag_tid = usage_flag_tid

    @property
    def comment(self):
        """Gets the comment of this GeneralObservationEditModel.  # noqa: E501


        :return: The comment of this GeneralObservationEditModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this GeneralObservationEditModel.


        :param comment: The comment of this GeneralObservationEditModel.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def urls(self):
        """Gets the urls of this GeneralObservationEditModel.  # noqa: E501


        :return: The urls of this GeneralObservationEditModel.  # noqa: E501
        :rtype: list[UrlViewModel]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this GeneralObservationEditModel.


        :param urls: The urls of this GeneralObservationEditModel.  # noqa: E501
        :type: list[UrlViewModel]
        """

        self._urls = urls

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
        if issubclass(GeneralObservationEditModel, dict):
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
        if not isinstance(other, GeneralObservationEditModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
