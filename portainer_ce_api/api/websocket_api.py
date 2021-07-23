# coding: utf-8

"""
    PortainerCE API

    Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API. Examples are available at https://documentation.portainer.io/api/api-examples/ You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).  # Authentication  Most of the API endpoints require to be authenticated as well as some level of authorization to be used. Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request with the **Bearer** authentication mechanism.  Example:  ``` Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE ```  # Security  Each API endpoint has an associated access policy, it is documented in the description of each endpoint.  Different access policies are available:  - Public access - Authenticated access - Restricted access - Administrator access  ### Public access  No authentication is required to access the endpoints with this access policy.  ### Authenticated access  Authentication is required to access the endpoints with this access policy.  ### Restricted access  Authentication is required to access the endpoints with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.  ### Administrator access  Authentication as well as an administrator role are required to access the endpoints with this access policy.  # Execute Docker requests  Portainer **DOES NOT** expose specific endpoints to manage your Docker resources (create a container, remove a volume, etc...).  Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.  To do so, you can use the `/endpoints/{id}/docker` Portainer API endpoint (which is not documented below due to Swagger limitations). This endpoint has a restricted access policy so you still need to be authenticated to be able to query this endpoint. Any query on this endpoint will be proxied to the Docker API of the associated endpoint (requests and responses objects are the same as documented in the Docker API).  **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://documentation.portainer.io/api/api-examples/).   # noqa: E501

    OpenAPI spec version: 2.6.0
    Contact: info@portainer.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from portainer_ce_api.api_client import ApiClient


class WebsocketApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def websocket_attach_get(self, endpoint_id, token, **kwargs):  # noqa: E501
        """Attach a websocket  # noqa: E501

        If the nodeName query parameter is present, the request will be proxied to the underlying agent endpoint. If the nodeName query parameter is not specified, the request will be upgraded to the websocket protocol and an AttachStart operation HTTP request will be created and hijacked. Authentication and access is controlled via the mandatory token query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.websocket_attach_get(endpoint_id, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int endpoint_id: endpoint ID of the endpoint where the resource is located (required)
        :param str token: JWT token used for authentication against this endpoint (required)
        :param str node_name: node name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.websocket_attach_get_with_http_info(endpoint_id, token, **kwargs)  # noqa: E501
        else:
            (data) = self.websocket_attach_get_with_http_info(endpoint_id, token, **kwargs)  # noqa: E501
            return data

    def websocket_attach_get_with_http_info(self, endpoint_id, token, **kwargs):  # noqa: E501
        """Attach a websocket  # noqa: E501

        If the nodeName query parameter is present, the request will be proxied to the underlying agent endpoint. If the nodeName query parameter is not specified, the request will be upgraded to the websocket protocol and an AttachStart operation HTTP request will be created and hijacked. Authentication and access is controlled via the mandatory token query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.websocket_attach_get_with_http_info(endpoint_id, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int endpoint_id: endpoint ID of the endpoint where the resource is located (required)
        :param str token: JWT token used for authentication against this endpoint (required)
        :param str node_name: node name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id', 'token', 'node_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method websocket_attach_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if self.api_client.client_side_validation and ('endpoint_id' not in params or
                                                       params['endpoint_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `endpoint_id` when calling `websocket_attach_get`")  # noqa: E501
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in params or
                                                       params['token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `token` when calling `websocket_attach_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint_id' in params:
            query_params.append(('endpointId', params['endpoint_id']))  # noqa: E501
        if 'node_name' in params:
            query_params.append(('nodeName', params['node_name']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt']  # noqa: E501

        return self.api_client.call_api(
            '/websocket/attach', 'GET',
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

    def websocket_exec_get(self, endpoint_id, token, **kwargs):  # noqa: E501
        """Execute a websocket  # noqa: E501

        If the nodeName query parameter is present, the request will be proxied to the underlying agent endpoint. If the nodeName query parameter is not specified, the request will be upgraded to the websocket protocol and an ExecStart operation HTTP request will be created and hijacked. Authentication and access is controlled via the mandatory token query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.websocket_exec_get(endpoint_id, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int endpoint_id: endpoint ID of the endpoint where the resource is located (required)
        :param str token: JWT token used for authentication against this endpoint (required)
        :param str node_name: node name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.websocket_exec_get_with_http_info(endpoint_id, token, **kwargs)  # noqa: E501
        else:
            (data) = self.websocket_exec_get_with_http_info(endpoint_id, token, **kwargs)  # noqa: E501
            return data

    def websocket_exec_get_with_http_info(self, endpoint_id, token, **kwargs):  # noqa: E501
        """Execute a websocket  # noqa: E501

        If the nodeName query parameter is present, the request will be proxied to the underlying agent endpoint. If the nodeName query parameter is not specified, the request will be upgraded to the websocket protocol and an ExecStart operation HTTP request will be created and hijacked. Authentication and access is controlled via the mandatory token query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.websocket_exec_get_with_http_info(endpoint_id, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int endpoint_id: endpoint ID of the endpoint where the resource is located (required)
        :param str token: JWT token used for authentication against this endpoint (required)
        :param str node_name: node name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id', 'token', 'node_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method websocket_exec_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if self.api_client.client_side_validation and ('endpoint_id' not in params or
                                                       params['endpoint_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `endpoint_id` when calling `websocket_exec_get`")  # noqa: E501
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in params or
                                                       params['token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `token` when calling `websocket_exec_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint_id' in params:
            query_params.append(('endpointId', params['endpoint_id']))  # noqa: E501
        if 'node_name' in params:
            query_params.append(('nodeName', params['node_name']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt']  # noqa: E501

        return self.api_client.call_api(
            '/websocket/exec', 'GET',
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

    def websocket_pod_get(self, endpoint_id, namespace, pod_name, container_name, command, token, **kwargs):  # noqa: E501
        """Execute a websocket on pod  # noqa: E501

        The request will be upgraded to the websocket protocol. Authentication and access is controlled via the mandatory token query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.websocket_pod_get(endpoint_id, namespace, pod_name, container_name, command, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int endpoint_id: endpoint ID of the endpoint where the resource is located (required)
        :param str namespace: namespace where the container is located (required)
        :param str pod_name: name of the pod containing the container (required)
        :param str container_name: name of the container (required)
        :param str command: command to execute in the container (required)
        :param str token: JWT token used for authentication against this endpoint (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.websocket_pod_get_with_http_info(endpoint_id, namespace, pod_name, container_name, command, token, **kwargs)  # noqa: E501
        else:
            (data) = self.websocket_pod_get_with_http_info(endpoint_id, namespace, pod_name, container_name, command, token, **kwargs)  # noqa: E501
            return data

    def websocket_pod_get_with_http_info(self, endpoint_id, namespace, pod_name, container_name, command, token, **kwargs):  # noqa: E501
        """Execute a websocket on pod  # noqa: E501

        The request will be upgraded to the websocket protocol. Authentication and access is controlled via the mandatory token query parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.websocket_pod_get_with_http_info(endpoint_id, namespace, pod_name, container_name, command, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int endpoint_id: endpoint ID of the endpoint where the resource is located (required)
        :param str namespace: namespace where the container is located (required)
        :param str pod_name: name of the pod containing the container (required)
        :param str container_name: name of the container (required)
        :param str command: command to execute in the container (required)
        :param str token: JWT token used for authentication against this endpoint (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpoint_id', 'namespace', 'pod_name', 'container_name', 'command', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method websocket_pod_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpoint_id' is set
        if self.api_client.client_side_validation and ('endpoint_id' not in params or
                                                       params['endpoint_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `endpoint_id` when calling `websocket_pod_get`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in params or
                                                       params['namespace'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespace` when calling `websocket_pod_get`")  # noqa: E501
        # verify the required parameter 'pod_name' is set
        if self.api_client.client_side_validation and ('pod_name' not in params or
                                                       params['pod_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `pod_name` when calling `websocket_pod_get`")  # noqa: E501
        # verify the required parameter 'container_name' is set
        if self.api_client.client_side_validation and ('container_name' not in params or
                                                       params['container_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `container_name` when calling `websocket_pod_get`")  # noqa: E501
        # verify the required parameter 'command' is set
        if self.api_client.client_side_validation and ('command' not in params or
                                                       params['command'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `command` when calling `websocket_pod_get`")  # noqa: E501
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in params or
                                                       params['token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `token` when calling `websocket_pod_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint_id' in params:
            query_params.append(('endpointId', params['endpoint_id']))  # noqa: E501
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501
        if 'pod_name' in params:
            query_params.append(('podName', params['pod_name']))  # noqa: E501
        if 'container_name' in params:
            query_params.append(('containerName', params['container_name']))  # noqa: E501
        if 'command' in params:
            query_params.append(('command', params['command']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt']  # noqa: E501

        return self.api_client.call_api(
            '/websocket/pod', 'GET',
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