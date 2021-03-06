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


class PortainerUser(object):
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
        'endpoint_authorizations': 'PortainerEndpointAuthorizations',
        'id': 'int',
        'password': 'str',
        'portainer_authorizations': 'PortainerAuthorizations',
        'role': 'int',
        'username': 'str'
    }

    attribute_map = {
        'endpoint_authorizations': 'EndpointAuthorizations',
        'id': 'Id',
        'password': 'Password',
        'portainer_authorizations': 'PortainerAuthorizations',
        'role': 'Role',
        'username': 'Username'
    }

    def __init__(self, endpoint_authorizations=None, id=None, password=None, portainer_authorizations=None, role=None, username=None, _configuration=None):  # noqa: E501
        """PortainerUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._endpoint_authorizations = None
        self._id = None
        self._password = None
        self._portainer_authorizations = None
        self._role = None
        self._username = None
        self.discriminator = None

        if endpoint_authorizations is not None:
            self.endpoint_authorizations = endpoint_authorizations
        if id is not None:
            self.id = id
        if password is not None:
            self.password = password
        if portainer_authorizations is not None:
            self.portainer_authorizations = portainer_authorizations
        if role is not None:
            self.role = role
        if username is not None:
            self.username = username

    @property
    def endpoint_authorizations(self):
        """Gets the endpoint_authorizations of this PortainerUser.  # noqa: E501


        :return: The endpoint_authorizations of this PortainerUser.  # noqa: E501
        :rtype: PortainerEndpointAuthorizations
        """
        return self._endpoint_authorizations

    @endpoint_authorizations.setter
    def endpoint_authorizations(self, endpoint_authorizations):
        """Sets the endpoint_authorizations of this PortainerUser.


        :param endpoint_authorizations: The endpoint_authorizations of this PortainerUser.  # noqa: E501
        :type: PortainerEndpointAuthorizations
        """

        self._endpoint_authorizations = endpoint_authorizations

    @property
    def id(self):
        """Gets the id of this PortainerUser.  # noqa: E501

        User Identifier  # noqa: E501

        :return: The id of this PortainerUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortainerUser.

        User Identifier  # noqa: E501

        :param id: The id of this PortainerUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def password(self):
        """Gets the password of this PortainerUser.  # noqa: E501


        :return: The password of this PortainerUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PortainerUser.


        :param password: The password of this PortainerUser.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def portainer_authorizations(self):
        """Gets the portainer_authorizations of this PortainerUser.  # noqa: E501

        Deprecated fields Deprecated in DBVersion == 25  # noqa: E501

        :return: The portainer_authorizations of this PortainerUser.  # noqa: E501
        :rtype: PortainerAuthorizations
        """
        return self._portainer_authorizations

    @portainer_authorizations.setter
    def portainer_authorizations(self, portainer_authorizations):
        """Sets the portainer_authorizations of this PortainerUser.

        Deprecated fields Deprecated in DBVersion == 25  # noqa: E501

        :param portainer_authorizations: The portainer_authorizations of this PortainerUser.  # noqa: E501
        :type: PortainerAuthorizations
        """

        self._portainer_authorizations = portainer_authorizations

    @property
    def role(self):
        """Gets the role of this PortainerUser.  # noqa: E501

        User role (1 for administrator account and 2 for regular account)  # noqa: E501

        :return: The role of this PortainerUser.  # noqa: E501
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this PortainerUser.

        User role (1 for administrator account and 2 for regular account)  # noqa: E501

        :param role: The role of this PortainerUser.  # noqa: E501
        :type: int
        """

        self._role = role

    @property
    def username(self):
        """Gets the username of this PortainerUser.  # noqa: E501


        :return: The username of this PortainerUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this PortainerUser.


        :param username: The username of this PortainerUser.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(PortainerUser, dict):
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
        if not isinstance(other, PortainerUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortainerUser):
            return True

        return self.to_dict() != other.to_dict()
