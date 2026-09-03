from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.statements_refresh_complete_result import StatementsRefreshCompleteResultOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class StatementsRefreshCompleteWebhook(SdkBaseModel):
    """Fired when refreshed statements extraction is completed or failed to be completed. Triggered by calling
    ``/statements/refresh``."""

    webhook_type: str
    """``STATEMENTS``"""

    webhook_code: str
    """``STATEMENTS_REFRESH_COMPLETE``"""

    item_id: str
    """The Plaid Item ID. The ``item_id`` is always unique; linking the same account at the same institution twice will
    result in two Items with different ``item_id`` values. Like all Plaid identifiers, the ``item_id`` is
    case-sensitive."""

    result: StatementsRefreshCompleteResultOrStr
    """The result of the statement refresh extraction

    ``SUCCESS``: The statements were successfully extracted and can be listed via ``/statements/list`` and downloaded
    via ``/statements/download``.

    ``FAILURE``: The statements failed to be extracted."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class StatementsRefreshCompleteWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    result: StatementsRefreshCompleteResultOrStr
    environment: WebhookEnvironmentValuesOrStr
