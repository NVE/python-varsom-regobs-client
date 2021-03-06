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


class SnowSurfaceViewModel(object):
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
        'snow_depth': 'float',
        'new_snow_depth24': 'float',
        'new_snow_line': 'int',
        'snow_wind_depth24': 'float',
        'surface_water_content_tid': 'int',
        'surface_water_content_name': 'str',
        'snow_drift_tid': 'int',
        'snow_drift_name': 'str',
        'snow_surface_tid': 'int',
        'snow_surface_name': 'str',
        'surface_rougness_tid': 'int',
        'surface_rougness_name': 'str',
        'foot_penetration': 'float',
        'comment': 'str',
        'height_limit_layered_snow': 'float',
        'snow_line': 'int'
    }

    attribute_map = {
        'snow_depth': 'SnowDepth',
        'new_snow_depth24': 'NewSnowDepth24',
        'new_snow_line': 'NewSnowLine',
        'snow_wind_depth24': 'SnowWindDepth24',
        'surface_water_content_tid': 'SurfaceWaterContentTID',
        'surface_water_content_name': 'SurfaceWaterContentName',
        'snow_drift_tid': 'SnowDriftTID',
        'snow_drift_name': 'SnowDriftName',
        'snow_surface_tid': 'SnowSurfaceTID',
        'snow_surface_name': 'SnowSurfaceName',
        'surface_rougness_tid': 'SurfaceRougnessTID',
        'surface_rougness_name': 'SurfaceRougnessName',
        'foot_penetration': 'FootPenetration',
        'comment': 'Comment',
        'height_limit_layered_snow': 'HeightLimitLayeredSnow',
        'snow_line': 'SnowLine'
    }

    def __init__(self, snow_depth=None, new_snow_depth24=None, new_snow_line=None, snow_wind_depth24=None, surface_water_content_tid=None, surface_water_content_name=None, snow_drift_tid=None, snow_drift_name=None, snow_surface_tid=None, snow_surface_name=None, surface_rougness_tid=None, surface_rougness_name=None, foot_penetration=None, comment=None, height_limit_layered_snow=None, snow_line=None):  # noqa: E501
        """SnowSurfaceViewModel - a model defined in Swagger"""  # noqa: E501
        self._snow_depth = None
        self._new_snow_depth24 = None
        self._new_snow_line = None
        self._snow_wind_depth24 = None
        self._surface_water_content_tid = None
        self._surface_water_content_name = None
        self._snow_drift_tid = None
        self._snow_drift_name = None
        self._snow_surface_tid = None
        self._snow_surface_name = None
        self._surface_rougness_tid = None
        self._surface_rougness_name = None
        self._foot_penetration = None
        self._comment = None
        self._height_limit_layered_snow = None
        self._snow_line = None
        self.discriminator = None
        if snow_depth is not None:
            self.snow_depth = snow_depth
        if new_snow_depth24 is not None:
            self.new_snow_depth24 = new_snow_depth24
        if new_snow_line is not None:
            self.new_snow_line = new_snow_line
        if snow_wind_depth24 is not None:
            self.snow_wind_depth24 = snow_wind_depth24
        if surface_water_content_tid is not None:
            self.surface_water_content_tid = surface_water_content_tid
        if surface_water_content_name is not None:
            self.surface_water_content_name = surface_water_content_name
        if snow_drift_tid is not None:
            self.snow_drift_tid = snow_drift_tid
        if snow_drift_name is not None:
            self.snow_drift_name = snow_drift_name
        if snow_surface_tid is not None:
            self.snow_surface_tid = snow_surface_tid
        if snow_surface_name is not None:
            self.snow_surface_name = snow_surface_name
        if surface_rougness_tid is not None:
            self.surface_rougness_tid = surface_rougness_tid
        if surface_rougness_name is not None:
            self.surface_rougness_name = surface_rougness_name
        if foot_penetration is not None:
            self.foot_penetration = foot_penetration
        if comment is not None:
            self.comment = comment
        if height_limit_layered_snow is not None:
            self.height_limit_layered_snow = height_limit_layered_snow
        if snow_line is not None:
            self.snow_line = snow_line

    @property
    def snow_depth(self):
        """Gets the snow_depth of this SnowSurfaceViewModel.  # noqa: E501


        :return: The snow_depth of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: float
        """
        return self._snow_depth

    @snow_depth.setter
    def snow_depth(self, snow_depth):
        """Sets the snow_depth of this SnowSurfaceViewModel.


        :param snow_depth: The snow_depth of this SnowSurfaceViewModel.  # noqa: E501
        :type: float
        """

        self._snow_depth = snow_depth

    @property
    def new_snow_depth24(self):
        """Gets the new_snow_depth24 of this SnowSurfaceViewModel.  # noqa: E501


        :return: The new_snow_depth24 of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: float
        """
        return self._new_snow_depth24

    @new_snow_depth24.setter
    def new_snow_depth24(self, new_snow_depth24):
        """Sets the new_snow_depth24 of this SnowSurfaceViewModel.


        :param new_snow_depth24: The new_snow_depth24 of this SnowSurfaceViewModel.  # noqa: E501
        :type: float
        """

        self._new_snow_depth24 = new_snow_depth24

    @property
    def new_snow_line(self):
        """Gets the new_snow_line of this SnowSurfaceViewModel.  # noqa: E501


        :return: The new_snow_line of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: int
        """
        return self._new_snow_line

    @new_snow_line.setter
    def new_snow_line(self, new_snow_line):
        """Sets the new_snow_line of this SnowSurfaceViewModel.


        :param new_snow_line: The new_snow_line of this SnowSurfaceViewModel.  # noqa: E501
        :type: int
        """

        self._new_snow_line = new_snow_line

    @property
    def snow_wind_depth24(self):
        """Gets the snow_wind_depth24 of this SnowSurfaceViewModel.  # noqa: E501


        :return: The snow_wind_depth24 of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: float
        """
        return self._snow_wind_depth24

    @snow_wind_depth24.setter
    def snow_wind_depth24(self, snow_wind_depth24):
        """Sets the snow_wind_depth24 of this SnowSurfaceViewModel.


        :param snow_wind_depth24: The snow_wind_depth24 of this SnowSurfaceViewModel.  # noqa: E501
        :type: float
        """

        self._snow_wind_depth24 = snow_wind_depth24

    @property
    def surface_water_content_tid(self):
        """Gets the surface_water_content_tid of this SnowSurfaceViewModel.  # noqa: E501


        :return: The surface_water_content_tid of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: int
        """
        return self._surface_water_content_tid

    @surface_water_content_tid.setter
    def surface_water_content_tid(self, surface_water_content_tid):
        """Sets the surface_water_content_tid of this SnowSurfaceViewModel.


        :param surface_water_content_tid: The surface_water_content_tid of this SnowSurfaceViewModel.  # noqa: E501
        :type: int
        """

        self._surface_water_content_tid = surface_water_content_tid

    @property
    def surface_water_content_name(self):
        """Gets the surface_water_content_name of this SnowSurfaceViewModel.  # noqa: E501


        :return: The surface_water_content_name of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: str
        """
        return self._surface_water_content_name

    @surface_water_content_name.setter
    def surface_water_content_name(self, surface_water_content_name):
        """Sets the surface_water_content_name of this SnowSurfaceViewModel.


        :param surface_water_content_name: The surface_water_content_name of this SnowSurfaceViewModel.  # noqa: E501
        :type: str
        """

        self._surface_water_content_name = surface_water_content_name

    @property
    def snow_drift_tid(self):
        """Gets the snow_drift_tid of this SnowSurfaceViewModel.  # noqa: E501


        :return: The snow_drift_tid of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: int
        """
        return self._snow_drift_tid

    @snow_drift_tid.setter
    def snow_drift_tid(self, snow_drift_tid):
        """Sets the snow_drift_tid of this SnowSurfaceViewModel.


        :param snow_drift_tid: The snow_drift_tid of this SnowSurfaceViewModel.  # noqa: E501
        :type: int
        """

        self._snow_drift_tid = snow_drift_tid

    @property
    def snow_drift_name(self):
        """Gets the snow_drift_name of this SnowSurfaceViewModel.  # noqa: E501


        :return: The snow_drift_name of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: str
        """
        return self._snow_drift_name

    @snow_drift_name.setter
    def snow_drift_name(self, snow_drift_name):
        """Sets the snow_drift_name of this SnowSurfaceViewModel.


        :param snow_drift_name: The snow_drift_name of this SnowSurfaceViewModel.  # noqa: E501
        :type: str
        """

        self._snow_drift_name = snow_drift_name

    @property
    def snow_surface_tid(self):
        """Gets the snow_surface_tid of this SnowSurfaceViewModel.  # noqa: E501


        :return: The snow_surface_tid of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: int
        """
        return self._snow_surface_tid

    @snow_surface_tid.setter
    def snow_surface_tid(self, snow_surface_tid):
        """Sets the snow_surface_tid of this SnowSurfaceViewModel.


        :param snow_surface_tid: The snow_surface_tid of this SnowSurfaceViewModel.  # noqa: E501
        :type: int
        """

        self._snow_surface_tid = snow_surface_tid

    @property
    def snow_surface_name(self):
        """Gets the snow_surface_name of this SnowSurfaceViewModel.  # noqa: E501


        :return: The snow_surface_name of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: str
        """
        return self._snow_surface_name

    @snow_surface_name.setter
    def snow_surface_name(self, snow_surface_name):
        """Sets the snow_surface_name of this SnowSurfaceViewModel.


        :param snow_surface_name: The snow_surface_name of this SnowSurfaceViewModel.  # noqa: E501
        :type: str
        """

        self._snow_surface_name = snow_surface_name

    @property
    def surface_rougness_tid(self):
        """Gets the surface_rougness_tid of this SnowSurfaceViewModel.  # noqa: E501


        :return: The surface_rougness_tid of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: int
        """
        return self._surface_rougness_tid

    @surface_rougness_tid.setter
    def surface_rougness_tid(self, surface_rougness_tid):
        """Sets the surface_rougness_tid of this SnowSurfaceViewModel.


        :param surface_rougness_tid: The surface_rougness_tid of this SnowSurfaceViewModel.  # noqa: E501
        :type: int
        """

        self._surface_rougness_tid = surface_rougness_tid

    @property
    def surface_rougness_name(self):
        """Gets the surface_rougness_name of this SnowSurfaceViewModel.  # noqa: E501


        :return: The surface_rougness_name of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: str
        """
        return self._surface_rougness_name

    @surface_rougness_name.setter
    def surface_rougness_name(self, surface_rougness_name):
        """Sets the surface_rougness_name of this SnowSurfaceViewModel.


        :param surface_rougness_name: The surface_rougness_name of this SnowSurfaceViewModel.  # noqa: E501
        :type: str
        """

        self._surface_rougness_name = surface_rougness_name

    @property
    def foot_penetration(self):
        """Gets the foot_penetration of this SnowSurfaceViewModel.  # noqa: E501


        :return: The foot_penetration of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: float
        """
        return self._foot_penetration

    @foot_penetration.setter
    def foot_penetration(self, foot_penetration):
        """Sets the foot_penetration of this SnowSurfaceViewModel.


        :param foot_penetration: The foot_penetration of this SnowSurfaceViewModel.  # noqa: E501
        :type: float
        """

        self._foot_penetration = foot_penetration

    @property
    def comment(self):
        """Gets the comment of this SnowSurfaceViewModel.  # noqa: E501


        :return: The comment of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SnowSurfaceViewModel.


        :param comment: The comment of this SnowSurfaceViewModel.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def height_limit_layered_snow(self):
        """Gets the height_limit_layered_snow of this SnowSurfaceViewModel.  # noqa: E501


        :return: The height_limit_layered_snow of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: float
        """
        return self._height_limit_layered_snow

    @height_limit_layered_snow.setter
    def height_limit_layered_snow(self, height_limit_layered_snow):
        """Sets the height_limit_layered_snow of this SnowSurfaceViewModel.


        :param height_limit_layered_snow: The height_limit_layered_snow of this SnowSurfaceViewModel.  # noqa: E501
        :type: float
        """

        self._height_limit_layered_snow = height_limit_layered_snow

    @property
    def snow_line(self):
        """Gets the snow_line of this SnowSurfaceViewModel.  # noqa: E501


        :return: The snow_line of this SnowSurfaceViewModel.  # noqa: E501
        :rtype: int
        """
        return self._snow_line

    @snow_line.setter
    def snow_line(self, snow_line):
        """Sets the snow_line of this SnowSurfaceViewModel.


        :param snow_line: The snow_line of this SnowSurfaceViewModel.  # noqa: E501
        :type: int
        """

        self._snow_line = snow_line

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
        if issubclass(SnowSurfaceViewModel, dict):
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
        if not isinstance(other, SnowSurfaceViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
