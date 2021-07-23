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


class StacksSwarmStackFromGitRepositoryPayload(object):
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
        'compose_file_path_in_repository': 'str',
        'env': 'list[PortainerPair]',
        'name': 'str',
        'repository_authentication': 'bool',
        'repository_password': 'str',
        'repository_reference_name': 'str',
        'repository_url': 'str',
        'repository_username': 'str',
        'swarm_id': 'str'
    }

    attribute_map = {
        'compose_file_path_in_repository': 'composeFilePathInRepository',
        'env': 'env',
        'name': 'name',
        'repository_authentication': 'repositoryAuthentication',
        'repository_password': 'repositoryPassword',
        'repository_reference_name': 'repositoryReferenceName',
        'repository_url': 'repositoryURL',
        'repository_username': 'repositoryUsername',
        'swarm_id': 'swarmID'
    }

    def __init__(self, compose_file_path_in_repository='docker-compose.yml', env=None, name=None, repository_authentication=None, repository_password=None, repository_reference_name=None, repository_url=None, repository_username=None, swarm_id=None, _configuration=None):  # noqa: E501
        """StacksSwarmStackFromGitRepositoryPayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compose_file_path_in_repository = None
        self._env = None
        self._name = None
        self._repository_authentication = None
        self._repository_password = None
        self._repository_reference_name = None
        self._repository_url = None
        self._repository_username = None
        self._swarm_id = None
        self.discriminator = None

        if compose_file_path_in_repository is not None:
            self.compose_file_path_in_repository = compose_file_path_in_repository
        if env is not None:
            self.env = env
        self.name = name
        if repository_authentication is not None:
            self.repository_authentication = repository_authentication
        if repository_password is not None:
            self.repository_password = repository_password
        if repository_reference_name is not None:
            self.repository_reference_name = repository_reference_name
        self.repository_url = repository_url
        if repository_username is not None:
            self.repository_username = repository_username
        self.swarm_id = swarm_id

    @property
    def compose_file_path_in_repository(self):
        """Gets the compose_file_path_in_repository of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501

        Path to the Stack file inside the Git repository  # noqa: E501

        :return: The compose_file_path_in_repository of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :rtype: str
        """
        return self._compose_file_path_in_repository

    @compose_file_path_in_repository.setter
    def compose_file_path_in_repository(self, compose_file_path_in_repository):
        """Sets the compose_file_path_in_repository of this StacksSwarmStackFromGitRepositoryPayload.

        Path to the Stack file inside the Git repository  # noqa: E501

        :param compose_file_path_in_repository: The compose_file_path_in_repository of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :type: str
        """

        self._compose_file_path_in_repository = compose_file_path_in_repository

    @property
    def env(self):
        """Gets the env of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501

        A list of environment variables used during stack deployment  # noqa: E501

        :return: The env of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :rtype: list[PortainerPair]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this StacksSwarmStackFromGitRepositoryPayload.

        A list of environment variables used during stack deployment  # noqa: E501

        :param env: The env of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :type: list[PortainerPair]
        """

        self._env = env

    @property
    def name(self):
        """Gets the name of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501

        Name of the stack  # noqa: E501

        :return: The name of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StacksSwarmStackFromGitRepositoryPayload.

        Name of the stack  # noqa: E501

        :param name: The name of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def repository_authentication(self):
        """Gets the repository_authentication of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501

        Use basic authentication to clone the Git repository  # noqa: E501

        :return: The repository_authentication of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :rtype: bool
        """
        return self._repository_authentication

    @repository_authentication.setter
    def repository_authentication(self, repository_authentication):
        """Sets the repository_authentication of this StacksSwarmStackFromGitRepositoryPayload.

        Use basic authentication to clone the Git repository  # noqa: E501

        :param repository_authentication: The repository_authentication of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :type: bool
        """

        self._repository_authentication = repository_authentication

    @property
    def repository_password(self):
        """Gets the repository_password of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501

        Password used in basic authentication. Required when RepositoryAuthentication is true.  # noqa: E501

        :return: The repository_password of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :rtype: str
        """
        return self._repository_password

    @repository_password.setter
    def repository_password(self, repository_password):
        """Sets the repository_password of this StacksSwarmStackFromGitRepositoryPayload.

        Password used in basic authentication. Required when RepositoryAuthentication is true.  # noqa: E501

        :param repository_password: The repository_password of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :type: str
        """

        self._repository_password = repository_password

    @property
    def repository_reference_name(self):
        """Gets the repository_reference_name of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501

        Reference name of a Git repository hosting the Stack file  # noqa: E501

        :return: The repository_reference_name of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :rtype: str
        """
        return self._repository_reference_name

    @repository_reference_name.setter
    def repository_reference_name(self, repository_reference_name):
        """Sets the repository_reference_name of this StacksSwarmStackFromGitRepositoryPayload.

        Reference name of a Git repository hosting the Stack file  # noqa: E501

        :param repository_reference_name: The repository_reference_name of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :type: str
        """

        self._repository_reference_name = repository_reference_name

    @property
    def repository_url(self):
        """Gets the repository_url of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501

        URL of a Git repository hosting the Stack file  # noqa: E501

        :return: The repository_url of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """Sets the repository_url of this StacksSwarmStackFromGitRepositoryPayload.

        URL of a Git repository hosting the Stack file  # noqa: E501

        :param repository_url: The repository_url of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and repository_url is None:
            raise ValueError("Invalid value for `repository_url`, must not be `None`")  # noqa: E501

        self._repository_url = repository_url

    @property
    def repository_username(self):
        """Gets the repository_username of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501

        Username used in basic authentication. Required when RepositoryAuthentication is true.  # noqa: E501

        :return: The repository_username of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :rtype: str
        """
        return self._repository_username

    @repository_username.setter
    def repository_username(self, repository_username):
        """Sets the repository_username of this StacksSwarmStackFromGitRepositoryPayload.

        Username used in basic authentication. Required when RepositoryAuthentication is true.  # noqa: E501

        :param repository_username: The repository_username of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :type: str
        """

        self._repository_username = repository_username

    @property
    def swarm_id(self):
        """Gets the swarm_id of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501

        Swarm cluster identifier  # noqa: E501

        :return: The swarm_id of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :rtype: str
        """
        return self._swarm_id

    @swarm_id.setter
    def swarm_id(self, swarm_id):
        """Sets the swarm_id of this StacksSwarmStackFromGitRepositoryPayload.

        Swarm cluster identifier  # noqa: E501

        :param swarm_id: The swarm_id of this StacksSwarmStackFromGitRepositoryPayload.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and swarm_id is None:
            raise ValueError("Invalid value for `swarm_id`, must not be `None`")  # noqa: E501

        self._swarm_id = swarm_id

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
        if issubclass(StacksSwarmStackFromGitRepositoryPayload, dict):
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
        if not isinstance(other, StacksSwarmStackFromGitRepositoryPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StacksSwarmStackFromGitRepositoryPayload):
            return True

        return self.to_dict() != other.to_dict()
