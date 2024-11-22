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


class TaskOperation(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "start_timestamp",
            "name",
            "alias",
            "attributes",
            "status",
        }

        class properties:

            @staticmethod
            def name() -> typing.Type['TaskOperationName']:
                return TaskOperationName

            alias = schemas.StrSchema
            start_timestamp = schemas.DateTimeSchema

            @staticmethod
            def status() -> typing.Type['OperationStatus']:
                return OperationStatus

            attributes = schemas.DictSchema

            class end_timestamp(
                    schemas.DateTimeBase,
                    schemas.ComposedSchema,
            ):

                class MetaOapg:
                    format = 'date-time'
                    any_of_0 = schemas.StrSchema
                    any_of_1 = schemas.NoneSchema

                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]

                def __new__(
                    cls,
                    *_args: typing.Union[
                        dict,
                        frozendict.frozendict,
                        str,
                        date,
                        datetime,
                        uuid.UUID,
                        int,
                        float,
                        decimal.Decimal,
                        bool,
                        None,
                        list,
                        tuple,
                        bytes,
                        io.FileIO,
                        io.BufferedReader,
                    ],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                                           frozendict.frozendict, str, date,
                                           datetime, uuid.UUID, int, float,
                                           decimal.Decimal, None, list, tuple,
                                           bytes],
                ) -> 'end_timestamp':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            __annotations__ = {
                "name": name,
                "alias": alias,
                "start_timestamp": start_timestamp,
                "status": status,
                "attributes": attributes,
                "end_timestamp": end_timestamp,
            }

    start_timestamp: MetaOapg.properties.start_timestamp
    name: 'TaskOperationName'
    alias: MetaOapg.properties.alias
    attributes: MetaOapg.properties.attributes
    status: 'OperationStatus'

    @typing.overload
    def __getitem__(
            self,
            name: typing_extensions.Literal["name"]) -> 'TaskOperationName':
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["alias"]
    ) -> MetaOapg.properties.alias:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["start_timestamp"]
    ) -> MetaOapg.properties.start_timestamp:
        ...

    @typing.overload
    def __getitem__(
            self,
            name: typing_extensions.Literal["status"]) -> 'OperationStatus':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["attributes"]
    ) -> MetaOapg.properties.attributes:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["end_timestamp"]
    ) -> MetaOapg.properties.end_timestamp:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal[
        "name",
        "alias",
        "start_timestamp",
        "status",
        "attributes",
        "end_timestamp",
    ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
            self,
            name: typing_extensions.Literal["name"]) -> 'TaskOperationName':
        ...

    @typing.overload
    def get_item_oapg(
            self, name: typing_extensions.Literal["alias"]
    ) -> MetaOapg.properties.alias:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["start_timestamp"]
    ) -> MetaOapg.properties.start_timestamp:
        ...

    @typing.overload
    def get_item_oapg(
            self,
            name: typing_extensions.Literal["status"]) -> 'OperationStatus':
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["attributes"]
    ) -> MetaOapg.properties.attributes:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["end_timestamp"]
    ) -> typing.Union[MetaOapg.properties.end_timestamp, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal[
        "name",
        "alias",
        "start_timestamp",
        "status",
        "attributes",
        "end_timestamp",
    ], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        start_timestamp: typing.Union[
            MetaOapg.properties.start_timestamp,
            str,
            datetime,
        ],
        name: 'TaskOperationName',
        alias: typing.Union[
            MetaOapg.properties.alias,
            str,
        ],
        attributes: typing.Union[
            MetaOapg.properties.attributes,
            dict,
            frozendict.frozendict,
        ],
        status: 'OperationStatus',
        end_timestamp: typing.Union[MetaOapg.properties.end_timestamp, dict,
                                    frozendict.frozendict, str, date, datetime,
                                    uuid.UUID, int, float, decimal.Decimal,
                                    bool, None, list, tuple, bytes, io.FileIO,
                                    io.BufferedReader,
                                    schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'TaskOperation':
        return super().__new__(
            cls,
            *_args,
            start_timestamp=start_timestamp,
            name=name,
            alias=alias,
            attributes=attributes,
            status=status,
            end_timestamp=end_timestamp,
            _configuration=_configuration,
            **kwargs,
        )


from inductiva.client.model.operation_status import OperationStatus
from inductiva.client.model.task_operation_name import TaskOperationName
