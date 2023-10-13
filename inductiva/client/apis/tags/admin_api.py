# coding: utf-8
"""
    InductivaWebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from inductiva.client.paths.admin_users.post import AddUser
from inductiva.client.paths.admin_users_username_tasks.get import GetTasksByUsername
from inductiva.client.paths.admin_users_username.get import GetUser
from inductiva.client.paths.admin_groups.get import ListActiveInstanceGroups


class AdminApi(
        AddUser,
        GetTasksByUsername,
        GetUser,
        ListActiveInstanceGroups,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
