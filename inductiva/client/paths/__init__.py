# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from inductiva.client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    TASKS_AUTH = "/tasks/auth"
    TASKS_SUBMIT = "/tasks/submit"
    TASKS_TASK_ID_INPUT_UPLOAD_URL = "/tasks/{task_id}/input_upload_url"
    TASKS_TASK_ID_INPUT_UPLOADED = "/tasks/{task_id}/input_uploaded"
    TASKS_TASK_ID_INPUT = "/tasks/{task_id}/input"
    TASKS_TASK_ID = "/tasks/{task_id}"
    TASKS = "/tasks"
    TASKS_TASK_ID_STATUS = "/tasks/{task_id}/status"
    TASKS_TASK_ID_POSITION_IN_QUEUE = "/tasks/{task_id}/position_in_queue"
    TASKS_TASK_ID_OUTPUT_LIST = "/tasks/{task_id}/output/list"
    TASKS_TASK_ID_DOWNLOAD_OUTPUT_URL = "/tasks/{task_id}/download_output_url"
    TASKS_TASK_ID_OUTPUT = "/tasks/{task_id}/output"
    TASKS_TASK_ID_RESUBMIT = "/tasks/{task_id}/resubmit"
    TASKS_TASK_ID_KILL = "/tasks/{task_id}/kill"
    TASKS_TASK_ID_DISABLE_LOGS = "/tasks/{task_id}/disable_logs"
    ADMIN_USERS = "/admin/users"
    ADMIN_USERS_EMAIL_API_KEY = "/admin/users/{email}/api_key"
    ADMIN_USERS_EMAIL = "/admin/users/{email}"
    ADMIN_USERS_EMAIL_EXPIRY_TS = "/admin/users/{email}/expiry_ts"
    ADMIN_USERS_USERNAME_TASKS = "/admin/users/{username}/tasks"
    ADMIN_GROUPS = "/admin/groups"
    ADMIN_GROUPS_ACTIVE = "/admin/groups/active"
    ADMIN_GROUPS_DEFAULT = "/admin/groups/default"
    ADMIN_GROUPS_DEFAULT_MACHINE_GROUP_ID = "/admin/groups/default/{machine_group_id}"
    ADMIN_PROVIDERS = "/admin/providers"
    ADMIN_PROVIDERS_PROVIDER_ID = "/admin/providers/{provider_id}"
    ADMIN_ACTIVE_TASKS = "/admin/active_tasks"
    ADMIN_USERS_USERNAME_COST = "/admin/users/{username}/cost"
    ADMIN_EXECUTERTRACKER_TOKEN = "/admin/executer-tracker/token"
    EXECUTERTRACKER_REGISTER = "/executer-tracker/register"
    EXECUTERTRACKER_MACHINE_ID = "/executer-tracker/{machine_id}"
    EXECUTERTRACKER_MACHINE_ID_TASK = "/executer-tracker/{machine_id}/task"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_ACK = "/executer-tracker/{machine_id}/task/{task_id}/ack"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_MESSAGE = "/executer-tracker/{machine_id}/task/{task_id}/message"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_MESSAGE_UNBLOCK = "/executer-tracker/{machine_id}/task/{task_id}/message/unblock"
    EXECUTERTRACKER_MACHINE_ID_EVENT = "/executer-tracker/{machine_id}/event"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_DOWNLOAD_INPUT_URL = "/executer-tracker/{machine_id}/task/{task_id}/download_input_url"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_UPLOAD_OUTPUT_URL = "/executer-tracker/{machine_id}/task/{task_id}/upload_output_url"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_METRIC = "/executer-tracker/{machine_id}/task/{task_id}/metric"
    COMPUTE_GROUP = "/compute/group"
    COMPUTE_TYPE = "/compute/type"
    COMPUTE_GROUP_START = "/compute/group/start"
    COMPUTE_GROUP_MG_ID = "/compute/group/{mg_id}"
    COMPUTE_PRICE = "/compute/price"
    COMPUTE_GROUPS = "/compute/groups"
    COMPUTE_GROUP_STATUS = "/compute/group_status"
    COMPUTE_MACHINE_TYPES = "/compute/machine_types"
    COMPUTE_GROUP_NAME = "/compute/group/{name}"
    STORAGE_SIZE = "/storage/size"
    STORAGE_CONTENTS = "/storage/contents"
    VERSION = "/version"
    VERSIONCHECK = "/version-check"
    USERS_COST = "/users/cost"
    USERS_QUOTAS = "/users/quotas"
    USERS_ME = "/users/me"
    PROJECTS = "/projects"
    PROJECTS_NAME = "/projects/{name}"
