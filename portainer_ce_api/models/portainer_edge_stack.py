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


class PortainerEdgeStack(object):
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
        'creation_date': 'int',
        'edge_groups': 'list[int]',
        'entry_point': 'str',
        'id': 'int',
        'name': 'str',
        'project_path': 'str',
        'prune': 'bool',
        'status': 'dict(str, PortainerEdgeStackStatus)',
        'version': 'int'
    }

    attribute_map = {
        'creation_date': 'CreationDate',
        'edge_groups': 'EdgeGroups',
        'entry_point': 'EntryPoint',
        'id': 'Id',
        'name': 'Name',
        'project_path': 'ProjectPath',
        'prune': 'Prune',
        'status': 'Status',
        'version': 'Version'
    }

    def __init__(self, creation_date=None, edge_groups=None, entry_point=None, id=None, name=None, project_path=None, prune=None, status=None, version=None, _configuration=None):  # noqa: E501
        """PortainerEdgeStack - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_date = None
        self._edge_groups = None
        self._entry_point = None
        self._id = None
        self._name = None
        self._project_path = None
        self._prune = None
        self._status = None
        self._version = None
        self.discriminator = None

        if creation_date is not None:
            self.creation_date = creation_date
        if edge_groups is not None:
            self.edge_groups = edge_groups
        if entry_point is not None:
            self.entry_point = entry_point
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_path is not None:
            self.project_path = project_path
        if prune is not None:
            self.prune = prune
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version

    @property
    def creation_date(self):
        """Gets the creation_date of this PortainerEdgeStack.  # noqa: E501


        :return: The creation_date of this PortainerEdgeStack.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this PortainerEdgeStack.


        :param creation_date: The creation_date of this PortainerEdgeStack.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def edge_groups(self):
        """Gets the edge_groups of this PortainerEdgeStack.  # noqa: E501


        :return: The edge_groups of this PortainerEdgeStack.  # noqa: E501
        :rtype: list[int]
        """
        return self._edge_groups

    @edge_groups.setter
    def edge_groups(self, edge_groups):
        """Sets the edge_groups of this PortainerEdgeStack.


        :param edge_groups: The edge_groups of this PortainerEdgeStack.  # noqa: E501
        :type: list[int]
        """

        self._edge_groups = edge_groups

    @property
    def entry_point(self):
        """Gets the entry_point of this PortainerEdgeStack.  # noqa: E501


        :return: The entry_point of this PortainerEdgeStack.  # noqa: E501
        :rtype: str
        """
        return self._entry_point

    @entry_point.setter
    def entry_point(self, entry_point):
        """Sets the entry_point of this PortainerEdgeStack.


        :param entry_point: The entry_point of this PortainerEdgeStack.  # noqa: E501
        :type: str
        """

        self._entry_point = entry_point

    @property
    def id(self):
        """Gets the id of this PortainerEdgeStack.  # noqa: E501

        EdgeStack Identifier  # noqa: E501

        :return: The id of this PortainerEdgeStack.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortainerEdgeStack.

        EdgeStack Identifier  # noqa: E501

        :param id: The id of this PortainerEdgeStack.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PortainerEdgeStack.  # noqa: E501


        :return: The name of this PortainerEdgeStack.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PortainerEdgeStack.


        :param name: The name of this PortainerEdgeStack.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_path(self):
        """Gets the project_path of this PortainerEdgeStack.  # noqa: E501


        :return: The project_path of this PortainerEdgeStack.  # noqa: E501
        :rtype: str
        """
        return self._project_path

    @project_path.setter
    def project_path(self, project_path):
        """Sets the project_path of this PortainerEdgeStack.


        :param project_path: The project_path of this PortainerEdgeStack.  # noqa: E501
        :type: str
        """

        self._project_path = project_path

    @property
    def prune(self):
        """Gets the prune of this PortainerEdgeStack.  # noqa: E501


        :return: The prune of this PortainerEdgeStack.  # noqa: E501
        :rtype: bool
        """
        return self._prune

    @prune.setter
    def prune(self, prune):
        """Sets the prune of this PortainerEdgeStack.


        :param prune: The prune of this PortainerEdgeStack.  # noqa: E501
        :type: bool
        """

        self._prune = prune

    @property
    def status(self):
        """Gets the status of this PortainerEdgeStack.  # noqa: E501


        :return: The status of this PortainerEdgeStack.  # noqa: E501
        :rtype: dict(str, PortainerEdgeStackStatus)
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PortainerEdgeStack.


        :param status: The status of this PortainerEdgeStack.  # noqa: E501
        :type: dict(str, PortainerEdgeStackStatus)
        """

        self._status = status

    @property
    def version(self):
        """Gets the version of this PortainerEdgeStack.  # noqa: E501


        :return: The version of this PortainerEdgeStack.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PortainerEdgeStack.


        :param version: The version of this PortainerEdgeStack.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(PortainerEdgeStack, dict):
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
        if not isinstance(other, PortainerEdgeStack):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortainerEdgeStack):
            return True

        return self.to_dict() != other.to_dict()
