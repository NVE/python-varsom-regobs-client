# coding: utf-8

"""
    RegObs API

      ## Introduction    RegObs is a tool for collecting observations and events   related to natural hazards. It is currently used by the   Norwegian flood, landslide and avalanche warning service in   Norway, but the data is openly available for anyone through this API.    Regobs has been developed by the Norwegian Water resources and   Energy Directorate (NVE), in collaboration with the Norwegian   Meteorological Institute (MET) and the Norwegian Public Roads   Administration (NPRA).    You can check out our representation of the data at [regobs.no](http://regobs.no).    ## Authentication    Some endpoints require an api key.  You can get an API key by sending an email to   [raek@nve.no](mailto:raek@nve.no?subject=RegObs%20API%20Key).  To use the api key with the swagger ui, fill in the api\\_key input above.   It should then be included with every request in the   `regObs_apptoken` header.    ## Getting started    Get the last 10 observations using python:    ```python  import requests  r = requests.post('https://api.regobs.no/v4/Search',       data={'NumberOfRecords': 10},      headers={'Content-Type': 'application/json'}  )  data = r.json()  print(len(data))  # 10  ```      # noqa: E501

    OpenAPI spec version: v4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from varsom_regobs_client.api_client import ApiClient


class GeneralObsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_general_obs(self, reg_id, **kwargs):  # noqa: E501
        """delete_general_obs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_general_obs(reg_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int reg_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_general_obs_with_http_info(reg_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_general_obs_with_http_info(reg_id, **kwargs)  # noqa: E501
            return data

    def delete_general_obs_with_http_info(self, reg_id, **kwargs):  # noqa: E501
        """delete_general_obs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_general_obs_with_http_info(reg_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int reg_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reg_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_general_obs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reg_id' is set
        if ('reg_id' not in params or
                params['reg_id'] is None):
            raise ValueError("Missing the required parameter `reg_id` when calling `delete_general_obs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reg_id' in params:
            path_params['regId'] = params['reg_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/GeneralObs/{regId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_general_obs(self, reg_id, **kwargs):  # noqa: E501
        """get_general_obs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_general_obs(reg_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int reg_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_general_obs_with_http_info(reg_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_general_obs_with_http_info(reg_id, **kwargs)  # noqa: E501
            return data

    def get_general_obs_with_http_info(self, reg_id, **kwargs):  # noqa: E501
        """get_general_obs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_general_obs_with_http_info(reg_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int reg_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reg_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_general_obs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reg_id' is set
        if ('reg_id' not in params or
                params['reg_id'] is None):
            raise ValueError("Missing the required parameter `reg_id` when calling `get_general_obs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reg_id' in params:
            path_params['regId'] = params['reg_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/GeneralObs/{regId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_general_obs(self, body, reg_id, **kwargs):  # noqa: E501
        """post_general_obs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_general_obs(body, reg_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GeneralObservationEditModel body: (required)
        :param int reg_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_general_obs_with_http_info(body, reg_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_general_obs_with_http_info(body, reg_id, **kwargs)  # noqa: E501
            return data

    def post_general_obs_with_http_info(self, body, reg_id, **kwargs):  # noqa: E501
        """post_general_obs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_general_obs_with_http_info(body, reg_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GeneralObservationEditModel body: (required)
        :param int reg_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'reg_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_general_obs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_general_obs`")  # noqa: E501
        # verify the required parameter 'reg_id' is set
        if ('reg_id' not in params or
                params['reg_id'] is None):
            raise ValueError("Missing the required parameter `reg_id` when calling `post_general_obs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reg_id' in params:
            path_params['regId'] = params['reg_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/GeneralObs/{regId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_general_obs(self, body, reg_id, **kwargs):  # noqa: E501
        """put_general_obs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_general_obs(body, reg_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GeneralObservationEditModel body: (required)
        :param int reg_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_general_obs_with_http_info(body, reg_id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_general_obs_with_http_info(body, reg_id, **kwargs)  # noqa: E501
            return data

    def put_general_obs_with_http_info(self, body, reg_id, **kwargs):  # noqa: E501
        """put_general_obs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_general_obs_with_http_info(body, reg_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GeneralObservationEditModel body: (required)
        :param int reg_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'reg_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_general_obs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_general_obs`")  # noqa: E501
        # verify the required parameter 'reg_id' is set
        if ('reg_id' not in params or
                params['reg_id'] is None):
            raise ValueError("Missing the required parameter `reg_id` when calling `put_general_obs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reg_id' in params:
            path_params['regId'] = params['reg_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/GeneralObs/{regId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
