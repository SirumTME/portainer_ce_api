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


class PortainerTLSConfiguration(object):
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
        'tls': 'bool',
        'tlsca_cert': 'str',
        'tls_cert': 'str',
        'tls_key': 'str',
        'tls_skip_verify': 'bool'
    }

    attribute_map = {
        'tls': 'TLS',
        'tlsca_cert': 'TLSCACert',
        'tls_cert': 'TLSCert',
        'tls_key': 'TLSKey',
        'tls_skip_verify': 'TLSSkipVerify'
    }

    def __init__(self, tls=None, tlsca_cert=None, tls_cert=None, tls_key=None, tls_skip_verify=None, _configuration=None):  # noqa: E501
        """PortainerTLSConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._tls = None
        self._tlsca_cert = None
        self._tls_cert = None
        self._tls_key = None
        self._tls_skip_verify = None
        self.discriminator = None

        if tls is not None:
            self.tls = tls
        if tlsca_cert is not None:
            self.tlsca_cert = tlsca_cert
        if tls_cert is not None:
            self.tls_cert = tls_cert
        if tls_key is not None:
            self.tls_key = tls_key
        if tls_skip_verify is not None:
            self.tls_skip_verify = tls_skip_verify

    @property
    def tls(self):
        """Gets the tls of this PortainerTLSConfiguration.  # noqa: E501

        Use TLS  # noqa: E501

        :return: The tls of this PortainerTLSConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this PortainerTLSConfiguration.

        Use TLS  # noqa: E501

        :param tls: The tls of this PortainerTLSConfiguration.  # noqa: E501
        :type: bool
        """

        self._tls = tls

    @property
    def tlsca_cert(self):
        """Gets the tlsca_cert of this PortainerTLSConfiguration.  # noqa: E501

        Path to the TLS CA certificate file  # noqa: E501

        :return: The tlsca_cert of this PortainerTLSConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._tlsca_cert

    @tlsca_cert.setter
    def tlsca_cert(self, tlsca_cert):
        """Sets the tlsca_cert of this PortainerTLSConfiguration.

        Path to the TLS CA certificate file  # noqa: E501

        :param tlsca_cert: The tlsca_cert of this PortainerTLSConfiguration.  # noqa: E501
        :type: str
        """

        self._tlsca_cert = tlsca_cert

    @property
    def tls_cert(self):
        """Gets the tls_cert of this PortainerTLSConfiguration.  # noqa: E501

        Path to the TLS client certificate file  # noqa: E501

        :return: The tls_cert of this PortainerTLSConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._tls_cert

    @tls_cert.setter
    def tls_cert(self, tls_cert):
        """Sets the tls_cert of this PortainerTLSConfiguration.

        Path to the TLS client certificate file  # noqa: E501

        :param tls_cert: The tls_cert of this PortainerTLSConfiguration.  # noqa: E501
        :type: str
        """

        self._tls_cert = tls_cert

    @property
    def tls_key(self):
        """Gets the tls_key of this PortainerTLSConfiguration.  # noqa: E501

        Path to the TLS client key file  # noqa: E501

        :return: The tls_key of this PortainerTLSConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._tls_key

    @tls_key.setter
    def tls_key(self, tls_key):
        """Sets the tls_key of this PortainerTLSConfiguration.

        Path to the TLS client key file  # noqa: E501

        :param tls_key: The tls_key of this PortainerTLSConfiguration.  # noqa: E501
        :type: str
        """

        self._tls_key = tls_key

    @property
    def tls_skip_verify(self):
        """Gets the tls_skip_verify of this PortainerTLSConfiguration.  # noqa: E501

        Skip the verification of the server TLS certificate  # noqa: E501

        :return: The tls_skip_verify of this PortainerTLSConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._tls_skip_verify

    @tls_skip_verify.setter
    def tls_skip_verify(self, tls_skip_verify):
        """Sets the tls_skip_verify of this PortainerTLSConfiguration.

        Skip the verification of the server TLS certificate  # noqa: E501

        :param tls_skip_verify: The tls_skip_verify of this PortainerTLSConfiguration.  # noqa: E501
        :type: bool
        """

        self._tls_skip_verify = tls_skip_verify

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
        if issubclass(PortainerTLSConfiguration, dict):
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
        if not isinstance(other, PortainerTLSConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortainerTLSConfiguration):
            return True

        return self.to_dict() != other.to_dict()