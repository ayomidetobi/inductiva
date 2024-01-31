"""Client for Inductiva's web API."""
import os
import logging
import contextvars

import absl

from . import api
from . import simulators
from . import resources
from . import storage
from . import utils
from . import tasks
from . import logs

logs.setup()

api_url = os.environ.get("INDUCTIVA_API_URL", "https://api.inductiva.ai")
_output_dir = contextvars.ContextVar("INDUCTIVA_OUTPUT_DIR")
_output_dir.set(os.environ.get("INDUCTIVA_OUTPUT_DIR", "inductiva_output"))
api_key = os.environ.get("INDUCTIVA_API_KEY")

absl.logging.set_verbosity(absl.logging.INFO)

# Disable urllib3 warnings.
# TODO: Verify and fix the appearance of this warning.
urllib3_logger = logging.getLogger("urllib3.connectionpool")
urllib3_logger.setLevel(logging.CRITICAL)

__version__ = "0.4.2"


def set_output_dir(new_output_dir):
    """Sets the value of `inductiva._output_dir` to `new_output_dir`"""
    _output_dir.set(new_output_dir)


def get_output_dir():
    """Returns the value of inductiva._output_dir"""
    return _output_dir.get()


def _check_for_available_package_update():
    # pylint: disable=import-outside-toplevel
    from .localization import translator as __
    import urllib3
    import json
    import sys

    new_version = __version__

    try:
        http = urllib3.PoolManager()
        resp = http.request("GET",
                            "https://pypi.org/pypi/inductiva/json",
                            headers={"Accept": "application/json"})
        json_response = json.loads(resp.data)
        new_version = json_response["info"]["version"]

    except Exception as ex:  # pylint: disable=broad-exception-caught
        logging.warning(__("failed-update-check", ex), exc_info=True)

    if new_version != __version__:
        msg = __("upgrade-available", new_version, __version__)
        print(msg, file=sys.stderr)


_check_for_available_package_update()
