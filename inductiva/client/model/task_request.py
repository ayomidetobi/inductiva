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


class TaskRequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "simulator",
            "resource_pool",
            "container_image",
        }

        class properties:
            simulator = schemas.StrSchema
            resource_pool = schemas.StrSchema
            container_image = schemas.StrSchema
            storage_path_prefix = schemas.StrSchema

            class project(
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
                ) -> 'project':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class time_to_live_seconds(
                    schemas.ComposedSchema,):

                class MetaOapg:
                    any_of_0 = schemas.NumberSchema
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
                ) -> 'time_to_live_seconds':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            resubmit_on_preemption = schemas.BoolSchema
            __annotations__ = {
                "simulator": simulator,
                "resource_pool": resource_pool,
                "container_image": container_image,
                "storage_path_prefix": storage_path_prefix,
                "project": project,
                "time_to_live_seconds": time_to_live_seconds,
                "resubmit_on_preemption": resubmit_on_preemption,
            }

    simulator: MetaOapg.properties.simulator
    resource_pool: MetaOapg.properties.resource_pool
    container_image: MetaOapg.properties.container_image

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["simulator"]
    ) -> MetaOapg.properties.simulator:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["resource_pool"]
    ) -> MetaOapg.properties.resource_pool:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["container_image"]
    ) -> MetaOapg.properties.container_image:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["storage_path_prefix"]
    ) -> MetaOapg.properties.storage_path_prefix:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["project"]
    ) -> MetaOapg.properties.project:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["time_to_live_seconds"]
    ) -> MetaOapg.properties.time_to_live_seconds:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["resubmit_on_preemption"]
    ) -> MetaOapg.properties.resubmit_on_preemption:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal[
        "simulator",
        "resource_pool",
        "container_image",
        "storage_path_prefix",
        "project",
        "time_to_live_seconds",
        "resubmit_on_preemption",
    ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["simulator"]
    ) -> MetaOapg.properties.simulator:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["resource_pool"]
    ) -> MetaOapg.properties.resource_pool:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["container_image"]
    ) -> MetaOapg.properties.container_image:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["storage_path_prefix"]
    ) -> typing.Union[MetaOapg.properties.storage_path_prefix, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["project"]
    ) -> typing.Union[MetaOapg.properties.project, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["time_to_live_seconds"]
    ) -> typing.Union[MetaOapg.properties.time_to_live_seconds, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["resubmit_on_preemption"]
    ) -> typing.Union[MetaOapg.properties.resubmit_on_preemption,
                      schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal[
        "simulator",
        "resource_pool",
        "container_image",
        "storage_path_prefix",
        "project",
        "time_to_live_seconds",
        "resubmit_on_preemption",
    ], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        simulator: typing.Union[
            MetaOapg.properties.simulator,
            str,
        ],
        resource_pool: typing.Union[
            MetaOapg.properties.resource_pool,
            str,
        ],
        container_image: typing.Union[
            MetaOapg.properties.container_image,
            str,
        ],
        storage_path_prefix: typing.Union[
            MetaOapg.properties.storage_path_prefix, str,
            schemas.Unset] = schemas.unset,
        project: typing.Union[MetaOapg.properties.project, dict,
                              frozendict.frozendict, str, date, datetime,
                              uuid.UUID, int, float, decimal.Decimal, bool,
                              None, list, tuple, bytes, io.FileIO,
                              io.BufferedReader, schemas.Unset] = schemas.unset,
        time_to_live_seconds: typing.Union[
            MetaOapg.properties.time_to_live_seconds, dict,
            frozendict.frozendict, str, date, datetime, uuid.UUID, int, float,
            decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO,
            io.BufferedReader, schemas.Unset] = schemas.unset,
        resubmit_on_preemption: typing.Union[
            MetaOapg.properties.resubmit_on_preemption, bool,
            schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'TaskRequest':
        return super().__new__(
            cls,
            *_args,
            simulator=simulator,
            resource_pool=resource_pool,
            container_image=container_image,
            storage_path_prefix=storage_path_prefix,
            project=project,
            time_to_live_seconds=time_to_live_seconds,
            resubmit_on_preemption=resubmit_on_preemption,
            _configuration=_configuration,
            **kwargs,
        )
