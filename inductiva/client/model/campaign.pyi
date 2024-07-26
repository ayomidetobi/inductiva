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


class Campaign(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "end_date",
            "credits",
            "begin_date",
            "id",
            "label",
        }
        
        class properties:
            id = schemas.StrSchema
            label = schemas.StrSchema
            credits = schemas.NumberSchema
            begin_date = schemas.DateTimeSchema
            end_date = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "label": label,
                "credits": credits,
                "begin_date": begin_date,
                "end_date": end_date,
            }
    
    end_date: MetaOapg.properties.end_date
    credits: MetaOapg.properties.credits
    begin_date: MetaOapg.properties.begin_date
    id: MetaOapg.properties.id
    label: MetaOapg.properties.label
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credits"]) -> MetaOapg.properties.credits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["begin_date"]) -> MetaOapg.properties.begin_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "label", "credits", "begin_date", "end_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credits"]) -> MetaOapg.properties.credits: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["begin_date"]) -> MetaOapg.properties.begin_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "label", "credits", "begin_date", "end_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        end_date: typing.Union[MetaOapg.properties.end_date, str, datetime, ],
        credits: typing.Union[MetaOapg.properties.credits, decimal.Decimal, int, float, ],
        begin_date: typing.Union[MetaOapg.properties.begin_date, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        label: typing.Union[MetaOapg.properties.label, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Campaign':
        return super().__new__(
            cls,
            *_args,
            end_date=end_date,
            credits=credits,
            begin_date=begin_date,
            id=id,
            label=label,
            _configuration=_configuration,
            **kwargs,
        )
