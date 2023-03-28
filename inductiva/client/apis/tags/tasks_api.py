# coding: utf-8
"""
    InductivaWebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from inductiva.client.paths.task_task_id_output.get import DownloadTaskOutput
from inductiva.client.paths.task_task_id_status.get import GetTaskStatus
from inductiva.client.paths.task_task_id_kill.post import KillTask
from inductiva.client.paths.task_submit.post import SubmitTask
from inductiva.client.paths.task_task_id_input.post import UploadTaskInput


class TasksApi(
        DownloadTaskOutput,
        GetTaskStatus,
        KillTask,
        SubmitTask,
        UploadTaskInput,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
