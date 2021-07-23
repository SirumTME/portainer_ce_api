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


class TeammembershipsTeamMembershipUpdatePayload(object):
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
        'role': 'int',
        'team_id': 'int',
        'user_id': 'int'
    }

    attribute_map = {
        'role': 'role',
        'team_id': 'teamID',
        'user_id': 'userID'
    }

    def __init__(self, role=None, team_id=None, user_id=None, _configuration=None):  # noqa: E501
        """TeammembershipsTeamMembershipUpdatePayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._role = None
        self._team_id = None
        self._user_id = None
        self.discriminator = None

        self.role = role
        self.team_id = team_id
        self.user_id = user_id

    @property
    def role(self):
        """Gets the role of this TeammembershipsTeamMembershipUpdatePayload.  # noqa: E501

        Role for the user inside the team (1 for leader and 2 for regular member)  # noqa: E501

        :return: The role of this TeammembershipsTeamMembershipUpdatePayload.  # noqa: E501
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this TeammembershipsTeamMembershipUpdatePayload.

        Role for the user inside the team (1 for leader and 2 for regular member)  # noqa: E501

        :param role: The role of this TeammembershipsTeamMembershipUpdatePayload.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def team_id(self):
        """Gets the team_id of this TeammembershipsTeamMembershipUpdatePayload.  # noqa: E501

        Team identifier  # noqa: E501

        :return: The team_id of this TeammembershipsTeamMembershipUpdatePayload.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this TeammembershipsTeamMembershipUpdatePayload.

        Team identifier  # noqa: E501

        :param team_id: The team_id of this TeammembershipsTeamMembershipUpdatePayload.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and team_id is None:
            raise ValueError("Invalid value for `team_id`, must not be `None`")  # noqa: E501

        self._team_id = team_id

    @property
    def user_id(self):
        """Gets the user_id of this TeammembershipsTeamMembershipUpdatePayload.  # noqa: E501

        User identifier  # noqa: E501

        :return: The user_id of this TeammembershipsTeamMembershipUpdatePayload.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TeammembershipsTeamMembershipUpdatePayload.

        User identifier  # noqa: E501

        :param user_id: The user_id of this TeammembershipsTeamMembershipUpdatePayload.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        if issubclass(TeammembershipsTeamMembershipUpdatePayload, dict):
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
        if not isinstance(other, TeammembershipsTeamMembershipUpdatePayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeammembershipsTeamMembershipUpdatePayload):
            return True

        return self.to_dict() != other.to_dict()
