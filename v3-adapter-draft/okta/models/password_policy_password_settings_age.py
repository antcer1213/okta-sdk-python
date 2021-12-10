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

class PasswordPolicyPasswordSettingsAge(object):
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
        'expire_warn_days': 'int',
        'history_count': 'int',
        'max_age_days': 'int',
        'min_age_minutes': 'int'
    }

    attribute_map = {
        'expire_warn_days': 'expireWarnDays',
        'history_count': 'historyCount',
        'max_age_days': 'maxAgeDays',
        'min_age_minutes': 'minAgeMinutes'
    }

    def __init__(self, expire_warn_days=None, history_count=None, max_age_days=None, min_age_minutes=None):  # noqa: E501
        """PasswordPolicyPasswordSettingsAge - a model defined in Swagger"""  # noqa: E501
        self._expire_warn_days = None
        self._history_count = None
        self._max_age_days = None
        self._min_age_minutes = None
        self.discriminator = None
        if expire_warn_days is not None:
            self.expire_warn_days = expire_warn_days
        if history_count is not None:
            self.history_count = history_count
        if max_age_days is not None:
            self.max_age_days = max_age_days
        if min_age_minutes is not None:
            self.min_age_minutes = min_age_minutes

    @property
    def expire_warn_days(self):
        """Gets the expire_warn_days of this PasswordPolicyPasswordSettingsAge.  # noqa: E501


        :return: The expire_warn_days of this PasswordPolicyPasswordSettingsAge.  # noqa: E501
        :rtype: int
        """
        return self._expire_warn_days

    @expire_warn_days.setter
    def expire_warn_days(self, expire_warn_days):
        """Sets the expire_warn_days of this PasswordPolicyPasswordSettingsAge.


        :param expire_warn_days: The expire_warn_days of this PasswordPolicyPasswordSettingsAge.  # noqa: E501
        :type: int
        """

        self._expire_warn_days = expire_warn_days

    @property
    def history_count(self):
        """Gets the history_count of this PasswordPolicyPasswordSettingsAge.  # noqa: E501


        :return: The history_count of this PasswordPolicyPasswordSettingsAge.  # noqa: E501
        :rtype: int
        """
        return self._history_count

    @history_count.setter
    def history_count(self, history_count):
        """Sets the history_count of this PasswordPolicyPasswordSettingsAge.


        :param history_count: The history_count of this PasswordPolicyPasswordSettingsAge.  # noqa: E501
        :type: int
        """

        self._history_count = history_count

    @property
    def max_age_days(self):
        """Gets the max_age_days of this PasswordPolicyPasswordSettingsAge.  # noqa: E501


        :return: The max_age_days of this PasswordPolicyPasswordSettingsAge.  # noqa: E501
        :rtype: int
        """
        return self._max_age_days

    @max_age_days.setter
    def max_age_days(self, max_age_days):
        """Sets the max_age_days of this PasswordPolicyPasswordSettingsAge.


        :param max_age_days: The max_age_days of this PasswordPolicyPasswordSettingsAge.  # noqa: E501
        :type: int
        """

        self._max_age_days = max_age_days

    @property
    def min_age_minutes(self):
        """Gets the min_age_minutes of this PasswordPolicyPasswordSettingsAge.  # noqa: E501


        :return: The min_age_minutes of this PasswordPolicyPasswordSettingsAge.  # noqa: E501
        :rtype: int
        """
        return self._min_age_minutes

    @min_age_minutes.setter
    def min_age_minutes(self, min_age_minutes):
        """Sets the min_age_minutes of this PasswordPolicyPasswordSettingsAge.


        :param min_age_minutes: The min_age_minutes of this PasswordPolicyPasswordSettingsAge.  # noqa: E501
        :type: int
        """

        self._min_age_minutes = min_age_minutes

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
        if issubclass(PasswordPolicyPasswordSettingsAge, dict):
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
        if not isinstance(other, PasswordPolicyPasswordSettingsAge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other