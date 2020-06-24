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


class AvalancheEvalProblem2Dto(object):
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
        'avalanche_eval_problem2_id': 'int',
        'avalanche_ext_tid': 'int',
        'aval_probability_tid': 'int',
        'aval_trigger_simple_tid': 'int',
        'destructive_size_tid': 'int',
        'aval_cause_tid': 'int',
        'aval_cause_depth_tid': 'int',
        'aval_cause_attributes': 'int',
        'valid_exposition': 'str',
        'exposed_height1': 'int',
        'exposed_height2': 'int',
        'exposed_height_combo_tid': 'int',
        'aval_propagation_tid': 'int',
        'comment': 'str'
    }

    attribute_map = {
        'avalanche_eval_problem2_id': 'AvalancheEvalProblem2ID',
        'avalanche_ext_tid': 'AvalancheExtTID',
        'aval_probability_tid': 'AvalProbabilityTID',
        'aval_trigger_simple_tid': 'AvalTriggerSimpleTID',
        'destructive_size_tid': 'DestructiveSizeTID',
        'aval_cause_tid': 'AvalCauseTID',
        'aval_cause_depth_tid': 'AvalCauseDepthTID',
        'aval_cause_attributes': 'AvalCauseAttributes',
        'valid_exposition': 'ValidExposition',
        'exposed_height1': 'ExposedHeight1',
        'exposed_height2': 'ExposedHeight2',
        'exposed_height_combo_tid': 'ExposedHeightComboTID',
        'aval_propagation_tid': 'AvalPropagationTID',
        'comment': 'Comment'
    }

    def __init__(self, avalanche_eval_problem2_id=None, avalanche_ext_tid=None, aval_probability_tid=None, aval_trigger_simple_tid=None, destructive_size_tid=None, aval_cause_tid=None, aval_cause_depth_tid=None, aval_cause_attributes=None, valid_exposition=None, exposed_height1=None, exposed_height2=None, exposed_height_combo_tid=None, aval_propagation_tid=None, comment=None):  # noqa: E501
        """AvalancheEvalProblem2Dto - a model defined in Swagger"""  # noqa: E501
        self._avalanche_eval_problem2_id = None
        self._avalanche_ext_tid = None
        self._aval_probability_tid = None
        self._aval_trigger_simple_tid = None
        self._destructive_size_tid = None
        self._aval_cause_tid = None
        self._aval_cause_depth_tid = None
        self._aval_cause_attributes = None
        self._valid_exposition = None
        self._exposed_height1 = None
        self._exposed_height2 = None
        self._exposed_height_combo_tid = None
        self._aval_propagation_tid = None
        self._comment = None
        self.discriminator = None
        if avalanche_eval_problem2_id is not None:
            self.avalanche_eval_problem2_id = avalanche_eval_problem2_id
        if avalanche_ext_tid is not None:
            self.avalanche_ext_tid = avalanche_ext_tid
        if aval_probability_tid is not None:
            self.aval_probability_tid = aval_probability_tid
        if aval_trigger_simple_tid is not None:
            self.aval_trigger_simple_tid = aval_trigger_simple_tid
        if destructive_size_tid is not None:
            self.destructive_size_tid = destructive_size_tid
        if aval_cause_tid is not None:
            self.aval_cause_tid = aval_cause_tid
        if aval_cause_depth_tid is not None:
            self.aval_cause_depth_tid = aval_cause_depth_tid
        if aval_cause_attributes is not None:
            self.aval_cause_attributes = aval_cause_attributes
        if valid_exposition is not None:
            self.valid_exposition = valid_exposition
        if exposed_height1 is not None:
            self.exposed_height1 = exposed_height1
        if exposed_height2 is not None:
            self.exposed_height2 = exposed_height2
        if exposed_height_combo_tid is not None:
            self.exposed_height_combo_tid = exposed_height_combo_tid
        if aval_propagation_tid is not None:
            self.aval_propagation_tid = aval_propagation_tid
        if comment is not None:
            self.comment = comment

    @property
    def avalanche_eval_problem2_id(self):
        """Gets the avalanche_eval_problem2_id of this AvalancheEvalProblem2Dto.  # noqa: E501

        Unik id på denne tabellen da flere er mulig pr RegID.  # noqa: E501

        :return: The avalanche_eval_problem2_id of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._avalanche_eval_problem2_id

    @avalanche_eval_problem2_id.setter
    def avalanche_eval_problem2_id(self, avalanche_eval_problem2_id):
        """Sets the avalanche_eval_problem2_id of this AvalancheEvalProblem2Dto.

        Unik id på denne tabellen da flere er mulig pr RegID.  # noqa: E501

        :param avalanche_eval_problem2_id: The avalanche_eval_problem2_id of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._avalanche_eval_problem2_id = avalanche_eval_problem2_id

    @property
    def avalanche_ext_tid(self):
        """Gets the avalanche_ext_tid of this AvalancheEvalProblem2Dto.  # noqa: E501

        Skredtype. I appen er dette 1. felt under skredproblem. The AvalancheExtKD unique identifier  # noqa: E501

        :return: The avalanche_ext_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._avalanche_ext_tid

    @avalanche_ext_tid.setter
    def avalanche_ext_tid(self, avalanche_ext_tid):
        """Sets the avalanche_ext_tid of this AvalancheEvalProblem2Dto.

        Skredtype. I appen er dette 1. felt under skredproblem. The AvalancheExtKD unique identifier  # noqa: E501

        :param avalanche_ext_tid: The avalanche_ext_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._avalanche_ext_tid = avalanche_ext_tid

    @property
    def aval_probability_tid(self):
        """Gets the aval_probability_tid of this AvalancheEvalProblem2Dto.  # noqa: E501

        Sannsynlighet for skred. The AvalProbabilityKD unique identifier  # noqa: E501

        :return: The aval_probability_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._aval_probability_tid

    @aval_probability_tid.setter
    def aval_probability_tid(self, aval_probability_tid):
        """Sets the aval_probability_tid of this AvalancheEvalProblem2Dto.

        Sannsynlighet for skred. The AvalProbabilityKD unique identifier  # noqa: E501

        :param aval_probability_tid: The aval_probability_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._aval_probability_tid = aval_probability_tid

    @property
    def aval_trigger_simple_tid(self):
        """Gets the aval_trigger_simple_tid of this AvalancheEvalProblem2Dto.  # noqa: E501

        The AvalTriggerSimpleKD unique identifier  # noqa: E501

        :return: The aval_trigger_simple_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._aval_trigger_simple_tid

    @aval_trigger_simple_tid.setter
    def aval_trigger_simple_tid(self, aval_trigger_simple_tid):
        """Sets the aval_trigger_simple_tid of this AvalancheEvalProblem2Dto.

        The AvalTriggerSimpleKD unique identifier  # noqa: E501

        :param aval_trigger_simple_tid: The aval_trigger_simple_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._aval_trigger_simple_tid = aval_trigger_simple_tid

    @property
    def destructive_size_tid(self):
        """Gets the destructive_size_tid of this AvalancheEvalProblem2Dto.  # noqa: E501

        Sannsynlig tilleggsbelastning for å utløse skred. The DestructiveSizeKD unique identifier  # noqa: E501

        :return: The destructive_size_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._destructive_size_tid

    @destructive_size_tid.setter
    def destructive_size_tid(self, destructive_size_tid):
        """Sets the destructive_size_tid of this AvalancheEvalProblem2Dto.

        Sannsynlig tilleggsbelastning for å utløse skred. The DestructiveSizeKD unique identifier  # noqa: E501

        :param destructive_size_tid: The destructive_size_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._destructive_size_tid = destructive_size_tid

    @property
    def aval_cause_tid(self):
        """Gets the aval_cause_tid of this AvalancheEvalProblem2Dto.  # noqa: E501

        Hvilket svakt lag løsner skredet på? The AvalCauseKD unique identifier  # noqa: E501

        :return: The aval_cause_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_tid

    @aval_cause_tid.setter
    def aval_cause_tid(self, aval_cause_tid):
        """Sets the aval_cause_tid of this AvalancheEvalProblem2Dto.

        Hvilket svakt lag løsner skredet på? The AvalCauseKD unique identifier  # noqa: E501

        :param aval_cause_tid: The aval_cause_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._aval_cause_tid = aval_cause_tid

    @property
    def aval_cause_depth_tid(self):
        """Gets the aval_cause_depth_tid of this AvalancheEvalProblem2Dto.  # noqa: E501

        Hvor dypt ligger det overnevnte svake laget? The AvalCauseDepthKD unique identifier  # noqa: E501

        :return: The aval_cause_depth_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_depth_tid

    @aval_cause_depth_tid.setter
    def aval_cause_depth_tid(self, aval_cause_depth_tid):
        """Sets the aval_cause_depth_tid of this AvalancheEvalProblem2Dto.

        Hvor dypt ligger det overnevnte svake laget? The AvalCauseDepthKD unique identifier  # noqa: E501

        :param aval_cause_depth_tid: The aval_cause_depth_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._aval_cause_depth_tid = aval_cause_depth_tid

    @property
    def aval_cause_attributes(self):
        """Gets the aval_cause_attributes of this AvalancheEvalProblem2Dto.  # noqa: E501

        AvalCauseAttributes er flagging. Det som lagres er ugunstige egenskaper til det svake laget i snøen. Dette er flervalgsliste. Om valg 1 og 4 er valgt lagres 9 (binært 1001). Om valg 1 og 2 er valgt lagres 3 (binært 11). Om bare valg 3 er valgt lagres 4 (binært 100)  # noqa: E501

        :return: The aval_cause_attributes of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_attributes

    @aval_cause_attributes.setter
    def aval_cause_attributes(self, aval_cause_attributes):
        """Sets the aval_cause_attributes of this AvalancheEvalProblem2Dto.

        AvalCauseAttributes er flagging. Det som lagres er ugunstige egenskaper til det svake laget i snøen. Dette er flervalgsliste. Om valg 1 og 4 er valgt lagres 9 (binært 1001). Om valg 1 og 2 er valgt lagres 3 (binært 11). Om bare valg 3 er valgt lagres 4 (binært 100)  # noqa: E501

        :param aval_cause_attributes: The aval_cause_attributes of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._aval_cause_attributes = aval_cause_attributes

    @property
    def valid_exposition(self):
        """Gets the valid_exposition of this AvalancheEvalProblem2Dto.  # noqa: E501

        Velg utsatte retninger  # noqa: E501

        :return: The valid_exposition of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: str
        """
        return self._valid_exposition

    @valid_exposition.setter
    def valid_exposition(self, valid_exposition):
        """Sets the valid_exposition of this AvalancheEvalProblem2Dto.

        Velg utsatte retninger  # noqa: E501

        :param valid_exposition: The valid_exposition of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: str
        """

        self._valid_exposition = valid_exposition

    @property
    def exposed_height1(self):
        """Gets the exposed_height1 of this AvalancheEvalProblem2Dto.  # noqa: E501

        Øverste høyde på “utsatt høyde” symbolet.  # noqa: E501

        :return: The exposed_height1 of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height1

    @exposed_height1.setter
    def exposed_height1(self, exposed_height1):
        """Sets the exposed_height1 of this AvalancheEvalProblem2Dto.

        Øverste høyde på “utsatt høyde” symbolet.  # noqa: E501

        :param exposed_height1: The exposed_height1 of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._exposed_height1 = exposed_height1

    @property
    def exposed_height2(self):
        """Gets the exposed_height2 of this AvalancheEvalProblem2Dto.  # noqa: E501

        Nederste høyde på “utsatt høyde” symbolet.  # noqa: E501

        :return: The exposed_height2 of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height2

    @exposed_height2.setter
    def exposed_height2(self, exposed_height2):
        """Sets the exposed_height2 of this AvalancheEvalProblem2Dto.

        Nederste høyde på “utsatt høyde” symbolet.  # noqa: E501

        :param exposed_height2: The exposed_height2 of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._exposed_height2 = exposed_height2

    @property
    def exposed_height_combo_tid(self):
        """Gets the exposed_height_combo_tid of this AvalancheEvalProblem2Dto.  # noqa: E501

        Hvilket symbol brukes? Er utsatt tereng over ExposedHeight2 eller under den? The ExposedHeightComboKD unique identifier  # noqa: E501

        :return: The exposed_height_combo_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height_combo_tid

    @exposed_height_combo_tid.setter
    def exposed_height_combo_tid(self, exposed_height_combo_tid):
        """Sets the exposed_height_combo_tid of this AvalancheEvalProblem2Dto.

        Hvilket symbol brukes? Er utsatt tereng over ExposedHeight2 eller under den? The ExposedHeightComboKD unique identifier  # noqa: E501

        :param exposed_height_combo_tid: The exposed_height_combo_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._exposed_height_combo_tid = exposed_height_combo_tid

    @property
    def aval_propagation_tid(self):
        """Gets the aval_propagation_tid of this AvalancheEvalProblem2Dto.  # noqa: E501

        TODO  # noqa: E501

        :return: The aval_propagation_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: int
        """
        return self._aval_propagation_tid

    @aval_propagation_tid.setter
    def aval_propagation_tid(self, aval_propagation_tid):
        """Sets the aval_propagation_tid of this AvalancheEvalProblem2Dto.

        TODO  # noqa: E501

        :param aval_propagation_tid: The aval_propagation_tid of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: int
        """

        self._aval_propagation_tid = aval_propagation_tid

    @property
    def comment(self):
        """Gets the comment of this AvalancheEvalProblem2Dto.  # noqa: E501

        Kommentar til skredproblemet  # noqa: E501

        :return: The comment of this AvalancheEvalProblem2Dto.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AvalancheEvalProblem2Dto.

        Kommentar til skredproblemet  # noqa: E501

        :param comment: The comment of this AvalancheEvalProblem2Dto.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(AvalancheEvalProblem2Dto, dict):
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
        if not isinstance(other, AvalancheEvalProblem2Dto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other