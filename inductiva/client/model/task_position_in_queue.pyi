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


class TaskPositionInQueue(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "tasks_ahead",
            "total_tasks",
            "tasks_behind",
            "position",
        }
        
        class properties:
            total_tasks = schemas.IntSchema
            tasks_ahead = schemas.IntSchema
            tasks_behind = schemas.IntSchema
            position = schemas.IntSchema
            __annotations__ = {
                "total_tasks": total_tasks,
                "tasks_ahead": tasks_ahead,
                "tasks_behind": tasks_behind,
                "position": position,
            }
    
    tasks_ahead: MetaOapg.properties.tasks_ahead
    total_tasks: MetaOapg.properties.total_tasks
    tasks_behind: MetaOapg.properties.tasks_behind
    position: MetaOapg.properties.position
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_tasks"]) -> MetaOapg.properties.total_tasks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tasks_ahead"]) -> MetaOapg.properties.tasks_ahead: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tasks_behind"]) -> MetaOapg.properties.tasks_behind: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_tasks", "tasks_ahead", "tasks_behind", "position", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_tasks"]) -> MetaOapg.properties.total_tasks: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tasks_ahead"]) -> MetaOapg.properties.tasks_ahead: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tasks_behind"]) -> MetaOapg.properties.tasks_behind: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_tasks", "tasks_ahead", "tasks_behind", "position", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tasks_ahead: typing.Union[MetaOapg.properties.tasks_ahead, decimal.Decimal, int, ],
        total_tasks: typing.Union[MetaOapg.properties.total_tasks, decimal.Decimal, int, ],
        tasks_behind: typing.Union[MetaOapg.properties.tasks_behind, decimal.Decimal, int, ],
        position: typing.Union[MetaOapg.properties.position, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskPositionInQueue':
        return super().__new__(
            cls,
            *_args,
            tasks_ahead=tasks_ahead,
            total_tasks=total_tasks,
            tasks_behind=tasks_behind,
            position=position,
            _configuration=_configuration,
            **kwargs,
        )
