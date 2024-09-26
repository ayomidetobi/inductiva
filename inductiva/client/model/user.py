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


class User(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "terms_and_conditions_decision",
            "tier",
            "total_available_credits",
            "organization",
            "registration_ts",
            "email",
            "username",
        }

        class properties:
            email = schemas.StrSchema
            username = schemas.StrSchema
            organization = schemas.StrSchema
            tier = schemas.StrSchema
            total_available_credits = schemas.NumberSchema

            @staticmethod
            def terms_and_conditions_decision(
            ) -> typing.Type['TermsAndConditions']:
                return TermsAndConditions

            registration_ts = schemas.DateTimeSchema

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

            credits_currency = schemas.StrSchema

            class terms_and_conditions_decision_ts(
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
                ) -> 'terms_and_conditions_decision_ts':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            __annotations__ = {
                "email":
                    email,
                "username":
                    username,
                "organization":
                    organization,
                "tier":
                    tier,
                "total_available_credits":
                    total_available_credits,
                "terms_and_conditions_decision":
                    terms_and_conditions_decision,
                "registration_ts":
                    registration_ts,
                "name":
                    name,
                "credits_currency":
                    credits_currency,
                "terms_and_conditions_decision_ts":
                    terms_and_conditions_decision_ts,
            }

    terms_and_conditions_decision: 'TermsAndConditions'
    tier: MetaOapg.properties.tier
    total_available_credits: MetaOapg.properties.total_available_credits
    organization: MetaOapg.properties.organization
    registration_ts: MetaOapg.properties.registration_ts
    email: MetaOapg.properties.email
    username: MetaOapg.properties.username

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["email"]
    ) -> MetaOapg.properties.email:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["username"]
    ) -> MetaOapg.properties.username:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["organization"]
    ) -> MetaOapg.properties.organization:
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["tier"]
    ) -> MetaOapg.properties.tier:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["total_available_credits"]
    ) -> MetaOapg.properties.total_available_credits:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["terms_and_conditions_decision"]
    ) -> 'TermsAndConditions':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["registration_ts"]
    ) -> MetaOapg.properties.registration_ts:
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["credits_currency"]
    ) -> MetaOapg.properties.credits_currency:
        ...

    @typing.overload
    def __getitem__(
        self,
        name: typing_extensions.Literal["terms_and_conditions_decision_ts"]
    ) -> MetaOapg.properties.terms_and_conditions_decision_ts:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal[
        "email",
        "username",
        "organization",
        "tier",
        "total_available_credits",
        "terms_and_conditions_decision",
        "registration_ts",
        "name",
        "credits_currency",
        "terms_and_conditions_decision_ts",
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
        self, name: typing_extensions.Literal["username"]
    ) -> MetaOapg.properties.username:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["organization"]
    ) -> MetaOapg.properties.organization:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: typing_extensions.Literal["tier"]
    ) -> MetaOapg.properties.tier:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["total_available_credits"]
    ) -> MetaOapg.properties.total_available_credits:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["terms_and_conditions_decision"]
    ) -> 'TermsAndConditions':
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["registration_ts"]
    ) -> MetaOapg.properties.registration_ts:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> typing.Union[MetaOapg.properties.name, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["credits_currency"]
    ) -> typing.Union[MetaOapg.properties.credits_currency, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self,
        name: typing_extensions.Literal["terms_and_conditions_decision_ts"]
    ) -> typing.Union[MetaOapg.properties.terms_and_conditions_decision_ts,
                      schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal[
        "email",
        "username",
        "organization",
        "tier",
        "total_available_credits",
        "terms_and_conditions_decision",
        "registration_ts",
        "name",
        "credits_currency",
        "terms_and_conditions_decision_ts",
    ], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        terms_and_conditions_decision: 'TermsAndConditions',
        tier: typing.Union[
            MetaOapg.properties.tier,
            str,
        ],
        total_available_credits: typing.Union[
            MetaOapg.properties.total_available_credits,
            decimal.Decimal,
            int,
            float,
        ],
        organization: typing.Union[
            MetaOapg.properties.organization,
            str,
        ],
        registration_ts: typing.Union[
            MetaOapg.properties.registration_ts,
            str,
            datetime,
        ],
        email: typing.Union[
            MetaOapg.properties.email,
            str,
        ],
        username: typing.Union[
            MetaOapg.properties.username,
            str,
        ],
        name: typing.Union[MetaOapg.properties.name, dict,
                           frozendict.frozendict, str, date, datetime,
                           uuid.UUID, int, float, decimal.Decimal, bool, None,
                           list, tuple, bytes, io.FileIO, io.BufferedReader,
                           schemas.Unset] = schemas.unset,
        credits_currency: typing.Union[MetaOapg.properties.credits_currency,
                                       str, schemas.Unset] = schemas.unset,
        terms_and_conditions_decision_ts: typing.Union[
            MetaOapg.properties.terms_and_conditions_decision_ts, dict,
            frozendict.frozendict, str, date, datetime, uuid.UUID, int, float,
            decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO,
            io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'User':
        return super().__new__(
            cls,
            *_args,
            terms_and_conditions_decision=terms_and_conditions_decision,
            tier=tier,
            total_available_credits=total_available_credits,
            organization=organization,
            registration_ts=registration_ts,
            email=email,
            username=username,
            name=name,
            credits_currency=credits_currency,
            terms_and_conditions_decision_ts=terms_and_conditions_decision_ts,
            _configuration=_configuration,
            **kwargs,
        )


from inductiva.client.model.terms_and_conditions import TermsAndConditions
