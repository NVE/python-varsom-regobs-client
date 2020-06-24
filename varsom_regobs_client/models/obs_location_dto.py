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


class ObsLocationDto(object):
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
        'latitude': 'float',
        'longitude': 'float',
        'obs_location_id': 'int',
        'location_name': 'str',
        'utm_zone': 'int',
        'utm_east': 'int',
        'utm_north': 'int',
        'utm_source_tid': 'int',
        'forecast_region_tid': 'int',
        'municipal_no': 'str',
        'location_description': 'str',
        'comment': 'str',
        'uncertainty': 'int'
    }

    attribute_map = {
        'latitude': 'Latitude',
        'longitude': 'Longitude',
        'obs_location_id': 'ObsLocationID',
        'location_name': 'LocationName',
        'utm_zone': 'UTMZone',
        'utm_east': 'UTMEast',
        'utm_north': 'UTMNorth',
        'utm_source_tid': 'UTMSourceTID',
        'forecast_region_tid': 'ForecastRegionTID',
        'municipal_no': 'MunicipalNo',
        'location_description': 'LocationDescription',
        'comment': 'Comment',
        'uncertainty': 'Uncertainty'
    }

    def __init__(self, latitude=None, longitude=None, obs_location_id=None, location_name=None, utm_zone=None, utm_east=None, utm_north=None, utm_source_tid=None, forecast_region_tid=None, municipal_no=None, location_description=None, comment=None, uncertainty=None):  # noqa: E501
        """ObsLocationDto - a model defined in Swagger"""  # noqa: E501
        self._latitude = None
        self._longitude = None
        self._obs_location_id = None
        self._location_name = None
        self._utm_zone = None
        self._utm_east = None
        self._utm_north = None
        self._utm_source_tid = None
        self._forecast_region_tid = None
        self._municipal_no = None
        self._location_description = None
        self._comment = None
        self._uncertainty = None
        self.discriminator = None
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if obs_location_id is not None:
            self.obs_location_id = obs_location_id
        if location_name is not None:
            self.location_name = location_name
        if utm_zone is not None:
            self.utm_zone = utm_zone
        if utm_east is not None:
            self.utm_east = utm_east
        if utm_north is not None:
            self.utm_north = utm_north
        if utm_source_tid is not None:
            self.utm_source_tid = utm_source_tid
        if forecast_region_tid is not None:
            self.forecast_region_tid = forecast_region_tid
        if municipal_no is not None:
            self.municipal_no = municipal_no
        if location_description is not None:
            self.location_description = location_description
        if comment is not None:
            self.comment = comment
        if uncertainty is not None:
            self.uncertainty = uncertainty

    @property
    def latitude(self):
        """Gets the latitude of this ObsLocationDto.  # noqa: E501

        Latitude  # noqa: E501

        :return: The latitude of this ObsLocationDto.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this ObsLocationDto.

        Latitude  # noqa: E501

        :param latitude: The latitude of this ObsLocationDto.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this ObsLocationDto.  # noqa: E501

        Longitude  # noqa: E501

        :return: The longitude of this ObsLocationDto.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this ObsLocationDto.

        Longitude  # noqa: E501

        :param longitude: The longitude of this ObsLocationDto.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def obs_location_id(self):
        """Gets the obs_location_id of this ObsLocationDto.  # noqa: E501

        ObsLocationID  # noqa: E501

        :return: The obs_location_id of this ObsLocationDto.  # noqa: E501
        :rtype: int
        """
        return self._obs_location_id

    @obs_location_id.setter
    def obs_location_id(self, obs_location_id):
        """Sets the obs_location_id of this ObsLocationDto.

        ObsLocationID  # noqa: E501

        :param obs_location_id: The obs_location_id of this ObsLocationDto.  # noqa: E501
        :type: int
        """

        self._obs_location_id = obs_location_id

    @property
    def location_name(self):
        """Gets the location_name of this ObsLocationDto.  # noqa: E501

        Navn på stedet  # noqa: E501

        :return: The location_name of this ObsLocationDto.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this ObsLocationDto.

        Navn på stedet  # noqa: E501

        :param location_name: The location_name of this ObsLocationDto.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def utm_zone(self):
        """Gets the utm_zone of this ObsLocationDto.  # noqa: E501

        UTM sone. Merk at kartene i norge ligger mellom UTM32 og 34  # noqa: E501

        :return: The utm_zone of this ObsLocationDto.  # noqa: E501
        :rtype: int
        """
        return self._utm_zone

    @utm_zone.setter
    def utm_zone(self, utm_zone):
        """Sets the utm_zone of this ObsLocationDto.

        UTM sone. Merk at kartene i norge ligger mellom UTM32 og 34  # noqa: E501

        :param utm_zone: The utm_zone of this ObsLocationDto.  # noqa: E501
        :type: int
        """

        self._utm_zone = utm_zone

    @property
    def utm_east(self):
        """Gets the utm_east of this ObsLocationDto.  # noqa: E501

        Østlig UTM sone uten desimaler  # noqa: E501

        :return: The utm_east of this ObsLocationDto.  # noqa: E501
        :rtype: int
        """
        return self._utm_east

    @utm_east.setter
    def utm_east(self, utm_east):
        """Sets the utm_east of this ObsLocationDto.

        Østlig UTM sone uten desimaler  # noqa: E501

        :param utm_east: The utm_east of this ObsLocationDto.  # noqa: E501
        :type: int
        """

        self._utm_east = utm_east

    @property
    def utm_north(self):
        """Gets the utm_north of this ObsLocationDto.  # noqa: E501

        Nordlig UTM sone uten desimaler  # noqa: E501

        :return: The utm_north of this ObsLocationDto.  # noqa: E501
        :rtype: int
        """
        return self._utm_north

    @utm_north.setter
    def utm_north(self, utm_north):
        """Sets the utm_north of this ObsLocationDto.

        Nordlig UTM sone uten desimaler  # noqa: E501

        :param utm_north: The utm_north of this ObsLocationDto.  # noqa: E501
        :type: int
        """

        self._utm_north = utm_north

    @property
    def utm_source_tid(self):
        """Gets the utm_source_tid of this ObsLocationDto.  # noqa: E501

        Kildehenvisning på hvordan koordinaten er satt. (GPS i tlf, klikk i kart, osv). Verdier gitt i UTMSourceKD  # noqa: E501

        :return: The utm_source_tid of this ObsLocationDto.  # noqa: E501
        :rtype: int
        """
        return self._utm_source_tid

    @utm_source_tid.setter
    def utm_source_tid(self, utm_source_tid):
        """Sets the utm_source_tid of this ObsLocationDto.

        Kildehenvisning på hvordan koordinaten er satt. (GPS i tlf, klikk i kart, osv). Verdier gitt i UTMSourceKD  # noqa: E501

        :param utm_source_tid: The utm_source_tid of this ObsLocationDto.  # noqa: E501
        :type: int
        """

        self._utm_source_tid = utm_source_tid

    @property
    def forecast_region_tid(self):
        """Gets the forecast_region_tid of this ObsLocationDto.  # noqa: E501

        Anngir varslingsregion stedet tilhører. Varslingsregioner gitt i ForecastRegionKD. The ForecastRegionKD unique identifier  # noqa: E501

        :return: The forecast_region_tid of this ObsLocationDto.  # noqa: E501
        :rtype: int
        """
        return self._forecast_region_tid

    @forecast_region_tid.setter
    def forecast_region_tid(self, forecast_region_tid):
        """Sets the forecast_region_tid of this ObsLocationDto.

        Anngir varslingsregion stedet tilhører. Varslingsregioner gitt i ForecastRegionKD. The ForecastRegionKD unique identifier  # noqa: E501

        :param forecast_region_tid: The forecast_region_tid of this ObsLocationDto.  # noqa: E501
        :type: int
        """

        self._forecast_region_tid = forecast_region_tid

    @property
    def municipal_no(self):
        """Gets the municipal_no of this ObsLocationDto.  # noqa: E501

        Kommune nr stedet tilhører  # noqa: E501

        :return: The municipal_no of this ObsLocationDto.  # noqa: E501
        :rtype: str
        """
        return self._municipal_no

    @municipal_no.setter
    def municipal_no(self, municipal_no):
        """Sets the municipal_no of this ObsLocationDto.

        Kommune nr stedet tilhører  # noqa: E501

        :param municipal_no: The municipal_no of this ObsLocationDto.  # noqa: E501
        :type: str
        """

        self._municipal_no = municipal_no

    @property
    def location_description(self):
        """Gets the location_description of this ObsLocationDto.  # noqa: E501

        Beskriver stedet.  # noqa: E501

        :return: The location_description of this ObsLocationDto.  # noqa: E501
        :rtype: str
        """
        return self._location_description

    @location_description.setter
    def location_description(self, location_description):
        """Sets the location_description of this ObsLocationDto.

        Beskriver stedet.  # noqa: E501

        :param location_description: The location_description of this ObsLocationDto.  # noqa: E501
        :type: str
        """

        self._location_description = location_description

    @property
    def comment(self):
        """Gets the comment of this ObsLocationDto.  # noqa: E501

        Kommentarfelt brukt av systemet. Altså vises ikke til brukerne.  # noqa: E501

        :return: The comment of this ObsLocationDto.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ObsLocationDto.

        Kommentarfelt brukt av systemet. Altså vises ikke til brukerne.  # noqa: E501

        :param comment: The comment of this ObsLocationDto.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def uncertainty(self):
        """Gets the uncertainty of this ObsLocationDto.  # noqa: E501

        Usikkerhet i posisjon i meter. Anslås på web og i app hentes det fra gps.  # noqa: E501

        :return: The uncertainty of this ObsLocationDto.  # noqa: E501
        :rtype: int
        """
        return self._uncertainty

    @uncertainty.setter
    def uncertainty(self, uncertainty):
        """Sets the uncertainty of this ObsLocationDto.

        Usikkerhet i posisjon i meter. Anslås på web og i app hentes det fra gps.  # noqa: E501

        :param uncertainty: The uncertainty of this ObsLocationDto.  # noqa: E501
        :type: int
        """

        self._uncertainty = uncertainty

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
        if issubclass(ObsLocationDto, dict):
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
        if not isinstance(other, ObsLocationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
