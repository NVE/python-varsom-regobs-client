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


class AvalancheEvalProblem2ViewModel(object):
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
        'avalanche_eval_problem_id': 'int',
        'aval_probability_tid': 'int',
        'aval_probability_name': 'str',
        'aval_trigger_simple_tid': 'int',
        'aval_trigger_simple_name': 'str',
        'aval_cause_depth_tid': 'int',
        'aval_cause_depth_name': 'str',
        'valid_exposition': 'str',
        'exposed_height1': 'int',
        'exposed_height2': 'int',
        'exposed_height_combo_tid': 'int',
        'exposed_height_combo_name': 'str',
        'avalanche_ext_tid': 'int',
        'avalanche_ext_name': 'str',
        'comment': 'str',
        'aval_cause_tid': 'int',
        'aval_cause_name': 'str',
        'destructive_size_tid': 'int',
        'destructive_size_name': 'str',
        'aval_propagation_tid': 'int',
        'aval_propagation_name': 'str',
        'aval_cause_attribute_light_tid': 'int',
        'aval_cause_attribute_light_name': 'str',
        'aval_cause_attribute_thin_tid': 'int',
        'aval_cause_attribute_thin_name': 'str',
        'aval_cause_attribute_soft_tid': 'int',
        'aval_cause_attribute_soft_name': 'str',
        'aval_cause_attribute_crystal_tid': 'int',
        'aval_cause_attribute_crystal_name': 'str'
    }

    attribute_map = {
        'avalanche_eval_problem_id': 'AvalancheEvalProblemID',
        'aval_probability_tid': 'AvalProbabilityTID',
        'aval_probability_name': 'AvalProbabilityName',
        'aval_trigger_simple_tid': 'AvalTriggerSimpleTID',
        'aval_trigger_simple_name': 'AvalTriggerSimpleName',
        'aval_cause_depth_tid': 'AvalCauseDepthTID',
        'aval_cause_depth_name': 'AvalCauseDepthName',
        'valid_exposition': 'ValidExposition',
        'exposed_height1': 'ExposedHeight1',
        'exposed_height2': 'ExposedHeight2',
        'exposed_height_combo_tid': 'ExposedHeightComboTID',
        'exposed_height_combo_name': 'ExposedHeightComboName',
        'avalanche_ext_tid': 'AvalancheExtTID',
        'avalanche_ext_name': 'AvalancheExtName',
        'comment': 'Comment',
        'aval_cause_tid': 'AvalCauseTID',
        'aval_cause_name': 'AvalCauseName',
        'destructive_size_tid': 'DestructiveSizeTID',
        'destructive_size_name': 'DestructiveSizeName',
        'aval_propagation_tid': 'AvalPropagationTID',
        'aval_propagation_name': 'AvalPropagationName',
        'aval_cause_attribute_light_tid': 'AvalCauseAttributeLightTID',
        'aval_cause_attribute_light_name': 'AvalCauseAttributeLightName',
        'aval_cause_attribute_thin_tid': 'AvalCauseAttributeThinTID',
        'aval_cause_attribute_thin_name': 'AvalCauseAttributeThinName',
        'aval_cause_attribute_soft_tid': 'AvalCauseAttributeSoftTID',
        'aval_cause_attribute_soft_name': 'AvalCauseAttributeSoftName',
        'aval_cause_attribute_crystal_tid': 'AvalCauseAttributeCrystalTID',
        'aval_cause_attribute_crystal_name': 'AvalCauseAttributeCrystalName'
    }

    def __init__(self, avalanche_eval_problem_id=None, aval_probability_tid=None, aval_probability_name=None, aval_trigger_simple_tid=None, aval_trigger_simple_name=None, aval_cause_depth_tid=None, aval_cause_depth_name=None, valid_exposition=None, exposed_height1=None, exposed_height2=None, exposed_height_combo_tid=None, exposed_height_combo_name=None, avalanche_ext_tid=None, avalanche_ext_name=None, comment=None, aval_cause_tid=None, aval_cause_name=None, destructive_size_tid=None, destructive_size_name=None, aval_propagation_tid=None, aval_propagation_name=None, aval_cause_attribute_light_tid=None, aval_cause_attribute_light_name=None, aval_cause_attribute_thin_tid=None, aval_cause_attribute_thin_name=None, aval_cause_attribute_soft_tid=None, aval_cause_attribute_soft_name=None, aval_cause_attribute_crystal_tid=None, aval_cause_attribute_crystal_name=None):  # noqa: E501
        """AvalancheEvalProblem2ViewModel - a model defined in Swagger"""  # noqa: E501
        self._avalanche_eval_problem_id = None
        self._aval_probability_tid = None
        self._aval_probability_name = None
        self._aval_trigger_simple_tid = None
        self._aval_trigger_simple_name = None
        self._aval_cause_depth_tid = None
        self._aval_cause_depth_name = None
        self._valid_exposition = None
        self._exposed_height1 = None
        self._exposed_height2 = None
        self._exposed_height_combo_tid = None
        self._exposed_height_combo_name = None
        self._avalanche_ext_tid = None
        self._avalanche_ext_name = None
        self._comment = None
        self._aval_cause_tid = None
        self._aval_cause_name = None
        self._destructive_size_tid = None
        self._destructive_size_name = None
        self._aval_propagation_tid = None
        self._aval_propagation_name = None
        self._aval_cause_attribute_light_tid = None
        self._aval_cause_attribute_light_name = None
        self._aval_cause_attribute_thin_tid = None
        self._aval_cause_attribute_thin_name = None
        self._aval_cause_attribute_soft_tid = None
        self._aval_cause_attribute_soft_name = None
        self._aval_cause_attribute_crystal_tid = None
        self._aval_cause_attribute_crystal_name = None
        self.discriminator = None
        if avalanche_eval_problem_id is not None:
            self.avalanche_eval_problem_id = avalanche_eval_problem_id
        if aval_probability_tid is not None:
            self.aval_probability_tid = aval_probability_tid
        if aval_probability_name is not None:
            self.aval_probability_name = aval_probability_name
        if aval_trigger_simple_tid is not None:
            self.aval_trigger_simple_tid = aval_trigger_simple_tid
        if aval_trigger_simple_name is not None:
            self.aval_trigger_simple_name = aval_trigger_simple_name
        if aval_cause_depth_tid is not None:
            self.aval_cause_depth_tid = aval_cause_depth_tid
        if aval_cause_depth_name is not None:
            self.aval_cause_depth_name = aval_cause_depth_name
        if valid_exposition is not None:
            self.valid_exposition = valid_exposition
        if exposed_height1 is not None:
            self.exposed_height1 = exposed_height1
        if exposed_height2 is not None:
            self.exposed_height2 = exposed_height2
        if exposed_height_combo_tid is not None:
            self.exposed_height_combo_tid = exposed_height_combo_tid
        if exposed_height_combo_name is not None:
            self.exposed_height_combo_name = exposed_height_combo_name
        if avalanche_ext_tid is not None:
            self.avalanche_ext_tid = avalanche_ext_tid
        if avalanche_ext_name is not None:
            self.avalanche_ext_name = avalanche_ext_name
        if comment is not None:
            self.comment = comment
        if aval_cause_tid is not None:
            self.aval_cause_tid = aval_cause_tid
        if aval_cause_name is not None:
            self.aval_cause_name = aval_cause_name
        if destructive_size_tid is not None:
            self.destructive_size_tid = destructive_size_tid
        if destructive_size_name is not None:
            self.destructive_size_name = destructive_size_name
        if aval_propagation_tid is not None:
            self.aval_propagation_tid = aval_propagation_tid
        if aval_propagation_name is not None:
            self.aval_propagation_name = aval_propagation_name
        if aval_cause_attribute_light_tid is not None:
            self.aval_cause_attribute_light_tid = aval_cause_attribute_light_tid
        if aval_cause_attribute_light_name is not None:
            self.aval_cause_attribute_light_name = aval_cause_attribute_light_name
        if aval_cause_attribute_thin_tid is not None:
            self.aval_cause_attribute_thin_tid = aval_cause_attribute_thin_tid
        if aval_cause_attribute_thin_name is not None:
            self.aval_cause_attribute_thin_name = aval_cause_attribute_thin_name
        if aval_cause_attribute_soft_tid is not None:
            self.aval_cause_attribute_soft_tid = aval_cause_attribute_soft_tid
        if aval_cause_attribute_soft_name is not None:
            self.aval_cause_attribute_soft_name = aval_cause_attribute_soft_name
        if aval_cause_attribute_crystal_tid is not None:
            self.aval_cause_attribute_crystal_tid = aval_cause_attribute_crystal_tid
        if aval_cause_attribute_crystal_name is not None:
            self.aval_cause_attribute_crystal_name = aval_cause_attribute_crystal_name

    @property
    def avalanche_eval_problem_id(self):
        """Gets the avalanche_eval_problem_id of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The avalanche_eval_problem_id of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._avalanche_eval_problem_id

    @avalanche_eval_problem_id.setter
    def avalanche_eval_problem_id(self, avalanche_eval_problem_id):
        """Sets the avalanche_eval_problem_id of this AvalancheEvalProblem2ViewModel.


        :param avalanche_eval_problem_id: The avalanche_eval_problem_id of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._avalanche_eval_problem_id = avalanche_eval_problem_id

    @property
    def aval_probability_tid(self):
        """Gets the aval_probability_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_probability_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aval_probability_tid

    @aval_probability_tid.setter
    def aval_probability_tid(self, aval_probability_tid):
        """Sets the aval_probability_tid of this AvalancheEvalProblem2ViewModel.


        :param aval_probability_tid: The aval_probability_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._aval_probability_tid = aval_probability_tid

    @property
    def aval_probability_name(self):
        """Gets the aval_probability_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_probability_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._aval_probability_name

    @aval_probability_name.setter
    def aval_probability_name(self, aval_probability_name):
        """Sets the aval_probability_name of this AvalancheEvalProblem2ViewModel.


        :param aval_probability_name: The aval_probability_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._aval_probability_name = aval_probability_name

    @property
    def aval_trigger_simple_tid(self):
        """Gets the aval_trigger_simple_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_trigger_simple_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aval_trigger_simple_tid

    @aval_trigger_simple_tid.setter
    def aval_trigger_simple_tid(self, aval_trigger_simple_tid):
        """Sets the aval_trigger_simple_tid of this AvalancheEvalProblem2ViewModel.


        :param aval_trigger_simple_tid: The aval_trigger_simple_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._aval_trigger_simple_tid = aval_trigger_simple_tid

    @property
    def aval_trigger_simple_name(self):
        """Gets the aval_trigger_simple_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_trigger_simple_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._aval_trigger_simple_name

    @aval_trigger_simple_name.setter
    def aval_trigger_simple_name(self, aval_trigger_simple_name):
        """Sets the aval_trigger_simple_name of this AvalancheEvalProblem2ViewModel.


        :param aval_trigger_simple_name: The aval_trigger_simple_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._aval_trigger_simple_name = aval_trigger_simple_name

    @property
    def aval_cause_depth_tid(self):
        """Gets the aval_cause_depth_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_depth_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_depth_tid

    @aval_cause_depth_tid.setter
    def aval_cause_depth_tid(self, aval_cause_depth_tid):
        """Sets the aval_cause_depth_tid of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_depth_tid: The aval_cause_depth_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._aval_cause_depth_tid = aval_cause_depth_tid

    @property
    def aval_cause_depth_name(self):
        """Gets the aval_cause_depth_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_depth_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._aval_cause_depth_name

    @aval_cause_depth_name.setter
    def aval_cause_depth_name(self, aval_cause_depth_name):
        """Sets the aval_cause_depth_name of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_depth_name: The aval_cause_depth_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._aval_cause_depth_name = aval_cause_depth_name

    @property
    def valid_exposition(self):
        """Gets the valid_exposition of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The valid_exposition of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._valid_exposition

    @valid_exposition.setter
    def valid_exposition(self, valid_exposition):
        """Sets the valid_exposition of this AvalancheEvalProblem2ViewModel.


        :param valid_exposition: The valid_exposition of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._valid_exposition = valid_exposition

    @property
    def exposed_height1(self):
        """Gets the exposed_height1 of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The exposed_height1 of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height1

    @exposed_height1.setter
    def exposed_height1(self, exposed_height1):
        """Sets the exposed_height1 of this AvalancheEvalProblem2ViewModel.


        :param exposed_height1: The exposed_height1 of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._exposed_height1 = exposed_height1

    @property
    def exposed_height2(self):
        """Gets the exposed_height2 of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The exposed_height2 of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height2

    @exposed_height2.setter
    def exposed_height2(self, exposed_height2):
        """Sets the exposed_height2 of this AvalancheEvalProblem2ViewModel.


        :param exposed_height2: The exposed_height2 of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._exposed_height2 = exposed_height2

    @property
    def exposed_height_combo_tid(self):
        """Gets the exposed_height_combo_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The exposed_height_combo_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._exposed_height_combo_tid

    @exposed_height_combo_tid.setter
    def exposed_height_combo_tid(self, exposed_height_combo_tid):
        """Sets the exposed_height_combo_tid of this AvalancheEvalProblem2ViewModel.


        :param exposed_height_combo_tid: The exposed_height_combo_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._exposed_height_combo_tid = exposed_height_combo_tid

    @property
    def exposed_height_combo_name(self):
        """Gets the exposed_height_combo_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The exposed_height_combo_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._exposed_height_combo_name

    @exposed_height_combo_name.setter
    def exposed_height_combo_name(self, exposed_height_combo_name):
        """Sets the exposed_height_combo_name of this AvalancheEvalProblem2ViewModel.


        :param exposed_height_combo_name: The exposed_height_combo_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._exposed_height_combo_name = exposed_height_combo_name

    @property
    def avalanche_ext_tid(self):
        """Gets the avalanche_ext_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The avalanche_ext_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._avalanche_ext_tid

    @avalanche_ext_tid.setter
    def avalanche_ext_tid(self, avalanche_ext_tid):
        """Sets the avalanche_ext_tid of this AvalancheEvalProblem2ViewModel.


        :param avalanche_ext_tid: The avalanche_ext_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._avalanche_ext_tid = avalanche_ext_tid

    @property
    def avalanche_ext_name(self):
        """Gets the avalanche_ext_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The avalanche_ext_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._avalanche_ext_name

    @avalanche_ext_name.setter
    def avalanche_ext_name(self, avalanche_ext_name):
        """Sets the avalanche_ext_name of this AvalancheEvalProblem2ViewModel.


        :param avalanche_ext_name: The avalanche_ext_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._avalanche_ext_name = avalanche_ext_name

    @property
    def comment(self):
        """Gets the comment of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The comment of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AvalancheEvalProblem2ViewModel.


        :param comment: The comment of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def aval_cause_tid(self):
        """Gets the aval_cause_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_tid

    @aval_cause_tid.setter
    def aval_cause_tid(self, aval_cause_tid):
        """Sets the aval_cause_tid of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_tid: The aval_cause_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._aval_cause_tid = aval_cause_tid

    @property
    def aval_cause_name(self):
        """Gets the aval_cause_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._aval_cause_name

    @aval_cause_name.setter
    def aval_cause_name(self, aval_cause_name):
        """Sets the aval_cause_name of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_name: The aval_cause_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._aval_cause_name = aval_cause_name

    @property
    def destructive_size_tid(self):
        """Gets the destructive_size_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The destructive_size_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._destructive_size_tid

    @destructive_size_tid.setter
    def destructive_size_tid(self, destructive_size_tid):
        """Sets the destructive_size_tid of this AvalancheEvalProblem2ViewModel.


        :param destructive_size_tid: The destructive_size_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._destructive_size_tid = destructive_size_tid

    @property
    def destructive_size_name(self):
        """Gets the destructive_size_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The destructive_size_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._destructive_size_name

    @destructive_size_name.setter
    def destructive_size_name(self, destructive_size_name):
        """Sets the destructive_size_name of this AvalancheEvalProblem2ViewModel.


        :param destructive_size_name: The destructive_size_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._destructive_size_name = destructive_size_name

    @property
    def aval_propagation_tid(self):
        """Gets the aval_propagation_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_propagation_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aval_propagation_tid

    @aval_propagation_tid.setter
    def aval_propagation_tid(self, aval_propagation_tid):
        """Sets the aval_propagation_tid of this AvalancheEvalProblem2ViewModel.


        :param aval_propagation_tid: The aval_propagation_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._aval_propagation_tid = aval_propagation_tid

    @property
    def aval_propagation_name(self):
        """Gets the aval_propagation_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_propagation_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._aval_propagation_name

    @aval_propagation_name.setter
    def aval_propagation_name(self, aval_propagation_name):
        """Sets the aval_propagation_name of this AvalancheEvalProblem2ViewModel.


        :param aval_propagation_name: The aval_propagation_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._aval_propagation_name = aval_propagation_name

    @property
    def aval_cause_attribute_light_tid(self):
        """Gets the aval_cause_attribute_light_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_attribute_light_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_attribute_light_tid

    @aval_cause_attribute_light_tid.setter
    def aval_cause_attribute_light_tid(self, aval_cause_attribute_light_tid):
        """Sets the aval_cause_attribute_light_tid of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_attribute_light_tid: The aval_cause_attribute_light_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._aval_cause_attribute_light_tid = aval_cause_attribute_light_tid

    @property
    def aval_cause_attribute_light_name(self):
        """Gets the aval_cause_attribute_light_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_attribute_light_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._aval_cause_attribute_light_name

    @aval_cause_attribute_light_name.setter
    def aval_cause_attribute_light_name(self, aval_cause_attribute_light_name):
        """Sets the aval_cause_attribute_light_name of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_attribute_light_name: The aval_cause_attribute_light_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._aval_cause_attribute_light_name = aval_cause_attribute_light_name

    @property
    def aval_cause_attribute_thin_tid(self):
        """Gets the aval_cause_attribute_thin_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_attribute_thin_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_attribute_thin_tid

    @aval_cause_attribute_thin_tid.setter
    def aval_cause_attribute_thin_tid(self, aval_cause_attribute_thin_tid):
        """Sets the aval_cause_attribute_thin_tid of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_attribute_thin_tid: The aval_cause_attribute_thin_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._aval_cause_attribute_thin_tid = aval_cause_attribute_thin_tid

    @property
    def aval_cause_attribute_thin_name(self):
        """Gets the aval_cause_attribute_thin_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_attribute_thin_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._aval_cause_attribute_thin_name

    @aval_cause_attribute_thin_name.setter
    def aval_cause_attribute_thin_name(self, aval_cause_attribute_thin_name):
        """Sets the aval_cause_attribute_thin_name of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_attribute_thin_name: The aval_cause_attribute_thin_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._aval_cause_attribute_thin_name = aval_cause_attribute_thin_name

    @property
    def aval_cause_attribute_soft_tid(self):
        """Gets the aval_cause_attribute_soft_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_attribute_soft_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_attribute_soft_tid

    @aval_cause_attribute_soft_tid.setter
    def aval_cause_attribute_soft_tid(self, aval_cause_attribute_soft_tid):
        """Sets the aval_cause_attribute_soft_tid of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_attribute_soft_tid: The aval_cause_attribute_soft_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._aval_cause_attribute_soft_tid = aval_cause_attribute_soft_tid

    @property
    def aval_cause_attribute_soft_name(self):
        """Gets the aval_cause_attribute_soft_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_attribute_soft_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._aval_cause_attribute_soft_name

    @aval_cause_attribute_soft_name.setter
    def aval_cause_attribute_soft_name(self, aval_cause_attribute_soft_name):
        """Sets the aval_cause_attribute_soft_name of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_attribute_soft_name: The aval_cause_attribute_soft_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._aval_cause_attribute_soft_name = aval_cause_attribute_soft_name

    @property
    def aval_cause_attribute_crystal_tid(self):
        """Gets the aval_cause_attribute_crystal_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_attribute_crystal_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: int
        """
        return self._aval_cause_attribute_crystal_tid

    @aval_cause_attribute_crystal_tid.setter
    def aval_cause_attribute_crystal_tid(self, aval_cause_attribute_crystal_tid):
        """Sets the aval_cause_attribute_crystal_tid of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_attribute_crystal_tid: The aval_cause_attribute_crystal_tid of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: int
        """

        self._aval_cause_attribute_crystal_tid = aval_cause_attribute_crystal_tid

    @property
    def aval_cause_attribute_crystal_name(self):
        """Gets the aval_cause_attribute_crystal_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501


        :return: The aval_cause_attribute_crystal_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :rtype: str
        """
        return self._aval_cause_attribute_crystal_name

    @aval_cause_attribute_crystal_name.setter
    def aval_cause_attribute_crystal_name(self, aval_cause_attribute_crystal_name):
        """Sets the aval_cause_attribute_crystal_name of this AvalancheEvalProblem2ViewModel.


        :param aval_cause_attribute_crystal_name: The aval_cause_attribute_crystal_name of this AvalancheEvalProblem2ViewModel.  # noqa: E501
        :type: str
        """

        self._aval_cause_attribute_crystal_name = aval_cause_attribute_crystal_name

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
        if issubclass(AvalancheEvalProblem2ViewModel, dict):
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
        if not isinstance(other, AvalancheEvalProblem2ViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other