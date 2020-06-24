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


class MyPageData(object):
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
        'guid': 'str',
        'nick_name': 'str',
        'email': 'str',
        'mob_phone_nr': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'work_place': 'str',
        'adrnr': 'int',
        'dt_reg_time': 'datetime',
        'member_of_groups': 'list[ObserverGroupDto]',
        'pending_invitations_to_groups': 'list[ObserverGroupDto]',
        'competence': 'list[ObserverCompetenceDto]',
        'number_of_observations': 'int',
        'main_geohazard_tid': 'int',
        'last_registration_date': 'datetime',
        'default_municipality': 'str'
    }

    attribute_map = {
        'guid': 'Guid',
        'nick_name': 'NickName',
        'email': 'Email',
        'mob_phone_nr': 'MobPhoneNr',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'work_place': 'WorkPlace',
        'adrnr': 'Adrnr',
        'dt_reg_time': 'DtRegTime',
        'member_of_groups': 'MemberOfGroups',
        'pending_invitations_to_groups': 'PendingInvitationsToGroups',
        'competence': 'Competence',
        'number_of_observations': 'NumberOfObservations',
        'main_geohazard_tid': 'MainGeohazardTID',
        'last_registration_date': 'LastRegistrationDate',
        'default_municipality': 'DefaultMunicipality'
    }

    def __init__(self, guid=None, nick_name=None, email=None, mob_phone_nr=None, first_name=None, last_name=None, work_place=None, adrnr=None, dt_reg_time=None, member_of_groups=None, pending_invitations_to_groups=None, competence=None, number_of_observations=None, main_geohazard_tid=None, last_registration_date=None, default_municipality=None):  # noqa: E501
        """MyPageData - a model defined in Swagger"""  # noqa: E501
        self._guid = None
        self._nick_name = None
        self._email = None
        self._mob_phone_nr = None
        self._first_name = None
        self._last_name = None
        self._work_place = None
        self._adrnr = None
        self._dt_reg_time = None
        self._member_of_groups = None
        self._pending_invitations_to_groups = None
        self._competence = None
        self._number_of_observations = None
        self._main_geohazard_tid = None
        self._last_registration_date = None
        self._default_municipality = None
        self.discriminator = None
        if guid is not None:
            self.guid = guid
        if nick_name is not None:
            self.nick_name = nick_name
        if email is not None:
            self.email = email
        if mob_phone_nr is not None:
            self.mob_phone_nr = mob_phone_nr
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if work_place is not None:
            self.work_place = work_place
        if adrnr is not None:
            self.adrnr = adrnr
        if dt_reg_time is not None:
            self.dt_reg_time = dt_reg_time
        if member_of_groups is not None:
            self.member_of_groups = member_of_groups
        if pending_invitations_to_groups is not None:
            self.pending_invitations_to_groups = pending_invitations_to_groups
        if competence is not None:
            self.competence = competence
        if number_of_observations is not None:
            self.number_of_observations = number_of_observations
        if main_geohazard_tid is not None:
            self.main_geohazard_tid = main_geohazard_tid
        if last_registration_date is not None:
            self.last_registration_date = last_registration_date
        if default_municipality is not None:
            self.default_municipality = default_municipality

    @property
    def guid(self):
        """Gets the guid of this MyPageData.  # noqa: E501


        :return: The guid of this MyPageData.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this MyPageData.


        :param guid: The guid of this MyPageData.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def nick_name(self):
        """Gets the nick_name of this MyPageData.  # noqa: E501


        :return: The nick_name of this MyPageData.  # noqa: E501
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this MyPageData.


        :param nick_name: The nick_name of this MyPageData.  # noqa: E501
        :type: str
        """

        self._nick_name = nick_name

    @property
    def email(self):
        """Gets the email of this MyPageData.  # noqa: E501


        :return: The email of this MyPageData.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MyPageData.


        :param email: The email of this MyPageData.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def mob_phone_nr(self):
        """Gets the mob_phone_nr of this MyPageData.  # noqa: E501


        :return: The mob_phone_nr of this MyPageData.  # noqa: E501
        :rtype: str
        """
        return self._mob_phone_nr

    @mob_phone_nr.setter
    def mob_phone_nr(self, mob_phone_nr):
        """Sets the mob_phone_nr of this MyPageData.


        :param mob_phone_nr: The mob_phone_nr of this MyPageData.  # noqa: E501
        :type: str
        """

        self._mob_phone_nr = mob_phone_nr

    @property
    def first_name(self):
        """Gets the first_name of this MyPageData.  # noqa: E501


        :return: The first_name of this MyPageData.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MyPageData.


        :param first_name: The first_name of this MyPageData.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this MyPageData.  # noqa: E501


        :return: The last_name of this MyPageData.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MyPageData.


        :param last_name: The last_name of this MyPageData.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def work_place(self):
        """Gets the work_place of this MyPageData.  # noqa: E501


        :return: The work_place of this MyPageData.  # noqa: E501
        :rtype: str
        """
        return self._work_place

    @work_place.setter
    def work_place(self, work_place):
        """Sets the work_place of this MyPageData.


        :param work_place: The work_place of this MyPageData.  # noqa: E501
        :type: str
        """

        self._work_place = work_place

    @property
    def adrnr(self):
        """Gets the adrnr of this MyPageData.  # noqa: E501


        :return: The adrnr of this MyPageData.  # noqa: E501
        :rtype: int
        """
        return self._adrnr

    @adrnr.setter
    def adrnr(self, adrnr):
        """Sets the adrnr of this MyPageData.


        :param adrnr: The adrnr of this MyPageData.  # noqa: E501
        :type: int
        """

        self._adrnr = adrnr

    @property
    def dt_reg_time(self):
        """Gets the dt_reg_time of this MyPageData.  # noqa: E501


        :return: The dt_reg_time of this MyPageData.  # noqa: E501
        :rtype: datetime
        """
        return self._dt_reg_time

    @dt_reg_time.setter
    def dt_reg_time(self, dt_reg_time):
        """Sets the dt_reg_time of this MyPageData.


        :param dt_reg_time: The dt_reg_time of this MyPageData.  # noqa: E501
        :type: datetime
        """

        self._dt_reg_time = dt_reg_time

    @property
    def member_of_groups(self):
        """Gets the member_of_groups of this MyPageData.  # noqa: E501


        :return: The member_of_groups of this MyPageData.  # noqa: E501
        :rtype: list[ObserverGroupDto]
        """
        return self._member_of_groups

    @member_of_groups.setter
    def member_of_groups(self, member_of_groups):
        """Sets the member_of_groups of this MyPageData.


        :param member_of_groups: The member_of_groups of this MyPageData.  # noqa: E501
        :type: list[ObserverGroupDto]
        """

        self._member_of_groups = member_of_groups

    @property
    def pending_invitations_to_groups(self):
        """Gets the pending_invitations_to_groups of this MyPageData.  # noqa: E501


        :return: The pending_invitations_to_groups of this MyPageData.  # noqa: E501
        :rtype: list[ObserverGroupDto]
        """
        return self._pending_invitations_to_groups

    @pending_invitations_to_groups.setter
    def pending_invitations_to_groups(self, pending_invitations_to_groups):
        """Sets the pending_invitations_to_groups of this MyPageData.


        :param pending_invitations_to_groups: The pending_invitations_to_groups of this MyPageData.  # noqa: E501
        :type: list[ObserverGroupDto]
        """

        self._pending_invitations_to_groups = pending_invitations_to_groups

    @property
    def competence(self):
        """Gets the competence of this MyPageData.  # noqa: E501


        :return: The competence of this MyPageData.  # noqa: E501
        :rtype: list[ObserverCompetenceDto]
        """
        return self._competence

    @competence.setter
    def competence(self, competence):
        """Sets the competence of this MyPageData.


        :param competence: The competence of this MyPageData.  # noqa: E501
        :type: list[ObserverCompetenceDto]
        """

        self._competence = competence

    @property
    def number_of_observations(self):
        """Gets the number_of_observations of this MyPageData.  # noqa: E501


        :return: The number_of_observations of this MyPageData.  # noqa: E501
        :rtype: int
        """
        return self._number_of_observations

    @number_of_observations.setter
    def number_of_observations(self, number_of_observations):
        """Sets the number_of_observations of this MyPageData.


        :param number_of_observations: The number_of_observations of this MyPageData.  # noqa: E501
        :type: int
        """

        self._number_of_observations = number_of_observations

    @property
    def main_geohazard_tid(self):
        """Gets the main_geohazard_tid of this MyPageData.  # noqa: E501


        :return: The main_geohazard_tid of this MyPageData.  # noqa: E501
        :rtype: int
        """
        return self._main_geohazard_tid

    @main_geohazard_tid.setter
    def main_geohazard_tid(self, main_geohazard_tid):
        """Sets the main_geohazard_tid of this MyPageData.


        :param main_geohazard_tid: The main_geohazard_tid of this MyPageData.  # noqa: E501
        :type: int
        """

        self._main_geohazard_tid = main_geohazard_tid

    @property
    def last_registration_date(self):
        """Gets the last_registration_date of this MyPageData.  # noqa: E501


        :return: The last_registration_date of this MyPageData.  # noqa: E501
        :rtype: datetime
        """
        return self._last_registration_date

    @last_registration_date.setter
    def last_registration_date(self, last_registration_date):
        """Sets the last_registration_date of this MyPageData.


        :param last_registration_date: The last_registration_date of this MyPageData.  # noqa: E501
        :type: datetime
        """

        self._last_registration_date = last_registration_date

    @property
    def default_municipality(self):
        """Gets the default_municipality of this MyPageData.  # noqa: E501


        :return: The default_municipality of this MyPageData.  # noqa: E501
        :rtype: str
        """
        return self._default_municipality

    @default_municipality.setter
    def default_municipality(self, default_municipality):
        """Sets the default_municipality of this MyPageData.


        :param default_municipality: The default_municipality of this MyPageData.  # noqa: E501
        :type: str
        """

        self._default_municipality = default_municipality

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
        if issubclass(MyPageData, dict):
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
        if not isinstance(other, MyPageData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other