# coding: utf-8

"""
    PortainerCE API

    Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API. Examples are available at https://documentation.portainer.io/api/api-examples/ You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).  # Authentication  Most of the API endpoints require to be authenticated as well as some level of authorization to be used. Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request with the **Bearer** authentication mechanism.  Example:  ``` Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE ```  # Security  Each API endpoint has an associated access policy, it is documented in the description of each endpoint.  Different access policies are available:  - Public access - Authenticated access - Restricted access - Administrator access  ### Public access  No authentication is required to access the endpoints with this access policy.  ### Authenticated access  Authentication is required to access the endpoints with this access policy.  ### Restricted access  Authentication is required to access the endpoints with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.  ### Administrator access  Authentication as well as an administrator role are required to access the endpoints with this access policy.  # Execute Docker requests  Portainer **DOES NOT** expose specific endpoints to manage your Docker resources (create a container, remove a volume, etc...).  Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.  To do so, you can use the `/endpoints/{id}/docker` Portainer API endpoint (which is not documented below due to Swagger limitations). This endpoint has a restricted access policy so you still need to be authenticated to be able to query this endpoint. Any query on this endpoint will be proxied to the Docker API of the associated endpoint (requests and responses objects are the same as documented in the Docker API).  **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://documentation.portainer.io/api/api-examples/).   # noqa: E501

    OpenAPI spec version: 2.6.0
    Contact: info@portainer.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from portainer_ce_api.configuration import Configuration


class EndpointgroupsEndpointGroupUpdatePayload(object):
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
        'description': 'str',
        'name': 'str',
        'tag_i_ds': 'list[int]',
        'team_access_policies': 'PortainerTeamAccessPolicies',
        'user_access_policies': 'PortainerUserAccessPolicies'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'tag_i_ds': 'tagIDs',
        'team_access_policies': 'teamAccessPolicies',
        'user_access_policies': 'userAccessPolicies'
    }

    def __init__(self, description=None, name=None, tag_i_ds=None, team_access_policies=None, user_access_policies=None, _configuration=None):  # noqa: E501
        """EndpointgroupsEndpointGroupUpdatePayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._name = None
        self._tag_i_ds = None
        self._team_access_policies = None
        self._user_access_policies = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if tag_i_ds is not None:
            self.tag_i_ds = tag_i_ds
        if team_access_policies is not None:
            self.team_access_policies = team_access_policies
        if user_access_policies is not None:
            self.user_access_policies = user_access_policies

    @property
    def description(self):
        """Gets the description of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501

        Endpoint group description  # noqa: E501

        :return: The description of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EndpointgroupsEndpointGroupUpdatePayload.

        Endpoint group description  # noqa: E501

        :param description: The description of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501

        Endpoint group name  # noqa: E501

        :return: The name of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EndpointgroupsEndpointGroupUpdatePayload.

        Endpoint group name  # noqa: E501

        :param name: The name of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tag_i_ds(self):
        """Gets the tag_i_ds of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501

        List of tag identifiers associated to the endpoint group  # noqa: E501

        :return: The tag_i_ds of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501
        :rtype: list[int]
        """
        return self._tag_i_ds

    @tag_i_ds.setter
    def tag_i_ds(self, tag_i_ds):
        """Sets the tag_i_ds of this EndpointgroupsEndpointGroupUpdatePayload.

        List of tag identifiers associated to the endpoint group  # noqa: E501

        :param tag_i_ds: The tag_i_ds of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501
        :type: list[int]
        """

        self._tag_i_ds = tag_i_ds

    @property
    def team_access_policies(self):
        """Gets the team_access_policies of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501


        :return: The team_access_policies of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501
        :rtype: PortainerTeamAccessPolicies
        """
        return self._team_access_policies

    @team_access_policies.setter
    def team_access_policies(self, team_access_policies):
        """Sets the team_access_policies of this EndpointgroupsEndpointGroupUpdatePayload.


        :param team_access_policies: The team_access_policies of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501
        :type: PortainerTeamAccessPolicies
        """

        self._team_access_policies = team_access_policies

    @property
    def user_access_policies(self):
        """Gets the user_access_policies of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501


        :return: The user_access_policies of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501
        :rtype: PortainerUserAccessPolicies
        """
        return self._user_access_policies

    @user_access_policies.setter
    def user_access_policies(self, user_access_policies):
        """Sets the user_access_policies of this EndpointgroupsEndpointGroupUpdatePayload.


        :param user_access_policies: The user_access_policies of this EndpointgroupsEndpointGroupUpdatePayload.  # noqa: E501
        :type: PortainerUserAccessPolicies
        """

        self._user_access_policies = user_access_policies

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
        if issubclass(EndpointgroupsEndpointGroupUpdatePayload, dict):
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
        if not isinstance(other, EndpointgroupsEndpointGroupUpdatePayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndpointgroupsEndpointGroupUpdatePayload):
            return True

        return self.to_dict() != other.to_dict()
