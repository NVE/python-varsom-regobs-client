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


class AvalancheEvaluation2ViewModel(object):
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
        'avalanche_danger_name': 'str',
        'valid_exposition': 'str',
        'comment': 'str',
        'avalanche_evaluation': 'str',
        'avalanche_development': 'str',
        'exposed_height1': 'int',
        'exposed_height2': 'int',
        'exposed_height_combo_tid': 'int',
        'exposed_height_combo_name': 'str',
        'exposed_climate_tid': 'int',
        'exposed_climate_name': 'str',
        'avalanche_danger_tid': 'int',
        'avalanche_eval_problems': 'list[AvalancheEvalProblemViewModel]'
    }

    attribute_map = {
        'avalanche_danger_name': 'AvalancheDangerName',
        'valid_exposition': 'ValidExposition',
        'comment': 'Comment',
        'avalanche_evaluation': 'AvalancheEvaluation',
        'avalanche_development': 'AvalancheDevelopment',
        'exposed_height1': 'ExposedHeight1',
        'exposed_height2': 'ExposedHeight2',
        'exposed_height_combo_tid': 'ExposedHeightComboTID',
        'exposed_height_combo_name': 'ExposedHeightComboName',
        'exposed_climate_tid': 'ExposedClimateTID',
        'exposed_climate_name': 'ExposedClimateName',
        'avalanche_danger_tid': 'AvalancheDangerTID',
        'avalanche_eval_problems': 'AvalancheEvalProblems'
    }

    def __init__(self, avalanche_danger_name=None, valid_exposition=None, comment=None, avalanche_evaluation=None, avalanche_development=None, exposed_height1=None, exposed_height2=None, exposed_height_combo_tid=None, exposed_height_combo_name=None, exposed_climate_tid=None, exposed_climate_name=None, avalanche_danger_tid=None, avalanche_eval_problems=None):  # noqa: E501
        """AvalancheEvaluation2ViewModel - a model defined in Swagger"""  # noqa: E501
        self._avalanche_danger_name = None
        self._valid_exposition = None
        self._comment = None
        self._avalanche_evaluation = None
        self._avalanche_development = None
        self._exposed_height1 = None
        self._exposed_height2 = None
        self._exposed_height_combo_tid = None
        self._exposed_height_combo_name = None
        self._exposed_climate_tid = None
        self._exposed_climate_name = None
        self._avalanche_danger_tid = None
        self._avalanche_eval_problems = None
        self.discriminator = None
        if avalanche_danger_name is not None:
            self.avalanche_danger_name = avalanche_danger_name
        if valid_exposition is not None:
            self.valid_exposition = valid_exposition
        if comment is not None:
            self.comment = comment
        if avalanche_evaluation is not None:
            self.avalanche_evaluation = avalanche_evaluation
        if avalanche_development is not None:
            self.avalanche_development = avalanche_development
        if exposed_height1 is not None:
            self.exposed_height1 = exposed_height1
        if exposed_height2 is not None:
            self.exposed_height2 = exposed_height2
        if exposed_height_combo_tid is not None:
            self.exposed_height_combo_tid = exposed_height_combo_tid
        if exposed_height_combo_name is not None:
            self.exposed_height_combo_name = exposed_height_combo_name
        if exposed_climate_tid is not None:
            self.exposed_climate_tid = exposed_climate_tid
        if exposed_climate_name is not None:
            self.exposed_climate_name = exposed_climate_name
        if avalanche_danger_tid is not None:
            self.avalanche_danger_tid = avalanche_danger_tid
        if avalanche_eval_problems is not None:
            self.avalanche_eval_problems = avalanche_eval_problems

    @property
    def avalanche_danger_name(self):
        """Gets the avalanche_danger_name of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The avalanche_danger_name of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._avalanche_danger_name

    @avalanche_danger_name.setter
    def avalanche_danger_name(self, avalanche_danger_name):
        """Sets the avalanche_danger_name of this AvalancheEvaluation2ViewModel.


        :param avalanche_danger_name: The avalanche_danger_name of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: str
        """

        self._avalanche_danger_name = avalanche_danger_name

    @property
    def valid_exposition(self):
        """Gets the valid_exposition of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The valid_exposition of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._valid_exposition

    @valid_exposition.setter
    def valid_exposition(self, valid_exposition):
        """Sets the valid_exposition of this AvalancheEvaluation2ViewModel.


        :param valid_exposition: The valid_exposition of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: str
        """

        self._valid_exposition = valid_exposition

    @property
    def comment(self):
        """Gets the comment of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The comment of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AvalancheEvaluation2ViewModel.


        :param comment: The comment of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def avalanche_evaluation(self):
        """Gets the avalanche_evaluation of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The avalanche_evaluation of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._avalanche_evaluation

    @avalanche_evaluation.setter
    def avalanche_evaluation(self, avalanche_evaluation):
        """Sets the avalanche_evaluation of this AvalancheEvaluation2ViewModel.


        :param avalanche_evaluation: The avalanche_evaluation of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: str
        """

        self._avalanche_evaluation = avalanche_evaluation

    @property
    def avalanche_development(self):
        """Gets the avalanche_development of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The avalanche_development of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._avalanche_development

    @avalanche_development.setter
    def avalanche_development(self, avalanche_development):
        """Sets the avalanche_development of this AvalancheEvaluation2ViewModel.


        :param avalanche_development: The avalanche_development of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: str
        """

        self._avalanche_development = avalanche_development

    @property
    def exposed_height1(self):
        """Gets the exposed_height1 of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The exposed_height1 of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height1

    @exposed_height1.setter
    def exposed_height1(self, exposed_height1):
        """Sets the exposed_height1 of this AvalancheEvaluation2ViewModel.


        :param exposed_height1: The exposed_height1 of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: int
        """

        self._exposed_height1 = exposed_height1

    @property
    def exposed_height2(self):
        """Gets the exposed_height2 of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The exposed_height2 of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height2

    @exposed_height2.setter
    def exposed_height2(self, exposed_height2):
        """Sets the exposed_height2 of this AvalancheEvaluation2ViewModel.


        :param exposed_height2: The exposed_height2 of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: int
        """

        self._exposed_height2 = exposed_height2

    @property
    def exposed_height_combo_tid(self):
        """Gets the exposed_height_combo_tid of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The exposed_height_combo_tid of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height_combo_tid

    @exposed_height_combo_tid.setter
    def exposed_height_combo_tid(self, exposed_height_combo_tid):
        """Sets the exposed_height_combo_tid of this AvalancheEvaluation2ViewModel.


        :param exposed_height_combo_tid: The exposed_height_combo_tid of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: int
        """

        self._exposed_height_combo_tid = exposed_height_combo_tid

    @property
    def exposed_height_combo_name(self):
        """Gets the exposed_height_combo_name of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The exposed_height_combo_name of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._exposed_height_combo_name

    @exposed_height_combo_name.setter
    def exposed_height_combo_name(self, exposed_height_combo_name):
        """Sets the exposed_height_combo_name of this AvalancheEvaluation2ViewModel.


        :param exposed_height_combo_name: The exposed_height_combo_name of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: str
        """

        self._exposed_height_combo_name = exposed_height_combo_name

    @property
    def exposed_climate_tid(self):
        """Gets the exposed_climate_tid of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The exposed_climate_tid of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._exposed_climate_tid

    @exposed_climate_tid.setter
    def exposed_climate_tid(self, exposed_climate_tid):
        """Sets the exposed_climate_tid of this AvalancheEvaluation2ViewModel.


        :param exposed_climate_tid: The exposed_climate_tid of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: int
        """

        self._exposed_climate_tid = exposed_climate_tid

    @property
    def exposed_climate_name(self):
        """Gets the exposed_climate_name of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The exposed_climate_name of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._exposed_climate_name

    @exposed_climate_name.setter
    def exposed_climate_name(self, exposed_climate_name):
        """Sets the exposed_climate_name of this AvalancheEvaluation2ViewModel.


        :param exposed_climate_name: The exposed_climate_name of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: str
        """

        self._exposed_climate_name = exposed_climate_name

    @property
    def avalanche_danger_tid(self):
        """Gets the avalanche_danger_tid of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The avalanche_danger_tid of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._avalanche_danger_tid

    @avalanche_danger_tid.setter
    def avalanche_danger_tid(self, avalanche_danger_tid):
        """Sets the avalanche_danger_tid of this AvalancheEvaluation2ViewModel.


        :param avalanche_danger_tid: The avalanche_danger_tid of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: int
        """

        self._avalanche_danger_tid = avalanche_danger_tid

    @property
    def avalanche_eval_problems(self):
        """Gets the avalanche_eval_problems of this AvalancheEvaluation2ViewModel.  # noqa: E501


        :return: The avalanche_eval_problems of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :rtype: list[AvalancheEvalProblemViewModel]
        """
        return self._avalanche_eval_problems

    @avalanche_eval_problems.setter
    def avalanche_eval_problems(self, avalanche_eval_problems):
        """Sets the avalanche_eval_problems of this AvalancheEvaluation2ViewModel.


        :param avalanche_eval_problems: The avalanche_eval_problems of this AvalancheEvaluation2ViewModel.  # noqa: E501
        :type: list[AvalancheEvalProblemViewModel]
        """

        self._avalanche_eval_problems = avalanche_eval_problems

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
        if issubclass(AvalancheEvaluation2ViewModel, dict):
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
        if not isinstance(other, AvalancheEvaluation2ViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
