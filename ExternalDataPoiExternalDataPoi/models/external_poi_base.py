# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ExternalPoiBase(object):
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
        '_date': 'str',
        'detail_vv': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'detail_vv': 'detail_vv'
    }

    def __init__(self, _date=None, detail_vv=None):  # noqa: E501
        """ExternalPoiBase - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._detail_vv = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if detail_vv is not None:
            self.detail_vv = detail_vv

    @property
    def _date(self):
        """Gets the _date of this ExternalPoiBase.  # noqa: E501

        日期  # noqa: E501

        :return: The _date of this ExternalPoiBase.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ExternalPoiBase.

        日期  # noqa: E501

        :param _date: The _date of this ExternalPoiBase.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def detail_vv(self):
        """Gets the detail_vv of this ExternalPoiBase.  # noqa: E501

        详情页pv  # noqa: E501

        :return: The detail_vv of this ExternalPoiBase.  # noqa: E501
        :rtype: int
        """
        return self._detail_vv

    @detail_vv.setter
    def detail_vv(self, detail_vv):
        """Sets the detail_vv of this ExternalPoiBase.

        详情页pv  # noqa: E501

        :param detail_vv: The detail_vv of this ExternalPoiBase.  # noqa: E501
        :type: int
        """

        self._detail_vv = detail_vv

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
        if issubclass(ExternalPoiBase, dict):
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
        if not isinstance(other, ExternalPoiBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
