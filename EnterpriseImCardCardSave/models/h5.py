# coding: utf-8

"""
    创建消息卡片

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class H5(object):
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
        'text': 'str',
        'media_id': 'str',
        'image_url': 'str',
        'link_url': 'str'
    }

    attribute_map = {
        'text': 'text',
        'media_id': 'media_id',
        'image_url': 'image_url',
        'link_url': 'link_url'
    }

    def __init__(self, text=None, media_id=None, image_url=None, link_url=None):  # noqa: E501
        """H5 - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self._media_id = None
        self._image_url = None
        self._link_url = None
        self.discriminator = None
        self.text = text
        if media_id is not None:
            self.media_id = media_id
        if image_url is not None:
            self.image_url = image_url
        self.link_url = link_url

    @property
    def text(self):
        """Gets the text of this H5.  # noqa: E501

        卡片内容  # noqa: E501

        :return: The text of this H5.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this H5.

        卡片内容  # noqa: E501

        :param text: The text of this H5.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def media_id(self):
        """Gets the media_id of this H5.  # noqa: E501

        图片的素材id，需已上传在素材库中，创建/更新时必传，查看接口不下发  # noqa: E501

        :return: The media_id of this H5.  # noqa: E501
        :rtype: str
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this H5.

        图片的素材id，需已上传在素材库中，创建/更新时必传，查看接口不下发  # noqa: E501

        :param media_id: The media_id of this H5.  # noqa: E501
        :type: str
        """

        self._media_id = media_id

    @property
    def image_url(self):
        """Gets the image_url of this H5.  # noqa: E501

        创建成功后，调用查看接口会下发media_id对应的图片url  # noqa: E501

        :return: The image_url of this H5.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this H5.

        创建成功后，调用查看接口会下发media_id对应的图片url  # noqa: E501

        :param image_url: The image_url of this H5.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def link_url(self):
        """Gets the link_url of this H5.  # noqa: E501

        点击后跳转url  # noqa: E501

        :return: The link_url of this H5.  # noqa: E501
        :rtype: str
        """
        return self._link_url

    @link_url.setter
    def link_url(self, link_url):
        """Sets the link_url of this H5.

        点击后跳转url  # noqa: E501

        :param link_url: The link_url of this H5.  # noqa: E501
        :type: str
        """
        if link_url is None:
            raise ValueError("Invalid value for `link_url`, must not be `None`")  # noqa: E501

        self._link_url = link_url

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
        if issubclass(H5, dict):
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
        if not isinstance(other, H5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other