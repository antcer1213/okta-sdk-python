# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from okta.api_client import ApiClient


class CAPTCHA(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_captcha_instance(self, **kwargs):  # noqa: E501
        """Create new CAPTCHA instance  # noqa: E501

        Adds a new CAPTCHA instance to your organization. In current release, we only allow one CAPTCHA instance per org.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_captcha_instance(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CAPTCHAInstance body:
        :return: CAPTCHAInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_captcha_instance_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_captcha_instance_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_captcha_instance_with_http_info(self, **kwargs):  # noqa: E501
        """Create new CAPTCHA instance  # noqa: E501

        Adds a new CAPTCHA instance to your organization. In current release, we only allow one CAPTCHA instance per org.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_captcha_instance_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CAPTCHAInstance body:
        :return: CAPTCHAInstance
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
                    " to method create_captcha_instance" % key
                )
            params[key] = val
        del params['kwargs']

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/captchas', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CAPTCHAInstance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_captcha_instance(self, captcha_id, **kwargs):  # noqa: E501
        """Delete CAPTCHA Instance  # noqa: E501

        Delete a CAPTCHA instance by `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_captcha_instance(captcha_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str captcha_id: id of the CAPTCHA (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_captcha_instance_with_http_info(captcha_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_captcha_instance_with_http_info(captcha_id, **kwargs)  # noqa: E501
            return data

    def delete_captcha_instance_with_http_info(self, captcha_id, **kwargs):  # noqa: E501
        """Delete CAPTCHA Instance  # noqa: E501

        Delete a CAPTCHA instance by `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_captcha_instance_with_http_info(captcha_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str captcha_id: id of the CAPTCHA (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['captcha_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_captcha_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'captcha_id' is set
        if ('captcha_id' not in params or
                params['captcha_id'] is None):
            raise ValueError("Missing the required parameter `captcha_id` when calling `delete_captcha_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'captcha_id' in params:
            path_params['captchaId'] = params['captcha_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/captchas/{captchaId}', 'DELETE',
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

    def get_captcha_instance(self, captcha_id, **kwargs):  # noqa: E501
        """Get CAPTCHA Instance  # noqa: E501

        Fetches a CAPTCHA instance by `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_captcha_instance(captcha_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str captcha_id: id of the CAPTCHA (required)
        :return: CAPTCHAInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_captcha_instance_with_http_info(captcha_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_captcha_instance_with_http_info(captcha_id, **kwargs)  # noqa: E501
            return data

    def get_captcha_instance_with_http_info(self, captcha_id, **kwargs):  # noqa: E501
        """Get CAPTCHA Instance  # noqa: E501

        Fetches a CAPTCHA instance by `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_captcha_instance_with_http_info(captcha_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str captcha_id: id of the CAPTCHA (required)
        :return: CAPTCHAInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['captcha_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_captcha_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'captcha_id' is set
        if ('captcha_id' not in params or
                params['captcha_id'] is None):
            raise ValueError("Missing the required parameter `captcha_id` when calling `get_captcha_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'captcha_id' in params:
            path_params['captchaId'] = params['captcha_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/captchas/{captchaId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CAPTCHAInstance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_captcha_instances(self, **kwargs):  # noqa: E501
        """List CAPTCHA instances  # noqa: E501

        Enumerates CAPTCHA instances in your organization with pagination. A subset of CAPTCHA instances can be returned that match a supported filter expression or query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_captcha_instances(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CAPTCHAInstance]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_captcha_instances_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_captcha_instances_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_captcha_instances_with_http_info(self, **kwargs):  # noqa: E501
        """List CAPTCHA instances  # noqa: E501

        Enumerates CAPTCHA instances in your organization with pagination. A subset of CAPTCHA instances can be returned that match a supported filter expression or query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_captcha_instances_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CAPTCHAInstance]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_captcha_instances" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/captchas', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CAPTCHAInstance]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def partial_update_captcha_instance(self, body, captcha_id, **kwargs):  # noqa: E501
        """Partial Update CAPTCHA instance  # noqa: E501

        Partially update a CAPTCHA instance by `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_captcha_instance(body, captcha_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CAPTCHAInstance body: (required)
        :param str captcha_id: id of the CAPTCHA (required)
        :return: CAPTCHAInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.partial_update_captcha_instance_with_http_info(body, captcha_id, **kwargs)  # noqa: E501
        else:
            (data) = self.partial_update_captcha_instance_with_http_info(body, captcha_id, **kwargs)  # noqa: E501
            return data

    def partial_update_captcha_instance_with_http_info(self, body, captcha_id, **kwargs):  # noqa: E501
        """Partial Update CAPTCHA instance  # noqa: E501

        Partially update a CAPTCHA instance by `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_captcha_instance_with_http_info(body, captcha_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CAPTCHAInstance body: (required)
        :param str captcha_id: id of the CAPTCHA (required)
        :return: CAPTCHAInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'captcha_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_update_captcha_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `partial_update_captcha_instance`")  # noqa: E501
        # verify the required parameter 'captcha_id' is set
        if ('captcha_id' not in params or
                params['captcha_id'] is None):
            raise ValueError("Missing the required parameter `captcha_id` when calling `partial_update_captcha_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'captcha_id' in params:
            path_params['captchaId'] = params['captcha_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/captchas/{captchaId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CAPTCHAInstance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_captcha_instance(self, body, captcha_id, **kwargs):  # noqa: E501
        """Update CAPTCHA instance  # noqa: E501

        Update a CAPTCHA instance by `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_captcha_instance(body, captcha_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CAPTCHAInstance body: (required)
        :param str captcha_id: id of the CAPTCHA (required)
        :return: CAPTCHAInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_captcha_instance_with_http_info(body, captcha_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_captcha_instance_with_http_info(body, captcha_id, **kwargs)  # noqa: E501
            return data

    def update_captcha_instance_with_http_info(self, body, captcha_id, **kwargs):  # noqa: E501
        """Update CAPTCHA instance  # noqa: E501

        Update a CAPTCHA instance by `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_captcha_instance_with_http_info(body, captcha_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CAPTCHAInstance body: (required)
        :param str captcha_id: id of the CAPTCHA (required)
        :return: CAPTCHAInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'captcha_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_captcha_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_captcha_instance`")  # noqa: E501
        # verify the required parameter 'captcha_id' is set
        if ('captcha_id' not in params or
                params['captcha_id'] is None):
            raise ValueError("Missing the required parameter `captcha_id` when calling `update_captcha_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'captcha_id' in params:
            path_params['captchaId'] = params['captcha_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/captchas/{captchaId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CAPTCHAInstance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
