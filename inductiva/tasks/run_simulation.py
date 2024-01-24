"""Functions for running simulations via Inductiva Web API."""
import pathlib
from typing import Any, Optional
import json
import threading

from absl import logging

from inductiva import tasks, types
from inductiva.api import methods
from inductiva.utils import format_utils, files

TASK_METADATA_FILENAME = "task_metadata.json"
TASK_METADATA_FILENAME_UPLOAD = "uploaded_metadata.json"

_metadata_lock = threading.RLock()


def run_simulation(
    api_method_name: str,
    input_dir: pathlib.Path,
    computational_resources: Optional[types.ComputationalResources] = None,
    storage_dir: Optional[types.Path] = "",
    api_invoker=None,
    extra_metadata=None,
    **kwargs: Any,
) -> tasks.Task:
    """Run a simulation via Inductiva Web API."""

    params = {
        "sim_dir": input_dir,
        **kwargs,
    }
    type_annotations = {
        "sim_dir": pathlib.Path,
    }

    if api_invoker is None:
        api_invoker = methods.invoke_async_api

    task_id = api_invoker(
        api_method_name,
        params,
        type_annotations,
        resource_pool=computational_resources,
        storage_path_prefix=storage_dir,
    )

    if computational_resources is not None:
        logging.info(
            "Task %s submitted to the queue of the %s.",
            task_id, computational_resources)
    else:
        logging.info(
            "Task %s submitted to the default queue. It will be picked for"
            "execution whenever a computational resource is available.",
            task_id)

    task = tasks.Task(task_id)
    if not isinstance(task_id, str):
        raise RuntimeError(
            f"Expected result to be a string with task_id, got {type(task_id)}")

    if not format_utils.getenv_bool("DISABLE_TASK_METADATA_LOGGING", False):
        machine_group_id = None
        if computational_resources is not None:
            machine_group_id = computational_resources.id

        metadata = {
            "api_method_name": api_method_name.split(".")[1],
            "machine_group_id": machine_group_id,
            "storage_dir": str(storage_dir),
            **kwargs,
        }
        if extra_metadata is not None:
            metadata = {**metadata, **extra_metadata}

        with _metadata_lock:
            task_metadata_file = _save_metadata(metadata,
                           mode="w",
                           path=pathlib.Path(input_dir) /
                           TASK_METADATA_FILENAME_UPLOAD)

        with _metadata_lock:
            global_metadata_file = _save_metadata({
                **{
                    "task_id": task_id,
                    "input_dir": str(input_dir)
                },
                **metadata
            })
        logging.info("Task configuration metadata is saved in a file in "
                     "the local input directory %s and added to the general "
                     "tasks metadata file in %s.", task_metadata_file,
                     global_metadata_file)

    logging.info("Consider tracking the status of the task via cli:"
                 " $inductiva tasks list")

    return task


def _save_metadata(metadata, mode="a", path=None):
    """Appends metadata to the TASK_METADATA_FILENAME in the cwd."""
    if path is None:
        file_path = files.resolve_path(TASK_METADATA_FILENAME)
    else:
        file_path = files.resolve_path(path)
    with open(file_path, mode, encoding="utf-8") as f:
        json.dump(metadata, f)
        f.write("\n")

    return file_path
