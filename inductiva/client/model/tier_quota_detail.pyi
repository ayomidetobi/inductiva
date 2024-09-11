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


class TierQuotaDetail(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Mixin to handle decimal.Decimal("Infinity") values. This is useful
when we want to represent infinity in a JSON response. Pydantic does
not support this out of the box. This mixin allows us to use
decimal.Decimal("Infinity") in our models, and it will be serialized to
"infinity" in the JSON response.
    """


    class MetaOapg:
        required = {
            "unit",
            "scope",
            "id",
            "label",
            "value",
        }
        
        class properties:
            id = schemas.StrSchema
            value = schemas.NumberSchema
            label = schemas.StrSchema
            unit = schemas.StrSchema
            scope = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "value": value,
                "label": label,
                "unit": unit,
                "scope": scope,
            }
    
    unit: MetaOapg.properties.unit
    scope: MetaOapg.properties.scope
    id: MetaOapg.properties.id
    label: MetaOapg.properties.label
    value: MetaOapg.properties.value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "value", "label", "unit", "scope", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "value", "label", "unit", "scope", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        unit: typing.Union[MetaOapg.properties.unit, str, ],
        scope: typing.Union[MetaOapg.properties.scope, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        label: typing.Union[MetaOapg.properties.label, str, ],
        value: typing.Union[MetaOapg.properties.value, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TierQuotaDetail':
        return super().__new__(
            cls,
            *_args,
            unit=unit,
            scope=scope,
            id=id,
            label=label,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )
