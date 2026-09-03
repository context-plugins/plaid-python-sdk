from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class BankIncomeRefreshUpdateWebhook(SdkBaseModel):
    """Fired when a change to the user's income is detected. To obtain refreshed Bank Income data, send the user through
    Link's update mode so they can confirm their income sources, or migrate to CRA Income Insights and call
    ``/cra/check_report/create`` for a backend refresh. To receive this webhook, subscribe in the `Dashboard
    <https://dashboard.plaid.com/developers/webhooks>`__."""

    webhook_type: str
    """``INCOME``"""

    webhook_code: str
    """``BANK_INCOME_REFRESH_UPDATE``"""

    user_id: str
    """The ``user_id`` corresponding to the user the webhook has fired for."""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class BankIncomeRefreshUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    user_id: str
    environment: WebhookEnvironmentValuesOrStr
