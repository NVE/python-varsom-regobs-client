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


class RegistrationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def registration_get(self, reg_id, lang_key, **kwargs):  # noqa: E501
        """Get registration by regId.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registration_get(reg_id, lang_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int reg_id: Registration Id (required)
        :param int lang_key: 1 = norwegian, 2 = english (required)
        :return: RegistrationViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.registration_get_with_http_info(reg_id, lang_key, **kwargs)  # noqa: E501
        else:
            (data) = self.registration_get_with_http_info(reg_id, lang_key, **kwargs)  # noqa: E501
            return data

    def registration_get_with_http_info(self, reg_id, lang_key, **kwargs):  # noqa: E501
        """Get registration by regId.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registration_get_with_http_info(reg_id, lang_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int reg_id: Registration Id (required)
        :param int lang_key: 1 = norwegian, 2 = english (required)
        :return: RegistrationViewModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reg_id', 'lang_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method registration_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reg_id' is set
        if ('reg_id' not in params or
                params['reg_id'] is None):
            raise ValueError("Missing the required parameter `reg_id` when calling `registration_get`")  # noqa: E501
        # verify the required parameter 'lang_key' is set
        if ('lang_key' not in params or
                params['lang_key'] is None):
            raise ValueError("Missing the required parameter `lang_key` when calling `registration_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reg_id' in params:
            path_params['regId'] = params['reg_id']  # noqa: E501
        if 'lang_key' in params:
            path_params['langKey'] = params['lang_key']  # noqa: E501

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
            '/Registration/{regId}/{langKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegistrationViewModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def registration_get_caaml(self, reg_id, **kwargs):  # noqa: E501
        """Get a registration in CAAML format  # noqa: E501

        CAAML (Canadian Avalanche Association Markup Language) is a standard   for the electronic representation of information pertinent to avalanche   safety operations. See http://caaml.org/.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registration_get_caaml(reg_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int reg_id: Registration Id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.registration_get_caaml_with_http_info(reg_id, **kwargs)  # noqa: E501
        else:
            (data) = self.registration_get_caaml_with_http_info(reg_id, **kwargs)  # noqa: E501
            return data

    def registration_get_caaml_with_http_info(self, reg_id, **kwargs):  # noqa: E501
        """Get a registration in CAAML format  # noqa: E501

        CAAML (Canadian Avalanche Association Markup Language) is a standard   for the electronic representation of information pertinent to avalanche   safety operations. See http://caaml.org/.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registration_get_caaml_with_http_info(reg_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int reg_id: Registration Id (required)
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
                    " to method registration_get_caaml" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reg_id' is set
        if ('reg_id' not in params or
                params['reg_id'] is None):
            raise ValueError("Missing the required parameter `reg_id` when calling `registration_get_caaml`")  # noqa: E501

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
            ['text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Registration/Caaml/{regId}', 'GET',
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

    def registration_insert(self, body, **kwargs):  # noqa: E501
        """Create a new registration.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registration_insert(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRegistrationRequestDto body: Registration data (required)
        :return: CreateRegistrationResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.registration_insert_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.registration_insert_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def registration_insert_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new registration.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registration_insert_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRegistrationRequestDto body: Registration data (required)
        :return: CreateRegistrationResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method registration_insert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `registration_insert`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/Registration', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateRegistrationResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def registration_plot_preview_png(self, body, format, height, width, **kwargs):  # noqa: E501
        """Generate a preview figure for a snow profile registration.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registration_plot_preview_png(body, format, height, width, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRegistrationRequestDto body: Snow profile registration (required)
        :param int format: (required)
        :param int height: (required)
        :param int width: (required)
        :param int lang_key: 1 = norwegian, 2 = english
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.registration_plot_preview_png_with_http_info(body, format, height, width, **kwargs)  # noqa: E501
        else:
            (data) = self.registration_plot_preview_png_with_http_info(body, format, height, width, **kwargs)  # noqa: E501
            return data

    def registration_plot_preview_png_with_http_info(self, body, format, height, width, **kwargs):  # noqa: E501
        """Generate a preview figure for a snow profile registration.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registration_plot_preview_png_with_http_info(body, format, height, width, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRegistrationRequestDto body: Snow profile registration (required)
        :param int format: (required)
        :param int height: (required)
        :param int width: (required)
        :param int lang_key: 1 = norwegian, 2 = english
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'format', 'height', 'width', 'lang_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method registration_plot_preview_png" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `registration_plot_preview_png`")  # noqa: E501
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `registration_plot_preview_png`")  # noqa: E501
        # verify the required parameter 'height' is set
        if ('height' not in params or
                params['height'] is None):
            raise ValueError("Missing the required parameter `height` when calling `registration_plot_preview_png`")  # noqa: E501
        # verify the required parameter 'width' is set
        if ('width' not in params or
                params['width'] is None):
            raise ValueError("Missing the required parameter `width` when calling `registration_plot_preview_png`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501
        if 'height' in params:
            query_params.append(('height', params['height']))  # noqa: E501
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501
        if 'lang_key' in params:
            query_params.append(('langKey', params['lang_key']))  # noqa: E501

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
            '/Registration/PlotPreviewPng', 'POST',
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

    def registration_validate(self, body, **kwargs):  # noqa: E501
        """Validate registration data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registration_validate(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRegistrationRequestDto body: Registration data (required)
        :return: CreateRegistrationResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.registration_validate_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.registration_validate_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def registration_validate_with_http_info(self, body, **kwargs):  # noqa: E501
        """Validate registration data.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.registration_validate_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRegistrationRequestDto body: Registration data (required)
        :return: CreateRegistrationResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method registration_validate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `registration_validate`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/Registration/Validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateRegistrationResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)