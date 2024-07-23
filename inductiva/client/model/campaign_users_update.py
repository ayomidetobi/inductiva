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


class CampaignUsersUpdate(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "emails",
            "campaign_id",
        }

        class properties:
            campaign_id = schemas.StrSchema

            class emails(schemas.ListSchema):

                class MetaOapg:
                    items = schemas.StrSchema

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[
                        MetaOapg.items,
                        str,
                    ]], typing.List[typing.Union[
                        MetaOapg.items,
                        str,
                    ]]],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'emails':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            __annotations__ = {
                "campaign_id": campaign_id,
                "emails": emails,
            }

    emails: MetaOapg.properties.emails
    campaign_id: MetaOapg.properties.campaign_id

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["campaign_id"]
    ) -> MetaOapg.properties.campaign_id:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["emails"]
    ) -> MetaOapg.properties.emails:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal[
        "campaign_id",
        "emails",
    ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["campaign_id"]
    ) -> MetaOapg.properties.campaign_id:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["emails"]
    ) -> MetaOapg.properties.emails:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal[
        "campaign_id",
        "emails",
    ], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        emails: typing.Union[
            MetaOapg.properties.emails,
            list,
            tuple,
        ],
        campaign_id: typing.Union[
            MetaOapg.properties.campaign_id,
            str,
        ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'CampaignUsersUpdate':
        return super().__new__(
            cls,
            *_args,
            emails=emails,
            campaign_id=campaign_id,
            _configuration=_configuration,
            **kwargs,
        )
