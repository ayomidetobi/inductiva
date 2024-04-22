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


class ExecuterTrackerAPIConnectionInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Information sent to the executer tracker after registration.
    """


    class MetaOapg:
        required = {
            "redis_consumer_group",
            "redis_stream",
            "redis_consumer_name",
            "uuid",
        }
        
        class properties:
            uuid = schemas.StrSchema
            redis_stream = schemas.StrSchema
            redis_consumer_name = schemas.StrSchema
            redis_consumer_group = schemas.StrSchema
            __annotations__ = {
                "uuid": uuid,
                "redis_stream": redis_stream,
                "redis_consumer_name": redis_consumer_name,
                "redis_consumer_group": redis_consumer_group,
            }
    
    redis_consumer_group: MetaOapg.properties.redis_consumer_group
    redis_stream: MetaOapg.properties.redis_stream
    redis_consumer_name: MetaOapg.properties.redis_consumer_name
    uuid: MetaOapg.properties.uuid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redis_stream"]) -> MetaOapg.properties.redis_stream: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redis_consumer_name"]) -> MetaOapg.properties.redis_consumer_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redis_consumer_group"]) -> MetaOapg.properties.redis_consumer_group: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", "redis_stream", "redis_consumer_name", "redis_consumer_group", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redis_stream"]) -> MetaOapg.properties.redis_stream: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redis_consumer_name"]) -> MetaOapg.properties.redis_consumer_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redis_consumer_group"]) -> MetaOapg.properties.redis_consumer_group: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", "redis_stream", "redis_consumer_name", "redis_consumer_group", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        redis_consumer_group: typing.Union[MetaOapg.properties.redis_consumer_group, str, ],
        redis_stream: typing.Union[MetaOapg.properties.redis_stream, str, ],
        redis_consumer_name: typing.Union[MetaOapg.properties.redis_consumer_name, str, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExecuterTrackerAPIConnectionInfo':
        return super().__new__(
            cls,
            *_args,
            redis_consumer_group=redis_consumer_group,
            redis_stream=redis_stream,
            redis_consumer_name=redis_consumer_name,
            uuid=uuid,
            _configuration=_configuration,
            **kwargs,
        )
