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


class FileDownloadDetails(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "file_path",
            "file_server_available",
            "url",
        }

        class properties:
            url = schemas.StrSchema
            file_server_available = schemas.BoolSchema
            file_path = schemas.StrSchema
            __annotations__ = {
                "url": url,
                "file_server_available": file_server_available,
                "file_path": file_path,
            }

    file_path: MetaOapg.properties.file_path
    file_server_available: MetaOapg.properties.file_server_available
    url: MetaOapg.properties.url

    @typing.overload
    def __getitem__(
            self,
            name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["file_server_available"]
    ) -> MetaOapg.properties.file_server_available:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["file_path"]
    ) -> MetaOapg.properties.file_path:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal[
        "url",
        "file_server_available",
        "file_path",
    ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
            self,
            name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["file_server_available"]
    ) -> MetaOapg.properties.file_server_available:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["file_path"]
    ) -> MetaOapg.properties.file_path:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal[
        "url",
        "file_server_available",
        "file_path",
    ], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        file_path: typing.Union[
            MetaOapg.properties.file_path,
            str,
        ],
        file_server_available: typing.Union[
            MetaOapg.properties.file_server_available,
            bool,
        ],
        url: typing.Union[
            MetaOapg.properties.url,
            str,
        ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'FileDownloadDetails':
        return super().__new__(
            cls,
            *_args,
            file_path=file_path,
            file_server_available=file_server_available,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )
