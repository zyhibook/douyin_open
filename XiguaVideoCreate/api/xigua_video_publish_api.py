# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from douyin_open.XiguaVideoCreate.api_client import ApiClient


class XiguaVideoPublishApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def xigua_video_create_post(self, open_id, access_token, **kwargs):  # noqa: E501
        """创建西瓜视频  # noqa: E501

        * Scope: `xigua.video.create`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xigua_video_create_post(open_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :param Body1 body:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.xigua_video_create_post_with_http_info(open_id, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.xigua_video_create_post_with_http_info(open_id, access_token, **kwargs)  # noqa: E501
            return data

    def xigua_video_create_post_with_http_info(self, open_id, access_token, **kwargs):  # noqa: E501
        """创建西瓜视频  # noqa: E501

        * Scope: `xigua.video.create`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xigua_video_create_post_with_http_info(open_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :param Body1 body:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['open_id', 'access_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method xigua_video_create_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'open_id' is set
        if ('open_id' not in params or
                params['open_id'] is None):
            raise ValueError("Missing the required parameter `open_id` when calling `xigua_video_create_post`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `xigua_video_create_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'open_id' in params:
            query_params.append(('open_id', params['open_id']))  # noqa: E501
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/xigua/video/create/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def xigua_video_part_complete_post(self, open_id, access_token, upload_id, **kwargs):  # noqa: E501
        """完成上传  # noqa: E501

        * Scope: `xigua.video.create`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xigua_video_part_complete_post(open_id, access_token, upload_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :param str upload_id: 分片上传的标记。有限时间为2小时。 (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.xigua_video_part_complete_post_with_http_info(open_id, access_token, upload_id, **kwargs)  # noqa: E501
        else:
            (data) = self.xigua_video_part_complete_post_with_http_info(open_id, access_token, upload_id, **kwargs)  # noqa: E501
            return data

    def xigua_video_part_complete_post_with_http_info(self, open_id, access_token, upload_id, **kwargs):  # noqa: E501
        """完成上传  # noqa: E501

        * Scope: `xigua.video.create`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xigua_video_part_complete_post_with_http_info(open_id, access_token, upload_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :param str upload_id: 分片上传的标记。有限时间为2小时。 (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['open_id', 'access_token', 'upload_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method xigua_video_part_complete_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'open_id' is set
        if ('open_id' not in params or
                params['open_id'] is None):
            raise ValueError("Missing the required parameter `open_id` when calling `xigua_video_part_complete_post`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `xigua_video_part_complete_post`")  # noqa: E501
        # verify the required parameter 'upload_id' is set
        if ('upload_id' not in params or
                params['upload_id'] is None):
            raise ValueError("Missing the required parameter `upload_id` when calling `xigua_video_part_complete_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'open_id' in params:
            query_params.append(('open_id', params['open_id']))  # noqa: E501
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'upload_id' in params:
            query_params.append(('upload_id', params['upload_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/xigua/video/part/complete/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def xigua_video_part_init_post(self, open_id, access_token, **kwargs):  # noqa: E501
        """初始化上传  # noqa: E501

        * Scope: `xigua.video.create`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xigua_video_part_init_post(open_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.xigua_video_part_init_post_with_http_info(open_id, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.xigua_video_part_init_post_with_http_info(open_id, access_token, **kwargs)  # noqa: E501
            return data

    def xigua_video_part_init_post_with_http_info(self, open_id, access_token, **kwargs):  # noqa: E501
        """初始化上传  # noqa: E501

        * Scope: `xigua.video.create`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xigua_video_part_init_post_with_http_info(open_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['open_id', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method xigua_video_part_init_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'open_id' is set
        if ('open_id' not in params or
                params['open_id'] is None):
            raise ValueError("Missing the required parameter `open_id` when calling `xigua_video_part_init_post`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `xigua_video_part_init_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'open_id' in params:
            query_params.append(('open_id', params['open_id']))  # noqa: E501
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/xigua/video/part/init/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def xigua_video_part_upload_post(self, video, open_id, access_token, upload_id, part_number, **kwargs):  # noqa: E501
        """上传视频分片到文件服务器  # noqa: E501

        * Scope: `xigua.video.create`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xigua_video_part_upload_post(video, open_id, access_token, upload_id, part_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str video: (required)
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :param str upload_id: 分片上传的标记。有限时间为2小时。 (required)
        :param int part_number: 第几个分片，从1开始  (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.xigua_video_part_upload_post_with_http_info(video, open_id, access_token, upload_id, part_number, **kwargs)  # noqa: E501
        else:
            (data) = self.xigua_video_part_upload_post_with_http_info(video, open_id, access_token, upload_id, part_number, **kwargs)  # noqa: E501
            return data

    def xigua_video_part_upload_post_with_http_info(self, video, open_id, access_token, upload_id, part_number, **kwargs):  # noqa: E501
        """上传视频分片到文件服务器  # noqa: E501

        * Scope: `xigua.video.create`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xigua_video_part_upload_post_with_http_info(video, open_id, access_token, upload_id, part_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str video: (required)
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :param str upload_id: 分片上传的标记。有限时间为2小时。 (required)
        :param int part_number: 第几个分片，从1开始  (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video', 'open_id', 'access_token', 'upload_id', 'part_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method xigua_video_part_upload_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video' is set
        if ('video' not in params or
                params['video'] is None):
            raise ValueError("Missing the required parameter `video` when calling `xigua_video_part_upload_post`")  # noqa: E501
        # verify the required parameter 'open_id' is set
        if ('open_id' not in params or
                params['open_id'] is None):
            raise ValueError("Missing the required parameter `open_id` when calling `xigua_video_part_upload_post`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `xigua_video_part_upload_post`")  # noqa: E501
        # verify the required parameter 'upload_id' is set
        if ('upload_id' not in params or
                params['upload_id'] is None):
            raise ValueError("Missing the required parameter `upload_id` when calling `xigua_video_part_upload_post`")  # noqa: E501
        # verify the required parameter 'part_number' is set
        if ('part_number' not in params or
                params['part_number'] is None):
            raise ValueError("Missing the required parameter `part_number` when calling `xigua_video_part_upload_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'open_id' in params:
            query_params.append(('open_id', params['open_id']))  # noqa: E501
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'upload_id' in params:
            query_params.append(('upload_id', params['upload_id']))  # noqa: E501
        if 'part_number' in params:
            query_params.append(('part_number', params['part_number']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'video' in params:
            local_var_files['video'] = params['video']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/xigua/video/part/upload/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def xigua_video_upload_post(self, video, open_id, access_token, **kwargs):  # noqa: E501
        """上传视频到文件服务器  # noqa: E501

        * Scope: `xigua.video.create`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xigua_video_upload_post(video, open_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str video: (required)
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.xigua_video_upload_post_with_http_info(video, open_id, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.xigua_video_upload_post_with_http_info(video, open_id, access_token, **kwargs)  # noqa: E501
            return data

    def xigua_video_upload_post_with_http_info(self, video, open_id, access_token, **kwargs):  # noqa: E501
        """上传视频到文件服务器  # noqa: E501

        * Scope: `xigua.video.create`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.xigua_video_upload_post_with_http_info(video, open_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str video: (required)
        :param str open_id: 通过/oauth/access_token/获取，用户唯一标志 (required)
        :param str access_token: 调用/oauth/access_token/生成的token，此token需要用户授权。 (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video', 'open_id', 'access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method xigua_video_upload_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video' is set
        if ('video' not in params or
                params['video'] is None):
            raise ValueError("Missing the required parameter `video` when calling `xigua_video_upload_post`")  # noqa: E501
        # verify the required parameter 'open_id' is set
        if ('open_id' not in params or
                params['open_id'] is None):
            raise ValueError("Missing the required parameter `open_id` when calling `xigua_video_upload_post`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `xigua_video_upload_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'open_id' in params:
            query_params.append(('open_id', params['open_id']))  # noqa: E501
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'video' in params:
            local_var_files['video'] = params['video']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/xigua/video/upload/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
