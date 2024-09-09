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


class MachineGroupStatus(schemas.EnumBase, schemas.StrSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enumeration.
    """

    class MetaOapg:
        enum_value_to_name = {
            "registered": "REGISTERED",
            "starting": "STARTING",
            "started": "STARTED",
            "shutting_down": "SHUTTING_DOWN",
            "shutdown_failed": "SHUTDOWN_FAILED",
            "terminated": "TERMINATED",
        }

    @schemas.classproperty
    def REGISTERED(cls):
        return cls("registered")

    @schemas.classproperty
    def STARTING(cls):
        return cls("starting")

    @schemas.classproperty
    def STARTED(cls):
        return cls("started")

    @schemas.classproperty
    def SHUTTING_DOWN(cls):
        return cls("shutting_down")

    @schemas.classproperty
    def SHUTDOWN_FAILED(cls):
        return cls("shutdown_failed")

    @schemas.classproperty
    def TERMINATED(cls):
        return cls("terminated")
