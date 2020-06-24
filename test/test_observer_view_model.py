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
from models.observer_view_model import ObserverViewModel  # noqa: E501
from varsom_regobs_client.rest import ApiException


class TestObserverViewModel(unittest.TestCase):
    """ObserverViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testObserverViewModel(self):
        """Test ObserverViewModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = varsom_regobs_client.models.observer_view_model.ObserverViewModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
