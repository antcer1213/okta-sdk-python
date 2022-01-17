# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.9.2
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from okta.swagger_api_client import ApiClient


class EventHook(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def activate_event_hook(self, event_hook_id, **kwargs):  # noqa: E501
        """activate_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_event_hook(event_hook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.activate_event_hook_with_http_info(event_hook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.activate_event_hook_with_http_info(event_hook_id, **kwargs)  # noqa: E501
            return data

    def activate_event_hook_with_http_info(self, event_hook_id, **kwargs):  # noqa: E501
        """activate_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_event_hook_with_http_info(event_hook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_hook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_event_hook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_hook_id' is set
        if ('event_hook_id' not in params or
                params['event_hook_id'] is None):
            raise ValueError("Missing the required parameter `event_hook_id` when calling `activate_event_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_hook_id' in params:
            path_params['eventHookId'] = params['event_hook_id']  # noqa: E501

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
            '/api/v1/eventHooks/{eventHookId}/lifecycle/activate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_event_hook(self, body, **kwargs):  # noqa: E501
        """create_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_event_hook(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EventHook body: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_event_hook_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_event_hook_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_event_hook_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_event_hook_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EventHook body: (required)
        :return: EventHook
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
                    " to method create_event_hook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_event_hook`")  # noqa: E501

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
            '/api/v1/eventHooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deactivate_event_hook(self, event_hook_id, **kwargs):  # noqa: E501
        """deactivate_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deactivate_event_hook(event_hook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deactivate_event_hook_with_http_info(event_hook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.deactivate_event_hook_with_http_info(event_hook_id, **kwargs)  # noqa: E501
            return data

    def deactivate_event_hook_with_http_info(self, event_hook_id, **kwargs):  # noqa: E501
        """deactivate_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deactivate_event_hook_with_http_info(event_hook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_hook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deactivate_event_hook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_hook_id' is set
        if ('event_hook_id' not in params or
                params['event_hook_id'] is None):
            raise ValueError("Missing the required parameter `event_hook_id` when calling `deactivate_event_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_hook_id' in params:
            path_params['eventHookId'] = params['event_hook_id']  # noqa: E501

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
            '/api/v1/eventHooks/{eventHookId}/lifecycle/deactivate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_event_hook(self, event_hook_id, **kwargs):  # noqa: E501
        """delete_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_event_hook(event_hook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_event_hook_with_http_info(event_hook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_event_hook_with_http_info(event_hook_id, **kwargs)  # noqa: E501
            return data

    def delete_event_hook_with_http_info(self, event_hook_id, **kwargs):  # noqa: E501
        """delete_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_event_hook_with_http_info(event_hook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_hook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_event_hook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_hook_id' is set
        if ('event_hook_id' not in params or
                params['event_hook_id'] is None):
            raise ValueError("Missing the required parameter `event_hook_id` when calling `delete_event_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_hook_id' in params:
            path_params['eventHookId'] = params['event_hook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/eventHooks/{eventHookId}', 'DELETE',
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

    def get_event_hook(self, event_hook_id, **kwargs):  # noqa: E501
        """get_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_hook(event_hook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_event_hook_with_http_info(event_hook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_event_hook_with_http_info(event_hook_id, **kwargs)  # noqa: E501
            return data

    def get_event_hook_with_http_info(self, event_hook_id, **kwargs):  # noqa: E501
        """get_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_hook_with_http_info(event_hook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_hook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event_hook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_hook_id' is set
        if ('event_hook_id' not in params or
                params['event_hook_id'] is None):
            raise ValueError("Missing the required parameter `event_hook_id` when calling `get_event_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_hook_id' in params:
            path_params['eventHookId'] = params['event_hook_id']  # noqa: E501

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
            '/api/v1/eventHooks/{eventHookId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_event_hooks(self, **kwargs):  # noqa: E501
        """list_event_hooks  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_event_hooks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[EventHook]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_event_hooks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_event_hooks_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_event_hooks_with_http_info(self, **kwargs):  # noqa: E501
        """list_event_hooks  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_event_hooks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[EventHook]
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
                    " to method list_event_hooks" % key
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
            '/api/v1/eventHooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EventHook]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_event_hook(self, event_hook_id, body, **kwargs):  # noqa: E501
        """update_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_event_hook(event_hook_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :param EventHook body: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_event_hook_with_http_info(event_hook_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_event_hook_with_http_info(event_hook_id, body, **kwargs)  # noqa: E501
            return data

    def update_event_hook_with_http_info(self, event_hook_id, body, **kwargs):  # noqa: E501
        """update_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_event_hook_with_http_info(event_hook_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :param EventHook body: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_hook_id''body', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_event_hook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_hook_id' is set
        if ('event_hook_id' not in params or
                params['event_hook_id'] is None):
            raise ValueError("Missing the required parameter `event_hook_id` when calling `update_event_hook`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_event_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_hook_id' in params:
            path_params['eventHookId'] = params['event_hook_id']  # noqa: E501

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
            '/api/v1/eventHooks/{eventHookId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_event_hook(self, event_hook_id, **kwargs):  # noqa: E501
        """verify_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_event_hook(event_hook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_event_hook_with_http_info(event_hook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_event_hook_with_http_info(event_hook_id, **kwargs)  # noqa: E501
            return data

    def verify_event_hook_with_http_info(self, event_hook_id, **kwargs):  # noqa: E501
        """verify_event_hook  # noqa: E501

        Success  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_event_hook_with_http_info(event_hook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_hook_id: (required)
        :return: EventHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_hook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify_event_hook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_hook_id' is set
        if ('event_hook_id' not in params or
                params['event_hook_id'] is None):
            raise ValueError("Missing the required parameter `event_hook_id` when calling `verify_event_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_hook_id' in params:
            path_params['eventHookId'] = params['event_hook_id']  # noqa: E501

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
            '/api/v1/eventHooks/{eventHookId}/lifecycle/verify', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
