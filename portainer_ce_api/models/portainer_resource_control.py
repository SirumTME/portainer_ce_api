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


class PortainerResourceControl(object):
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
        'access_level': 'int',
        'administrators_only': 'bool',
        'id': 'int',
        'owner_id': 'int',
        'public': 'bool',
        'resource_id': 'str',
        'sub_resource_ids': 'list[str]',
        'system': 'bool',
        'team_accesses': 'list[PortainerTeamResourceAccess]',
        'type': 'int',
        'user_accesses': 'list[PortainerUserResourceAccess]'
    }

    attribute_map = {
        'access_level': 'AccessLevel',
        'administrators_only': 'AdministratorsOnly',
        'id': 'Id',
        'owner_id': 'OwnerId',
        'public': 'Public',
        'resource_id': 'ResourceId',
        'sub_resource_ids': 'SubResourceIds',
        'system': 'System',
        'team_accesses': 'TeamAccesses',
        'type': 'Type',
        'user_accesses': 'UserAccesses'
    }

    def __init__(self, access_level=None, administrators_only=None, id=None, owner_id=None, public=None, resource_id=None, sub_resource_ids=None, system=None, team_accesses=None, type=None, user_accesses=None, _configuration=None):  # noqa: E501
        """PortainerResourceControl - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_level = None
        self._administrators_only = None
        self._id = None
        self._owner_id = None
        self._public = None
        self._resource_id = None
        self._sub_resource_ids = None
        self._system = None
        self._team_accesses = None
        self._type = None
        self._user_accesses = None
        self.discriminator = None

        if access_level is not None:
            self.access_level = access_level
        if administrators_only is not None:
            self.administrators_only = administrators_only
        if id is not None:
            self.id = id
        if owner_id is not None:
            self.owner_id = owner_id
        if public is not None:
            self.public = public
        if resource_id is not None:
            self.resource_id = resource_id
        if sub_resource_ids is not None:
            self.sub_resource_ids = sub_resource_ids
        if system is not None:
            self.system = system
        if team_accesses is not None:
            self.team_accesses = team_accesses
        if type is not None:
            self.type = type
        if user_accesses is not None:
            self.user_accesses = user_accesses

    @property
    def access_level(self):
        """Gets the access_level of this PortainerResourceControl.  # noqa: E501


        :return: The access_level of this PortainerResourceControl.  # noqa: E501
        :rtype: int
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this PortainerResourceControl.


        :param access_level: The access_level of this PortainerResourceControl.  # noqa: E501
        :type: int
        """

        self._access_level = access_level

    @property
    def administrators_only(self):
        """Gets the administrators_only of this PortainerResourceControl.  # noqa: E501

        Permit access to resource only to admins  # noqa: E501

        :return: The administrators_only of this PortainerResourceControl.  # noqa: E501
        :rtype: bool
        """
        return self._administrators_only

    @administrators_only.setter
    def administrators_only(self, administrators_only):
        """Sets the administrators_only of this PortainerResourceControl.

        Permit access to resource only to admins  # noqa: E501

        :param administrators_only: The administrators_only of this PortainerResourceControl.  # noqa: E501
        :type: bool
        """

        self._administrators_only = administrators_only

    @property
    def id(self):
        """Gets the id of this PortainerResourceControl.  # noqa: E501

        ResourceControl Identifier  # noqa: E501

        :return: The id of this PortainerResourceControl.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortainerResourceControl.

        ResourceControl Identifier  # noqa: E501

        :param id: The id of this PortainerResourceControl.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def owner_id(self):
        """Gets the owner_id of this PortainerResourceControl.  # noqa: E501

        Deprecated fields Deprecated in DBVersion == 2  # noqa: E501

        :return: The owner_id of this PortainerResourceControl.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this PortainerResourceControl.

        Deprecated fields Deprecated in DBVersion == 2  # noqa: E501

        :param owner_id: The owner_id of this PortainerResourceControl.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def public(self):
        """Gets the public of this PortainerResourceControl.  # noqa: E501

        Permit access to the associated resource to any user  # noqa: E501

        :return: The public of this PortainerResourceControl.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this PortainerResourceControl.

        Permit access to the associated resource to any user  # noqa: E501

        :param public: The public of this PortainerResourceControl.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def resource_id(self):
        """Gets the resource_id of this PortainerResourceControl.  # noqa: E501

        Docker resource identifier on which access control will be applied.\\ In the case of a resource control applied to a stack, use the stack name as identifier  # noqa: E501

        :return: The resource_id of this PortainerResourceControl.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this PortainerResourceControl.

        Docker resource identifier on which access control will be applied.\\ In the case of a resource control applied to a stack, use the stack name as identifier  # noqa: E501

        :param resource_id: The resource_id of this PortainerResourceControl.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def sub_resource_ids(self):
        """Gets the sub_resource_ids of this PortainerResourceControl.  # noqa: E501

        List of Docker resources that will inherit this access control  # noqa: E501

        :return: The sub_resource_ids of this PortainerResourceControl.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_resource_ids

    @sub_resource_ids.setter
    def sub_resource_ids(self, sub_resource_ids):
        """Sets the sub_resource_ids of this PortainerResourceControl.

        List of Docker resources that will inherit this access control  # noqa: E501

        :param sub_resource_ids: The sub_resource_ids of this PortainerResourceControl.  # noqa: E501
        :type: list[str]
        """

        self._sub_resource_ids = sub_resource_ids

    @property
    def system(self):
        """Gets the system of this PortainerResourceControl.  # noqa: E501


        :return: The system of this PortainerResourceControl.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this PortainerResourceControl.


        :param system: The system of this PortainerResourceControl.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def team_accesses(self):
        """Gets the team_accesses of this PortainerResourceControl.  # noqa: E501


        :return: The team_accesses of this PortainerResourceControl.  # noqa: E501
        :rtype: list[PortainerTeamResourceAccess]
        """
        return self._team_accesses

    @team_accesses.setter
    def team_accesses(self, team_accesses):
        """Sets the team_accesses of this PortainerResourceControl.


        :param team_accesses: The team_accesses of this PortainerResourceControl.  # noqa: E501
        :type: list[PortainerTeamResourceAccess]
        """

        self._team_accesses = team_accesses

    @property
    def type(self):
        """Gets the type of this PortainerResourceControl.  # noqa: E501

        Type of Docker resource. Valid values are: 1- container, 2 -service 3 - volume, 4 - secret, 5 - stack, 6 - config or 7 - custom template  # noqa: E501

        :return: The type of this PortainerResourceControl.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PortainerResourceControl.

        Type of Docker resource. Valid values are: 1- container, 2 -service 3 - volume, 4 - secret, 5 - stack, 6 - config or 7 - custom template  # noqa: E501

        :param type: The type of this PortainerResourceControl.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def user_accesses(self):
        """Gets the user_accesses of this PortainerResourceControl.  # noqa: E501


        :return: The user_accesses of this PortainerResourceControl.  # noqa: E501
        :rtype: list[PortainerUserResourceAccess]
        """
        return self._user_accesses

    @user_accesses.setter
    def user_accesses(self, user_accesses):
        """Sets the user_accesses of this PortainerResourceControl.


        :param user_accesses: The user_accesses of this PortainerResourceControl.  # noqa: E501
        :type: list[PortainerUserResourceAccess]
        """

        self._user_accesses = user_accesses

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
        if issubclass(PortainerResourceControl, dict):
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
        if not isinstance(other, PortainerResourceControl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortainerResourceControl):
            return True

        return self.to_dict() != other.to_dict()