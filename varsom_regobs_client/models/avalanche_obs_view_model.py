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


class AvalancheObsViewModel(object):
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
        'dt_avalanche_time': 'datetime',
        'aspect': 'int',
        'height_start_zone': 'int',
        'height_stop_zone': 'int',
        'destructive_size_tid': 'int',
        'destructive_size_name': 'str',
        'avalanche_trigger_tid': 'int',
        'avalanche_trigger_name': 'str',
        'avalanche_tid': 'int',
        'avalanche_name': 'str',
        'terrain_start_zone_tid': 'int',
        'terrain_start_zone_name': 'str',
        'utm_zone_stop': 'int',
        'utm_east_stop': 'int',
        'utm_north_stop': 'int',
        'utm_east_start': 'int',
        'snow_line': 'int',
        'valid_exposition': 'str',
        'aval_cause_tid': 'int',
        'aval_cause_name': 'str',
        'fracture_height': 'int',
        'fracture_width': 'int',
        'trajectory': 'str',
        'start_lat': 'float',
        'start_long': 'float',
        'stop_lat': 'float',
        'stop_long': 'float',
        'comment': 'str',
        'utm_north_start': 'int'
    }

    attribute_map = {
        'dt_avalanche_time': 'DtAvalancheTime',
        'aspect': 'Aspect',
        'height_start_zone': 'HeightStartZone',
        'height_stop_zone': 'HeightStopZone',
        'destructive_size_tid': 'DestructiveSizeTID',
        'destructive_size_name': 'DestructiveSizeName',
        'avalanche_trigger_tid': 'AvalancheTriggerTID',
        'avalanche_trigger_name': 'AvalancheTriggerName',
        'avalanche_tid': 'AvalancheTID',
        'avalanche_name': 'AvalancheName',
        'terrain_start_zone_tid': 'TerrainStartZoneTID',
        'terrain_start_zone_name': 'TerrainStartZoneName',
        'utm_zone_stop': 'UTMZoneStop',
        'utm_east_stop': 'UTMEastStop',
        'utm_north_stop': 'UTMNorthStop',
        'utm_east_start': 'UTMEastStart',
        'snow_line': 'SnowLine',
        'valid_exposition': 'ValidExposition',
        'aval_cause_tid': 'AvalCauseTID',
        'aval_cause_name': 'AvalCauseName',
        'fracture_height': 'FractureHeight',
        'fracture_width': 'FractureWidth',
        'trajectory': 'Trajectory',
        'start_lat': 'StartLat',
        'start_long': 'StartLong',
        'stop_lat': 'StopLat',
        'stop_long': 'StopLong',
        'comment': 'Comment',
        'utm_north_start': 'UTMNorthStart'
    }

    def __init__(self, dt_avalanche_time=None, aspect=None, height_start_zone=None, height_stop_zone=None, destructive_size_tid=None, destructive_size_name=None, avalanche_trigger_tid=None, avalanche_trigger_name=None, avalanche_tid=None, avalanche_name=None, terrain_start_zone_tid=None, terrain_start_zone_name=None, utm_zone_stop=None, utm_east_stop=None, utm_north_stop=None, utm_east_start=None, snow_line=None, valid_exposition=None, aval_cause_tid=None, aval_cause_name=None, fracture_height=None, fracture_width=None, trajectory=None, start_lat=None, start_long=None, stop_lat=None, stop_long=None, comment=None, utm_north_start=None):  # noqa: E501
        """AvalancheObsViewModel - a model defined in Swagger"""  # noqa: E501
        self._dt_avalanche_time = None
        self._aspect = None
        self._height_start_zone = None
        self._height_stop_zone = None
        self._destructive_size_tid = None
        self._destructive_size_name = None
        self._avalanche_trigger_tid = None
        self._avalanche_trigger_name = None
        self._avalanche_tid = None
        self._avalanche_name = None
        self._terrain_start_zone_tid = None
        self._terrain_start_zone_name = None
        self._utm_zone_stop = None
        self._utm_east_stop = None
        self._utm_north_stop = None
        self._utm_east_start = None
        self._snow_line = None
        self._valid_exposition = None
        self._aval_cause_tid = None
        self._aval_cause_name = None
        self._fracture_height = None
        self._fracture_width = None
        self._trajectory = None
        self._start_lat = None
        self._start_long = None
        self._stop_lat = None
        self._stop_long = None
        self._comment = None
        self._utm_north_start = None
        self.discriminator = None
        if dt_avalanche_time is not None:
            self.dt_avalanche_time = dt_avalanche_time
        if aspect is not None:
            self.aspect = aspect
        if height_start_zone is not None:
            self.height_start_zone = height_start_zone
        if height_stop_zone is not None:
            self.height_stop_zone = height_stop_zone
        if destructive_size_tid is not None:
            self.destructive_size_tid = destructive_size_tid
        if destructive_size_name is not None:
            self.destructive_size_name = destructive_size_name
        if avalanche_trigger_tid is not None:
            self.avalanche_trigger_tid = avalanche_trigger_tid
        if avalanche_trigger_name is not None:
            self.avalanche_trigger_name = avalanche_trigger_name
        if avalanche_tid is not None:
            self.avalanche_tid = avalanche_tid
        if avalanche_name is not None:
            self.avalanche_name = avalanche_name
        if terrain_start_zone_tid is not None:
            self.terrain_start_zone_tid = terrain_start_zone_tid
        if terrain_start_zone_name is not None:
            self.terrain_start_zone_name = terrain_start_zone_name
        if utm_zone_stop is not None:
            self.utm_zone_stop = utm_zone_stop
        if utm_east_stop is not None:
            self.utm_east_stop = utm_east_stop
        if utm_north_stop is not None:
            self.utm_north_stop = utm_north_stop
        if utm_east_start is not None:
            self.utm_east_start = utm_east_start
        if snow_line is not None:
            self.snow_line = snow_line
        if valid_exposition is not None:
            self.valid_exposition = valid_exposition
        if aval_cause_tid is not None:
            self.aval_cause_tid = aval_cause_tid
        if aval_cause_name is not None:
            self.aval_cause_name = aval_cause_name
        if fracture_height is not None:
            self.fracture_height = fracture_height
        if fracture_width is not None:
            self.fracture_width = fracture_width
        if trajectory is not None:
            self.trajectory = trajectory
        if start_lat is not None:
            self.start_lat = start_lat
        if start_long is not None:
            self.start_long = start_long
        if stop_lat is not None:
            self.stop_lat = stop_lat
        if stop_long is not None:
            self.stop_long = stop_long
        if comment is not None:
            self.comment = comment
        if utm_north_start is not None:
            self.utm_north_start = utm_north_start

    @property
    def dt_avalanche_time(self):
        """Gets the dt_avalanche_time of this AvalancheObsViewModel.  # noqa: E501


        :return: The dt_avalanche_time of this AvalancheObsViewModel.  # noqa: E501
        :rtype: datetime
        """
        return self._dt_avalanche_time

    @dt_avalanche_time.setter
    def dt_avalanche_time(self, dt_avalanche_time):
        """Sets the dt_avalanche_time of this AvalancheObsViewModel.


        :param dt_avalanche_time: The dt_avalanche_time of this AvalancheObsViewModel.  # noqa: E501
        :type: datetime
        """

        self._dt_avalanche_time = dt_avalanche_time

    @property
    def aspect(self):
        """Gets the aspect of this AvalancheObsViewModel.  # noqa: E501


        :return: The aspect of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aspect

    @aspect.setter
    def aspect(self, aspect):
        """Sets the aspect of this AvalancheObsViewModel.


        :param aspect: The aspect of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._aspect = aspect

    @property
    def height_start_zone(self):
        """Gets the height_start_zone of this AvalancheObsViewModel.  # noqa: E501


        :return: The height_start_zone of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._height_start_zone

    @height_start_zone.setter
    def height_start_zone(self, height_start_zone):
        """Sets the height_start_zone of this AvalancheObsViewModel.


        :param height_start_zone: The height_start_zone of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._height_start_zone = height_start_zone

    @property
    def height_stop_zone(self):
        """Gets the height_stop_zone of this AvalancheObsViewModel.  # noqa: E501


        :return: The height_stop_zone of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._height_stop_zone

    @height_stop_zone.setter
    def height_stop_zone(self, height_stop_zone):
        """Sets the height_stop_zone of this AvalancheObsViewModel.


        :param height_stop_zone: The height_stop_zone of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._height_stop_zone = height_stop_zone

    @property
    def destructive_size_tid(self):
        """Gets the destructive_size_tid of this AvalancheObsViewModel.  # noqa: E501


        :return: The destructive_size_tid of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._destructive_size_tid

    @destructive_size_tid.setter
    def destructive_size_tid(self, destructive_size_tid):
        """Sets the destructive_size_tid of this AvalancheObsViewModel.


        :param destructive_size_tid: The destructive_size_tid of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._destructive_size_tid = destructive_size_tid

    @property
    def destructive_size_name(self):
        """Gets the destructive_size_name of this AvalancheObsViewModel.  # noqa: E501


        :return: The destructive_size_name of this AvalancheObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._destructive_size_name

    @destructive_size_name.setter
    def destructive_size_name(self, destructive_size_name):
        """Sets the destructive_size_name of this AvalancheObsViewModel.


        :param destructive_size_name: The destructive_size_name of this AvalancheObsViewModel.  # noqa: E501
        :type: str
        """

        self._destructive_size_name = destructive_size_name

    @property
    def avalanche_trigger_tid(self):
        """Gets the avalanche_trigger_tid of this AvalancheObsViewModel.  # noqa: E501


        :return: The avalanche_trigger_tid of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._avalanche_trigger_tid

    @avalanche_trigger_tid.setter
    def avalanche_trigger_tid(self, avalanche_trigger_tid):
        """Sets the avalanche_trigger_tid of this AvalancheObsViewModel.


        :param avalanche_trigger_tid: The avalanche_trigger_tid of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._avalanche_trigger_tid = avalanche_trigger_tid

    @property
    def avalanche_trigger_name(self):
        """Gets the avalanche_trigger_name of this AvalancheObsViewModel.  # noqa: E501


        :return: The avalanche_trigger_name of this AvalancheObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._avalanche_trigger_name

    @avalanche_trigger_name.setter
    def avalanche_trigger_name(self, avalanche_trigger_name):
        """Sets the avalanche_trigger_name of this AvalancheObsViewModel.


        :param avalanche_trigger_name: The avalanche_trigger_name of this AvalancheObsViewModel.  # noqa: E501
        :type: str
        """

        self._avalanche_trigger_name = avalanche_trigger_name

    @property
    def avalanche_tid(self):
        """Gets the avalanche_tid of this AvalancheObsViewModel.  # noqa: E501


        :return: The avalanche_tid of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._avalanche_tid

    @avalanche_tid.setter
    def avalanche_tid(self, avalanche_tid):
        """Sets the avalanche_tid of this AvalancheObsViewModel.


        :param avalanche_tid: The avalanche_tid of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._avalanche_tid = avalanche_tid

    @property
    def avalanche_name(self):
        """Gets the avalanche_name of this AvalancheObsViewModel.  # noqa: E501


        :return: The avalanche_name of this AvalancheObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._avalanche_name

    @avalanche_name.setter
    def avalanche_name(self, avalanche_name):
        """Sets the avalanche_name of this AvalancheObsViewModel.


        :param avalanche_name: The avalanche_name of this AvalancheObsViewModel.  # noqa: E501
        :type: str
        """

        self._avalanche_name = avalanche_name

    @property
    def terrain_start_zone_tid(self):
        """Gets the terrain_start_zone_tid of this AvalancheObsViewModel.  # noqa: E501


        :return: The terrain_start_zone_tid of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._terrain_start_zone_tid

    @terrain_start_zone_tid.setter
    def terrain_start_zone_tid(self, terrain_start_zone_tid):
        """Sets the terrain_start_zone_tid of this AvalancheObsViewModel.


        :param terrain_start_zone_tid: The terrain_start_zone_tid of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._terrain_start_zone_tid = terrain_start_zone_tid

    @property
    def terrain_start_zone_name(self):
        """Gets the terrain_start_zone_name of this AvalancheObsViewModel.  # noqa: E501


        :return: The terrain_start_zone_name of this AvalancheObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._terrain_start_zone_name

    @terrain_start_zone_name.setter
    def terrain_start_zone_name(self, terrain_start_zone_name):
        """Sets the terrain_start_zone_name of this AvalancheObsViewModel.


        :param terrain_start_zone_name: The terrain_start_zone_name of this AvalancheObsViewModel.  # noqa: E501
        :type: str
        """

        self._terrain_start_zone_name = terrain_start_zone_name

    @property
    def utm_zone_stop(self):
        """Gets the utm_zone_stop of this AvalancheObsViewModel.  # noqa: E501


        :return: The utm_zone_stop of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._utm_zone_stop

    @utm_zone_stop.setter
    def utm_zone_stop(self, utm_zone_stop):
        """Sets the utm_zone_stop of this AvalancheObsViewModel.


        :param utm_zone_stop: The utm_zone_stop of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._utm_zone_stop = utm_zone_stop

    @property
    def utm_east_stop(self):
        """Gets the utm_east_stop of this AvalancheObsViewModel.  # noqa: E501


        :return: The utm_east_stop of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._utm_east_stop

    @utm_east_stop.setter
    def utm_east_stop(self, utm_east_stop):
        """Sets the utm_east_stop of this AvalancheObsViewModel.


        :param utm_east_stop: The utm_east_stop of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._utm_east_stop = utm_east_stop

    @property
    def utm_north_stop(self):
        """Gets the utm_north_stop of this AvalancheObsViewModel.  # noqa: E501


        :return: The utm_north_stop of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._utm_north_stop

    @utm_north_stop.setter
    def utm_north_stop(self, utm_north_stop):
        """Sets the utm_north_stop of this AvalancheObsViewModel.


        :param utm_north_stop: The utm_north_stop of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._utm_north_stop = utm_north_stop

    @property
    def utm_east_start(self):
        """Gets the utm_east_start of this AvalancheObsViewModel.  # noqa: E501


        :return: The utm_east_start of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._utm_east_start

    @utm_east_start.setter
    def utm_east_start(self, utm_east_start):
        """Sets the utm_east_start of this AvalancheObsViewModel.


        :param utm_east_start: The utm_east_start of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._utm_east_start = utm_east_start

    @property
    def snow_line(self):
        """Gets the snow_line of this AvalancheObsViewModel.  # noqa: E501


        :return: The snow_line of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._snow_line

    @snow_line.setter
    def snow_line(self, snow_line):
        """Sets the snow_line of this AvalancheObsViewModel.


        :param snow_line: The snow_line of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._snow_line = snow_line

    @property
    def valid_exposition(self):
        """Gets the valid_exposition of this AvalancheObsViewModel.  # noqa: E501


        :return: The valid_exposition of this AvalancheObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._valid_exposition

    @valid_exposition.setter
    def valid_exposition(self, valid_exposition):
        """Sets the valid_exposition of this AvalancheObsViewModel.


        :param valid_exposition: The valid_exposition of this AvalancheObsViewModel.  # noqa: E501
        :type: str
        """

        self._valid_exposition = valid_exposition

    @property
    def aval_cause_tid(self):
        """Gets the aval_cause_tid of this AvalancheObsViewModel.  # noqa: E501


        :return: The aval_cause_tid of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_tid

    @aval_cause_tid.setter
    def aval_cause_tid(self, aval_cause_tid):
        """Sets the aval_cause_tid of this AvalancheObsViewModel.


        :param aval_cause_tid: The aval_cause_tid of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._aval_cause_tid = aval_cause_tid

    @property
    def aval_cause_name(self):
        """Gets the aval_cause_name of this AvalancheObsViewModel.  # noqa: E501


        :return: The aval_cause_name of this AvalancheObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._aval_cause_name

    @aval_cause_name.setter
    def aval_cause_name(self, aval_cause_name):
        """Sets the aval_cause_name of this AvalancheObsViewModel.


        :param aval_cause_name: The aval_cause_name of this AvalancheObsViewModel.  # noqa: E501
        :type: str
        """

        self._aval_cause_name = aval_cause_name

    @property
    def fracture_height(self):
        """Gets the fracture_height of this AvalancheObsViewModel.  # noqa: E501


        :return: The fracture_height of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._fracture_height

    @fracture_height.setter
    def fracture_height(self, fracture_height):
        """Sets the fracture_height of this AvalancheObsViewModel.


        :param fracture_height: The fracture_height of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._fracture_height = fracture_height

    @property
    def fracture_width(self):
        """Gets the fracture_width of this AvalancheObsViewModel.  # noqa: E501


        :return: The fracture_width of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._fracture_width

    @fracture_width.setter
    def fracture_width(self, fracture_width):
        """Sets the fracture_width of this AvalancheObsViewModel.


        :param fracture_width: The fracture_width of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._fracture_width = fracture_width

    @property
    def trajectory(self):
        """Gets the trajectory of this AvalancheObsViewModel.  # noqa: E501


        :return: The trajectory of this AvalancheObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._trajectory

    @trajectory.setter
    def trajectory(self, trajectory):
        """Sets the trajectory of this AvalancheObsViewModel.


        :param trajectory: The trajectory of this AvalancheObsViewModel.  # noqa: E501
        :type: str
        """

        self._trajectory = trajectory

    @property
    def start_lat(self):
        """Gets the start_lat of this AvalancheObsViewModel.  # noqa: E501


        :return: The start_lat of this AvalancheObsViewModel.  # noqa: E501
        :rtype: float
        """
        return self._start_lat

    @start_lat.setter
    def start_lat(self, start_lat):
        """Sets the start_lat of this AvalancheObsViewModel.


        :param start_lat: The start_lat of this AvalancheObsViewModel.  # noqa: E501
        :type: float
        """

        self._start_lat = start_lat

    @property
    def start_long(self):
        """Gets the start_long of this AvalancheObsViewModel.  # noqa: E501


        :return: The start_long of this AvalancheObsViewModel.  # noqa: E501
        :rtype: float
        """
        return self._start_long

    @start_long.setter
    def start_long(self, start_long):
        """Sets the start_long of this AvalancheObsViewModel.


        :param start_long: The start_long of this AvalancheObsViewModel.  # noqa: E501
        :type: float
        """

        self._start_long = start_long

    @property
    def stop_lat(self):
        """Gets the stop_lat of this AvalancheObsViewModel.  # noqa: E501


        :return: The stop_lat of this AvalancheObsViewModel.  # noqa: E501
        :rtype: float
        """
        return self._stop_lat

    @stop_lat.setter
    def stop_lat(self, stop_lat):
        """Sets the stop_lat of this AvalancheObsViewModel.


        :param stop_lat: The stop_lat of this AvalancheObsViewModel.  # noqa: E501
        :type: float
        """

        self._stop_lat = stop_lat

    @property
    def stop_long(self):
        """Gets the stop_long of this AvalancheObsViewModel.  # noqa: E501


        :return: The stop_long of this AvalancheObsViewModel.  # noqa: E501
        :rtype: float
        """
        return self._stop_long

    @stop_long.setter
    def stop_long(self, stop_long):
        """Sets the stop_long of this AvalancheObsViewModel.


        :param stop_long: The stop_long of this AvalancheObsViewModel.  # noqa: E501
        :type: float
        """

        self._stop_long = stop_long

    @property
    def comment(self):
        """Gets the comment of this AvalancheObsViewModel.  # noqa: E501


        :return: The comment of this AvalancheObsViewModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AvalancheObsViewModel.


        :param comment: The comment of this AvalancheObsViewModel.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def utm_north_start(self):
        """Gets the utm_north_start of this AvalancheObsViewModel.  # noqa: E501


        :return: The utm_north_start of this AvalancheObsViewModel.  # noqa: E501
        :rtype: int
        """
        return self._utm_north_start

    @utm_north_start.setter
    def utm_north_start(self, utm_north_start):
        """Sets the utm_north_start of this AvalancheObsViewModel.


        :param utm_north_start: The utm_north_start of this AvalancheObsViewModel.  # noqa: E501
        :type: int
        """

        self._utm_north_start = utm_north_start

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
        if issubclass(AvalancheObsViewModel, dict):
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
        if not isinstance(other, AvalancheObsViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
