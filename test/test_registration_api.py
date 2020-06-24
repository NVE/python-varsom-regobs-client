# coding: utf-8

"""
    RegObs API

      ## Introduction    RegObs is a tool for collecting observations and events   related to natural hazards. It is currently used by the   Norwegian flood, landslide and avalanche warning service in   Norway, but the data is openly available for anyone through this API.    Regobs has been developed by the Norwegian Water resources and   Energy Directorate (NVE), in collaboration with the Norwegian   Meteorological Institute (MET) and the Norwegian Public Roads   Administration (NPRA).    You can check out our representation of the data at [regobs.no](http://regobs.no).    ## Authentication    Some endpoints require an api key.  You can get an API key by sending an email to   [raek@nve.no](mailto:raek@nve.no?subject=RegObs%20API%20Key).  To use the api key with the swagger ui, fill in the api\\_key input above.   It should then be included with every request in the   `regObs_apptoken` header.    ## Getting started    Get the last 10 observations using python:    ```python  import requests  r = requests.post('https://api.regobs.no/v4/Search',       data={'NumberOfRecords': 10},      headers={'Content-Type': 'application/json'}  )  data = r.json()  print(len(data))  # 10  ```      # noqa: E501

    OpenAPI spec version: v4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import varsom_regobs_client
from api.registration_api import RegistrationApi  # noqa: E501
from varsom_regobs_client.rest import ApiException


class TestRegistrationApi(unittest.TestCase):
    """RegistrationApi unit test stubs"""

    def setUp(self):
        self.api = api.registration_api.RegistrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_registration_get(self):
        """Test case for registration_get

        Get registration by regId.  # noqa: E501
        """
        pass

    def test_registration_get_caaml(self):
        """Test case for registration_get_caaml

        Get a registration in CAAML format  # noqa: E501
        """
        pass

    def test_registration_insert(self):
        """Test case for registration_insert

        Create a new registration.  # noqa: E501
        """
        pass

    def test_registration_plot_preview_png(self):
        """Test case for registration_plot_preview_png

        Generate a preview figure for a snow profile registration.  # noqa: E501
        """
        pass

    def test_registration_validate(self):
        """Test case for registration_validate

        Validate registration data.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
