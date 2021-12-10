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


class TrustedOrigin(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def activate_origin(self, trusted_origin_id, **kwargs):  # noqa: E501
        """activate_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_origin(trusted_origin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str trusted_origin_id: (required)
        :return: TrustedOrigin
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.activate_origin_with_http_info(trusted_origin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.activate_origin_with_http_info(trusted_origin_id, **kwargs)  # noqa: E501
            return data

    def activate_origin_with_http_info(self, trusted_origin_id, **kwargs):  # noqa: E501
        """activate_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_origin_with_http_info(trusted_origin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str trusted_origin_id: (required)
        :return: TrustedOrigin
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trusted_origin_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_origin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trusted_origin_id' is set
        if ('trusted_origin_id' not in params or
                params['trusted_origin_id'] is None):
            raise ValueError("Missing the required parameter `trusted_origin_id` when calling `activate_origin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trusted_origin_id' in params:
            path_params['trustedOriginId'] = params['trusted_origin_id']  # noqa: E501

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
            '/api/v1/trustedOrigins/{trustedOriginId}/lifecycle/activate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrustedOrigin',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_origin(self, body, **kwargs):  # noqa: E501
        """create_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_origin(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TrustedOrigin body: (required)
        :return: TrustedOrigin
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_origin_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_origin_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_origin_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_origin_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TrustedOrigin body: (required)
        :return: TrustedOrigin
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
                    " to method create_origin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_origin`")  # noqa: E501

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
            '/api/v1/trustedOrigins', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrustedOrigin',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deactivate_origin(self, trusted_origin_id, **kwargs):  # noqa: E501
        """deactivate_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deactivate_origin(trusted_origin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str trusted_origin_id: (required)
        :return: TrustedOrigin
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deactivate_origin_with_http_info(trusted_origin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.deactivate_origin_with_http_info(trusted_origin_id, **kwargs)  # noqa: E501
            return data

    def deactivate_origin_with_http_info(self, trusted_origin_id, **kwargs):  # noqa: E501
        """deactivate_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deactivate_origin_with_http_info(trusted_origin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str trusted_origin_id: (required)
        :return: TrustedOrigin
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trusted_origin_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deactivate_origin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trusted_origin_id' is set
        if ('trusted_origin_id' not in params or
                params['trusted_origin_id'] is None):
            raise ValueError("Missing the required parameter `trusted_origin_id` when calling `deactivate_origin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trusted_origin_id' in params:
            path_params['trustedOriginId'] = params['trusted_origin_id']  # noqa: E501

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
            '/api/v1/trustedOrigins/{trustedOriginId}/lifecycle/deactivate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrustedOrigin',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_origin(self, trusted_origin_id, **kwargs):  # noqa: E501
        """delete_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_origin(trusted_origin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str trusted_origin_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_origin_with_http_info(trusted_origin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_origin_with_http_info(trusted_origin_id, **kwargs)  # noqa: E501
            return data

    def delete_origin_with_http_info(self, trusted_origin_id, **kwargs):  # noqa: E501
        """delete_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_origin_with_http_info(trusted_origin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str trusted_origin_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trusted_origin_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_origin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trusted_origin_id' is set
        if ('trusted_origin_id' not in params or
                params['trusted_origin_id'] is None):
            raise ValueError("Missing the required parameter `trusted_origin_id` when calling `delete_origin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trusted_origin_id' in params:
            path_params['trustedOriginId'] = params['trusted_origin_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/trustedOrigins/{trustedOriginId}', 'DELETE',
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

    def get_origin(self, trusted_origin_id, **kwargs):  # noqa: E501
        """get_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_origin(trusted_origin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str trusted_origin_id: (required)
        :return: TrustedOrigin
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_origin_with_http_info(trusted_origin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_origin_with_http_info(trusted_origin_id, **kwargs)  # noqa: E501
            return data

    def get_origin_with_http_info(self, trusted_origin_id, **kwargs):  # noqa: E501
        """get_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_origin_with_http_info(trusted_origin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str trusted_origin_id: (required)
        :return: TrustedOrigin
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trusted_origin_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_origin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trusted_origin_id' is set
        if ('trusted_origin_id' not in params or
                params['trusted_origin_id'] is None):
            raise ValueError("Missing the required parameter `trusted_origin_id` when calling `get_origin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trusted_origin_id' in params:
            path_params['trustedOriginId'] = params['trusted_origin_id']  # noqa: E501

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
            '/api/v1/trustedOrigins/{trustedOriginId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrustedOrigin',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_origins(self, **kwargs):  # noqa: E501
        """list_origins  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_origins(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q:
        :param str filter:
        :param str after:
        :param int limit:
        :return: list[TrustedOrigin]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_origins_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_origins_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_origins_with_http_info(self, **kwargs):  # noqa: E501
        """list_origins  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_origins_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q:
        :param str filter:
        :param str after:
        :param int limit:
        :return: list[TrustedOrigin]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'filter', 'after', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_origins" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/api/v1/trustedOrigins', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TrustedOrigin]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_origin(self, body, trusted_origin_id, **kwargs):  # noqa: E501
        """update_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_origin(body, trusted_origin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TrustedOrigin body: (required)
        :param str trusted_origin_id: (required)
        :return: TrustedOrigin
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_origin_with_http_info(body, trusted_origin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_origin_with_http_info(body, trusted_origin_id, **kwargs)  # noqa: E501
            return data

    def update_origin_with_http_info(self, body, trusted_origin_id, **kwargs):  # noqa: E501
        """update_origin  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_origin_with_http_info(body, trusted_origin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TrustedOrigin body: (required)
        :param str trusted_origin_id: (required)
        :return: TrustedOrigin
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'trusted_origin_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_origin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_origin`")  # noqa: E501
        # verify the required parameter 'trusted_origin_id' is set
        if ('trusted_origin_id' not in params or
                params['trusted_origin_id'] is None):
            raise ValueError("Missing the required parameter `trusted_origin_id` when calling `update_origin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trusted_origin_id' in params:
            path_params['trustedOriginId'] = params['trusted_origin_id']  # noqa: E501

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
            '/api/v1/trustedOrigins/{trustedOriginId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrustedOrigin',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
