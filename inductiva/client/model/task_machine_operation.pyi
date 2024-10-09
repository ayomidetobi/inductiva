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


class TaskMachineOperation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "start_timestamp",
            "description",
            "machine_id",
            "type",
            "info",
        }
        
        class properties:
            machine_id = schemas.UUIDSchema
        
            @staticmethod
            def type() -> typing.Type['MachineOperationType']:
                return MachineOperationType
            start_timestamp = schemas.DateTimeSchema
            description = schemas.StrSchema
            info = schemas.DictSchema
            
            
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
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'end_timestamp':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "machine_id": machine_id,
                "type": type,
                "start_timestamp": start_timestamp,
                "description": description,
                "info": info,
                "end_timestamp": end_timestamp,
            }
    
    start_timestamp: MetaOapg.properties.start_timestamp
    description: MetaOapg.properties.description
    machine_id: MetaOapg.properties.machine_id
    type: 'MachineOperationType'
    info: MetaOapg.properties.info
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["machine_id"]) -> MetaOapg.properties.machine_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'MachineOperationType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_timestamp"]) -> MetaOapg.properties.start_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["info"]) -> MetaOapg.properties.info: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_timestamp"]) -> MetaOapg.properties.end_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["machine_id", "type", "start_timestamp", "description", "info", "end_timestamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["machine_id"]) -> MetaOapg.properties.machine_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'MachineOperationType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_timestamp"]) -> MetaOapg.properties.start_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["info"]) -> MetaOapg.properties.info: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_timestamp"]) -> typing.Union[MetaOapg.properties.end_timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["machine_id", "type", "start_timestamp", "description", "info", "end_timestamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        start_timestamp: typing.Union[MetaOapg.properties.start_timestamp, str, datetime, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        machine_id: typing.Union[MetaOapg.properties.machine_id, str, uuid.UUID, ],
        type: 'MachineOperationType',
        info: typing.Union[MetaOapg.properties.info, dict, frozendict.frozendict, ],
        end_timestamp: typing.Union[MetaOapg.properties.end_timestamp, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskMachineOperation':
        return super().__new__(
            cls,
            *_args,
            start_timestamp=start_timestamp,
            description=description,
            machine_id=machine_id,
            type=type,
            info=info,
            end_timestamp=end_timestamp,
            _configuration=_configuration,
            **kwargs,
        )

from inductiva.client.model.machine_operation_type import MachineOperationType
