# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ThreatInsightConfiguration(object):
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
        'action': 'str',
        'exclude_zones': 'list[str]',
        'created': 'datetime',
        'last_updated': 'datetime',
        'links': 'dict(str, object)'
    }

    attribute_map = {
        'action': 'action',
        'exclude_zones': 'excludeZones',
        'created': 'created',
        'last_updated': 'lastUpdated',
        'links': '_links'
    }

    def __init__(self, action=None, exclude_zones=None, created=None, last_updated=None, links=None):  # noqa: E501
        """ThreatInsightConfiguration - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._exclude_zones = None
        self._created = None
        self._last_updated = None
        self._links = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if exclude_zones is not None:
            self.exclude_zones = exclude_zones
        if created is not None:
            self.created = created
        if last_updated is not None:
            self.last_updated = last_updated
        if links is not None:
            self.links = links

    @property
    def action(self):
        """Gets the action of this ThreatInsightConfiguration.  # noqa: E501


        :return: The action of this ThreatInsightConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ThreatInsightConfiguration.


        :param action: The action of this ThreatInsightConfiguration.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def exclude_zones(self):
        """Gets the exclude_zones of this ThreatInsightConfiguration.  # noqa: E501


        :return: The exclude_zones of this ThreatInsightConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_zones

    @exclude_zones.setter
    def exclude_zones(self, exclude_zones):
        """Sets the exclude_zones of this ThreatInsightConfiguration.


        :param exclude_zones: The exclude_zones of this ThreatInsightConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._exclude_zones = exclude_zones

    @property
    def created(self):
        """Gets the created of this ThreatInsightConfiguration.  # noqa: E501


        :return: The created of this ThreatInsightConfiguration.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ThreatInsightConfiguration.


        :param created: The created of this ThreatInsightConfiguration.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this ThreatInsightConfiguration.  # noqa: E501


        :return: The last_updated of this ThreatInsightConfiguration.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ThreatInsightConfiguration.


        :param last_updated: The last_updated of this ThreatInsightConfiguration.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def links(self):
        """Gets the links of this ThreatInsightConfiguration.  # noqa: E501


        :return: The links of this ThreatInsightConfiguration.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ThreatInsightConfiguration.


        :param links: The links of this ThreatInsightConfiguration.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

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
        if issubclass(ThreatInsightConfiguration, dict):
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
        if not isinstance(other, ThreatInsightConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
