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


class MachineTypeResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "machine_type",
            "num_cpus",
            "price",
            "spot",
            "ram_gb",
        }
        
        class properties:
            machine_type = schemas.StrSchema
            num_cpus = schemas.IntSchema
            ram_gb = schemas.IntSchema
            spot = schemas.BoolSchema
            price = schemas.NumberSchema
            
            
            class provider(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GCP(cls):
                    return cls("GCP")
            __annotations__ = {
                "machine_type": machine_type,
                "num_cpus": num_cpus,
                "ram_gb": ram_gb,
                "spot": spot,
                "price": price,
                "provider": provider,
            }
    
    machine_type: MetaOapg.properties.machine_type
    num_cpus: MetaOapg.properties.num_cpus
    price: MetaOapg.properties.price
    spot: MetaOapg.properties.spot
    ram_gb: MetaOapg.properties.ram_gb
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["machine_type"]) -> MetaOapg.properties.machine_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["num_cpus"]) -> MetaOapg.properties.num_cpus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ram_gb"]) -> MetaOapg.properties.ram_gb: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spot"]) -> MetaOapg.properties.spot: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["machine_type", "num_cpus", "ram_gb", "spot", "price", "provider", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["machine_type"]) -> MetaOapg.properties.machine_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["num_cpus"]) -> MetaOapg.properties.num_cpus: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ram_gb"]) -> MetaOapg.properties.ram_gb: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spot"]) -> MetaOapg.properties.spot: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> typing.Union[MetaOapg.properties.provider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["machine_type", "num_cpus", "ram_gb", "spot", "price", "provider", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        machine_type: typing.Union[MetaOapg.properties.machine_type, str, ],
        num_cpus: typing.Union[MetaOapg.properties.num_cpus, decimal.Decimal, int, ],
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, ],
        spot: typing.Union[MetaOapg.properties.spot, bool, ],
        ram_gb: typing.Union[MetaOapg.properties.ram_gb, decimal.Decimal, int, ],
        provider: typing.Union[MetaOapg.properties.provider, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MachineTypeResponse':
        return super().__new__(
            cls,
            *_args,
            machine_type=machine_type,
            num_cpus=num_cpus,
            price=price,
            spot=spot,
            ram_gb=ram_gb,
            provider=provider,
            _configuration=_configuration,
            **kwargs,
        )
