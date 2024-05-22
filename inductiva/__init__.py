"""Client for Inductiva's web API."""
import os
import sys
import logging
import contextvars

import absl

from . import api
from . import simulators
from . import resources
from . import storage
from . import utils
from . import tasks
from . import users
from . import logs
from . import projects
from .templating import TemplateManager

logs.setup()

api_url = os.environ.get("INDUCTIVA_API_URL", "https://api.inductiva.ai")
_output_dir = contextvars.ContextVar("INDUCTIVA_OUTPUT_DIR",
                                     default=os.environ.get(
                                         "INDUCTIVA_OUTPUT_DIR",
                                         "inductiva_output"))
_api_key = contextvars.ContextVar("INDUCTIVA_API_KEY",
                                  default=os.environ.get(
                                      "INDUCTIVA_API_KEY", None))

absl.logging.set_verbosity(absl.logging.INFO)

# Disable urllib3 warnings.
# TODO: Verify and fix the appearance of this warning.
urllib3_logger = logging.getLogger("urllib3.connectionpool")
urllib3_logger.setLevel(logging.CRITICAL)

__version__ = "0.6.0"


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


def _check_key():
    if utils.format_utils.getenv_bool("GITHUB_ACTIONS", False) is not True:
        api.methods.validate_api_key()


_check_for_available_package_update()


def set_api_key(api_key):
    """Sets the value of `inductiva._api_key` to `api_key"""
    _api_key.set(api_key)


def get_api_key():
    """Returns the value of inductiva._api_key"""
    return _api_key.get()


def _supports_ansi():
    """Checks if we support ansi formatting for colors and bolds"""
    user_disable_ansi = utils.format_utils.getenv_bool("INDUCTIVA_DISABLE_ANSI",
                                                       False)
    if sys.platform.startswith("win"):
        return "TERM" in os.environ and os.environ[
            "TERM"] == "xterm" and not user_disable_ansi
    return hasattr(sys.stdout,
                   "isatty") and sys.stdout.isatty() and not user_disable_ansi


_ansi_enabled = _supports_ansi()

_check_key()
