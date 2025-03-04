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


class UserCreate(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "email",
        }

        class properties:
            email = schemas.StrSchema

            class expiry_ts(
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
                ) -> 'expiry_ts':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class name(
                    schemas.ComposedSchema,):

                class MetaOapg:
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
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class extra_metadata(
                    schemas.ComposedSchema,):

                class MetaOapg:
                    additional_properties = schemas.StrSchema
                    any_of_0 = schemas.DictSchema
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

                def __getitem__(
                        self, name: typing.Union[
                            str,
                        ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)

                def get_item_oapg(
                        self, name: typing.Union[
                            str,
                        ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)

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
                    **kwargs: typing.Union[
                        MetaOapg.additional_properties,
                        str,
                    ],
                ) -> 'extra_metadata':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            __annotations__ = {
                "email": email,
                "expiry_ts": expiry_ts,
                "name": name,
                "extra_metadata": extra_metadata,
            }

    email: MetaOapg.properties.email

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["email"]
    ) -> MetaOapg.properties.email:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["expiry_ts"]
    ) -> MetaOapg.properties.expiry_ts:
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["extra_metadata"]
    ) -> MetaOapg.properties.extra_metadata:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal[
        "email",
        "expiry_ts",
        "name",
        "extra_metadata",
    ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
            self, name: typing_extensions.Literal["email"]
    ) -> MetaOapg.properties.email:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["expiry_ts"]
    ) -> typing.Union[MetaOapg.properties.expiry_ts, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> typing.Union[MetaOapg.properties.name, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["extra_metadata"]
    ) -> typing.Union[MetaOapg.properties.extra_metadata, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal[
        "email",
        "expiry_ts",
        "name",
        "extra_metadata",
    ], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        email: typing.Union[
            MetaOapg.properties.email,
            str,
        ],
        expiry_ts: typing.Union[MetaOapg.properties.expiry_ts, dict,
                                frozendict.frozendict, str, date, datetime,
                                uuid.UUID, int, float, decimal.Decimal, bool,
                                None, list, tuple, bytes, io.FileIO,
                                io.BufferedReader,
                                schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, dict,
                           frozendict.frozendict, str, date, datetime,
                           uuid.UUID, int, float, decimal.Decimal, bool, None,
                           list, tuple, bytes, io.FileIO, io.BufferedReader,
                           schemas.Unset] = schemas.unset,
        extra_metadata: typing.Union[MetaOapg.properties.extra_metadata, dict,
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
    ) -> 'UserCreate':
        return super().__new__(
            cls,
            *_args,
            email=email,
            expiry_ts=expiry_ts,
            name=name,
            extra_metadata=extra_metadata,
            _configuration=_configuration,
            **kwargs,
        )
