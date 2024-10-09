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
    TASKS_TASK_ID_DOWNLOAD_INPUT_URL = "/tasks/{task_id}/download_input_url"
    TASKS_TASK_ID_DOWNLOAD_OUTPUT_URL = "/tasks/{task_id}/download_output_url"
    TASKS_TASK_ID_OUTPUT = "/tasks/{task_id}/output"
    TASKS_TASK_ID_RESUBMIT = "/tasks/{task_id}/resubmit"
    TASKS_TASK_ID_KILL = "/tasks/{task_id}/kill"
    TASKS_TASK_ID_DISABLE_LOGS = "/tasks/{task_id}/disable_logs"
    TASKS_TASK_ID_FILES = "/tasks/{task_id}/files"
    ADMIN_USERS = "/admin/users"
    ADMIN_USERS_EMAIL_TERMS_AND_CONDITIONS = "/admin/users/{email}/terms_and_conditions"
    ADMIN_USERS_USERNAME_ORGANIZATION = "/admin/users/{username}/organization"
    ADMIN_USERS_USERNAME_TIER = "/admin/users/{username}/tier"
    ADMIN_USERS_USERNAME_CREDITS = "/admin/users/{username}/credits"
    ADMIN_USERS_EMAIL_API_KEY = "/admin/users/{email}/api_key"
    ADMIN_USERS_EMAIL = "/admin/users/{email}"
    ADMIN_USERS_EMAIL_CAMPAIGN_CAMPAIGN_ID = "/admin/users/{email}/campaign/{campaign_id}"
    ADMIN_USERS_USERNAME_STORAGE_SIZE_FS = "/admin/users/{username}/storage_size_fs"
    ADMIN_USERS_USERNAME_STORAGE_SIZE = "/admin/users/{username}/storage_size"
    ADMIN_USERS_USERNAME_TASKS = "/admin/users/{username}/tasks"
    ADMIN_USERS_USERNAME_CAPABILITIES = "/admin/users/{username}/capabilities"
    ADMIN_GROUPS = "/admin/groups"
    ADMIN_GROUPS_ACTIVE = "/admin/groups/active"
    ADMIN_PROVIDERS = "/admin/providers"
    ADMIN_PROVIDERS_PROVIDER_ID = "/admin/providers/{provider_id}"
    ADMIN_ACTIVE_TASKS = "/admin/active_tasks"
    ADMIN_EXECUTERTRACKER_TOKEN = "/admin/executer-tracker/token"
    ADMIN_GROUPS_MACHINE_GROUP_ID_TERMINATE = "/admin/groups/{machine_group_id}/terminate"
    ADMIN_CAMPAIGNS = "/admin/campaigns"
    ADMIN_CAMPAIGNS_CAMPAIGN_ID = "/admin/campaigns/{campaign_id}"
    ADMIN_CAMPAIGNS_CAMPAIGN_ID_DEACTIVATE = "/admin/campaigns/{campaign_id}/deactivate"
    ADMIN_CAMPAIGNS_CAMPAIGN_ID_USERS = "/admin/campaigns/{campaign_id}/users"
    ADMIN_CAMPAIGNS_CAMPAIGN_ID_CAPABILITIES = "/admin/campaigns/{campaign_id}/capabilities"
    ADMIN_CAMPAIGNS_CAMPAIGN_ID_CAPABILITIES_CAPABILITY_ID = "/admin/campaigns/{campaign_id}/capabilities/{capability_id}"
    ADMIN_CAMPAIGNS_CAMPAIGN_ID_QUOTAS = "/admin/campaigns/{campaign_id}/quotas"
    ADMIN_CAMPAIGNS_CAMPAIGN_ID_QUOTAS_QUOTA_ID = "/admin/campaigns/{campaign_id}/quotas/{quota_id}"
    ADMIN_ORGANIZATIONS = "/admin/organizations"
    ADMIN_ORGANIZATIONS_ORGANIZATION_ID = "/admin/organizations/{organization_id}"
    ADMIN_ORGANIZATIONS_BILLING = "/admin/organizations/billing"
    ADMIN_TIERS = "/admin/tiers"
    EXECUTERTRACKER_REGISTER = "/executer-tracker/register"
    EXECUTERTRACKER_MACHINE_ID = "/executer-tracker/{machine_id}"
    EXECUTERTRACKER_MACHINE_ID_TASK = "/executer-tracker/{machine_id}/task"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_MESSAGE = "/executer-tracker/{machine_id}/task/{task_id}/message"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_MESSAGE_UNBLOCK = "/executer-tracker/{machine_id}/task/{task_id}/message/unblock"
    EXECUTERTRACKER_MACHINE_ID_EVENT = "/executer-tracker/{machine_id}/event"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_DOWNLOAD_INPUT_URL = "/executer-tracker/{machine_id}/task/{task_id}/download_input_url"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_UPLOAD_OUTPUT_URL = "/executer-tracker/{machine_id}/task/{task_id}/upload_output_url"
    EXECUTERTRACKER_MACHINE_ID_TASK_TASK_ID_METRIC = "/executer-tracker/{machine_id}/task/{task_id}/metric"
    EXECUTERTRACKER_MACHINE_ID_RESIZE_DISK = "/executer-tracker/{machine_id}/resize_disk"
    EXECUTERTRACKER_MACHINE_ID_RESIZE_DISK_DONE = "/executer-tracker/{machine_id}/resize_disk_done"
    COMPUTE_GROUP = "/compute/group"
    COMPUTE_TYPE = "/compute/type"
    COMPUTE_GROUP_START = "/compute/group/start"
    COMPUTE_PRICE = "/compute/price"
    COMPUTE_GROUPS = "/compute/groups"
    COMPUTE_GROUP_STATUS = "/compute/group_status"
    COMPUTE_MACHINE_TYPES = "/compute/machine_types"
    COMPUTE_GROUP_NAME = "/compute/group/{name}"
    STORAGE_SIZE = "/storage/size"
    STORAGE_CONTENTS = "/storage/contents"
    VERSION = "/version"
    VERSIONCHECK = "/version-check"
    USERS_QUOTAS = "/users/quotas"
    USERS_INFO = "/users/info"
    USERS_CAPABILITIES = "/users/capabilities"
    PROJECTS = "/projects"
    PROJECTS_NAME = "/projects/{name}"
    METRICS_USERS_USERNAME_ACTIVITY = "/metrics/users/{username}/activity"
    METRICS_USERS_USERNAME_COST_OVER_TIME = "/metrics/users/{username}/cost_over_time"
    METRICS_USERS_USERNAME_TASK_STATUS_OVERVIEW = "/metrics/users/{username}/task_status_overview"
    METRICS_USERS_USERNAME_COMPUTATION_TIME_TREND = "/metrics/users/{username}/computation_time_trend"
    METRICS_USERS_USERNAME_TASKS_OVERVIEW = "/metrics/users/{username}/tasks_overview"
    METRICS_USERS_USERNAME_MOST_USED_MACHINE_TYPES = "/metrics/users/{username}/most_used_machine_types"
    METRICS_USERS_USERNAME_MOST_USED_SIMULATORS_OVERVIEW = "/metrics/users/{username}/most_used_simulators_overview"
