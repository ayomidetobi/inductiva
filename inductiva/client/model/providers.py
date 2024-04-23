# coding: utf-8
"""
    InductivaWebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from inductiva.client import schemas  # noqa: F401


class Providers(schemas.EnumBase, schemas.StrSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enumeration.
    """

    class MetaOapg:
        enum_value_to_name = {
            "GCP": "GCP",
            "ICE": "ICE",
            "LOCAL": "LOCAL",
        }

    @schemas.classproperty
    def GCP(cls):
        return cls("GCP")

    @schemas.classproperty
    def ICE(cls):
        return cls("ICE")

    @schemas.classproperty
    def LOCAL(cls):
        return cls("LOCAL")
