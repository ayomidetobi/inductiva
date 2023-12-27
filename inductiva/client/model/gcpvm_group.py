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


class GCPVMGroup(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Schema for creating a GCP instance group.
    """

    class MetaOapg:
        required = {
            "machine_type",
            "num_vms",
            "spot",
            "is_elastic",
            "disk_size_gb",
        }

        class properties:
            machine_type = schemas.StrSchema
            disk_size_gb = schemas.IntSchema
            num_vms = schemas.IntSchema
            spot = schemas.BoolSchema
            is_elastic = schemas.BoolSchema

            class id(
                    schemas.UUIDBase,
                    schemas.ComposedSchema,
            ):

                class MetaOapg:
                    format = 'uuid'
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
                ) -> 'id':
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

            class creation_timestamp(
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
                ) -> 'creation_timestamp':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class deletion_timestamp(
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
                ) -> 'deletion_timestamp':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class min_vms(
                    schemas.ComposedSchema,):

                class MetaOapg:
                    any_of_0 = schemas.IntSchema
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
                ) -> 'min_vms':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class max_vms(
                    schemas.ComposedSchema,):

                class MetaOapg:
                    any_of_0 = schemas.IntSchema
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
                ) -> 'max_vms':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class provider(schemas.EnumBase, schemas.StrSchema):

                class MetaOapg:
                    enum_value_to_name = {
                        "GCP": "GCP",
                    }

                @schemas.classproperty
                def GCP(cls):
                    return cls("GCP")

            __annotations__ = {
                "machine_type": machine_type,
                "disk_size_gb": disk_size_gb,
                "num_vms": num_vms,
                "spot": spot,
                "is_elastic": is_elastic,
                "id": id,
                "name": name,
                "creation_timestamp": creation_timestamp,
                "deletion_timestamp": deletion_timestamp,
                "min_vms": min_vms,
                "max_vms": max_vms,
                "provider": provider,
            }

    machine_type: MetaOapg.properties.machine_type
    num_vms: MetaOapg.properties.num_vms
    spot: MetaOapg.properties.spot
    is_elastic: MetaOapg.properties.is_elastic
    disk_size_gb: MetaOapg.properties.disk_size_gb

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["machine_type"]
    ) -> MetaOapg.properties.machine_type:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["disk_size_gb"]
    ) -> MetaOapg.properties.disk_size_gb:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["num_vms"]
    ) -> MetaOapg.properties.num_vms:
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["spot"]
    ) -> MetaOapg.properties.spot:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["is_elastic"]
    ) -> MetaOapg.properties.is_elastic:
        ...

    @typing.overload
    def __getitem__(
            self,
            name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id:
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["creation_timestamp"]
    ) -> MetaOapg.properties.creation_timestamp:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["deletion_timestamp"]
    ) -> MetaOapg.properties.deletion_timestamp:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["min_vms"]
    ) -> MetaOapg.properties.min_vms:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["max_vms"]
    ) -> MetaOapg.properties.max_vms:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["provider"]
    ) -> MetaOapg.properties.provider:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal[
        "machine_type",
        "disk_size_gb",
        "num_vms",
        "spot",
        "is_elastic",
        "id",
        "name",
        "creation_timestamp",
        "deletion_timestamp",
        "min_vms",
        "max_vms",
        "provider",
    ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["machine_type"]
    ) -> MetaOapg.properties.machine_type:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["disk_size_gb"]
    ) -> MetaOapg.properties.disk_size_gb:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["num_vms"]
    ) -> MetaOapg.properties.num_vms:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: typing_extensions.Literal["spot"]
    ) -> MetaOapg.properties.spot:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["is_elastic"]
    ) -> MetaOapg.properties.is_elastic:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["id"]
    ) -> typing.Union[MetaOapg.properties.id, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> typing.Union[MetaOapg.properties.name, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["creation_timestamp"]
    ) -> typing.Union[MetaOapg.properties.creation_timestamp, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["deletion_timestamp"]
    ) -> typing.Union[MetaOapg.properties.deletion_timestamp, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["min_vms"]
    ) -> typing.Union[MetaOapg.properties.min_vms, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["max_vms"]
    ) -> typing.Union[MetaOapg.properties.max_vms, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["provider"]
    ) -> typing.Union[MetaOapg.properties.provider, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal[
        "machine_type",
        "disk_size_gb",
        "num_vms",
        "spot",
        "is_elastic",
        "id",
        "name",
        "creation_timestamp",
        "deletion_timestamp",
        "min_vms",
        "max_vms",
        "provider",
    ], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        machine_type: typing.Union[
            MetaOapg.properties.machine_type,
            str,
        ],
        num_vms: typing.Union[
            MetaOapg.properties.num_vms,
            decimal.Decimal,
            int,
        ],
        spot: typing.Union[
            MetaOapg.properties.spot,
            bool,
        ],
        is_elastic: typing.Union[
            MetaOapg.properties.is_elastic,
            bool,
        ],
        disk_size_gb: typing.Union[
            MetaOapg.properties.disk_size_gb,
            decimal.Decimal,
            int,
        ],
        id: typing.Union[MetaOapg.properties.id, dict, frozendict.frozendict,
                         str, date, datetime, uuid.UUID, int, float,
                         decimal.Decimal, bool, None, list, tuple, bytes,
                         io.FileIO, io.BufferedReader,
                         schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, dict,
                           frozendict.frozendict, str, date, datetime,
                           uuid.UUID, int, float, decimal.Decimal, bool, None,
                           list, tuple, bytes, io.FileIO, io.BufferedReader,
                           schemas.Unset] = schemas.unset,
        creation_timestamp: typing.Union[MetaOapg.properties.creation_timestamp,
                                         dict, frozendict.frozendict, str, date,
                                         datetime, uuid.UUID, int, float,
                                         decimal.Decimal, bool, None, list,
                                         tuple, bytes, io.FileIO,
                                         io.BufferedReader,
                                         schemas.Unset] = schemas.unset,
        deletion_timestamp: typing.Union[MetaOapg.properties.deletion_timestamp,
                                         dict, frozendict.frozendict, str, date,
                                         datetime, uuid.UUID, int, float,
                                         decimal.Decimal, bool, None, list,
                                         tuple, bytes, io.FileIO,
                                         io.BufferedReader,
                                         schemas.Unset] = schemas.unset,
        min_vms: typing.Union[MetaOapg.properties.min_vms, dict,
                              frozendict.frozendict, str, date, datetime,
                              uuid.UUID, int, float, decimal.Decimal, bool,
                              None, list, tuple, bytes, io.FileIO,
                              io.BufferedReader, schemas.Unset] = schemas.unset,
        max_vms: typing.Union[MetaOapg.properties.max_vms, dict,
                              frozendict.frozendict, str, date, datetime,
                              uuid.UUID, int, float, decimal.Decimal, bool,
                              None, list, tuple, bytes, io.FileIO,
                              io.BufferedReader, schemas.Unset] = schemas.unset,
        provider: typing.Union[MetaOapg.properties.provider, str,
                               schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'GCPVMGroup':
        return super().__new__(
            cls,
            *_args,
            machine_type=machine_type,
            num_vms=num_vms,
            spot=spot,
            is_elastic=is_elastic,
            disk_size_gb=disk_size_gb,
            id=id,
            name=name,
            creation_timestamp=creation_timestamp,
            deletion_timestamp=deletion_timestamp,
            min_vms=min_vms,
            max_vms=max_vms,
            provider=provider,
            _configuration=_configuration,
            **kwargs,
        )
