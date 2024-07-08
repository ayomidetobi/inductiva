"""Methods to interact with the user info on the API."""
import json
from typing import Any, Dict

from inductiva import api
from inductiva.client import ApiClient
from inductiva.client.apis.tags.users_api import UsersApi


def _fetch_quotas_from_api() -> Dict[str, Dict[str, Any]]:
    """Get information about a user's quotas.
    """
    api_config = api.get_api_config()

    with ApiClient(api_config) as client:
        api_instance = UsersApi(client)

        resp = api_instance.get_user_quotas(skip_deserialization=True).response
        quotas = json.loads(resp.data.decode("utf-8"))

        return quotas


def get_quotas() -> Dict[str, Dict[str, Any]]:
    """Get the user quotas.

    This function gets a dict with the user quotas.

    Returns:
        Dict with the user quotas.
    """
    quotas = _fetch_quotas_from_api()

    return quotas


def get_info() -> Dict[str, Any]:
    """Get the user credits.

    Returns:
        Dict with the user credits.
    """

    api_config = api.get_api_config()
    with (ApiClient(api_config)) as client:
        api_instance = UsersApi(client)
        request = api_instance.get_auth_user_info()

    request.body = {
        "email": "pbarbosa@inductiva.ai",
        "username": "pbarbosa",
        "tier": "Fremium",
        "credits": {
            "processing_hours": {
                "used": 50,
                "total": 100,
                "remaining": 50
            },
            "queue_time": {
                "used": 50,
                "total": 100,
                "remaining": 50
            }
        }
    }

    return request.body
