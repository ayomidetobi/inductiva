# coding: utf-8
"""
    InductivaWebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from inductiva.client.paths.storage_folder_name.delete import DeleteFile
from inductiva.client.paths.storage_cost.get import GetStorageMonthlyCost
from inductiva.client.paths.storage_size.get import GetStorageSize
from inductiva.client.paths.storage_folder_name_input_url.get import GetUploadUrl
from inductiva.client.paths.storage_contents.get import ListStorageContents
from inductiva.client.paths.storage_folder_name_input_notify.post import NotifyUploadFile
from inductiva.client.paths.storage_folder_name_input.put import UploadFile
from inductiva.client.paths.storage_folder_name_input_remote.post import UploadFromUrl


class StorageApi(
        DeleteFile,
        GetStorageMonthlyCost,
        GetStorageSize,
        GetUploadUrl,
        ListStorageContents,
        NotifyUploadFile,
        UploadFile,
        UploadFromUrl,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
