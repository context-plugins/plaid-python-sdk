from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.bank_income_refresh_complete_result import BankIncomeRefreshCompleteResultOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class BankIncomeRefreshCompleteWebhook(SdkBaseModel):
    """Fired when a refreshed bank income report has finished generating or failed to generate. To obtain refreshed Bank
    Income data, send the user through Link's update mode, or migrate to CRA Income Insights and call
    ``/cra/check_report/create`` for a backend refresh. To get this webhook, subscribe via the `Dashboard
    <https://dashboard.plaid.com/developers/webhooks>`__."""

    webhook_type: str
    """``INCOME``"""

    webhook_code: str
    """``BANK_INCOME_REFRESH_COMPLETE``"""

    user_id: str
    """The ``user_id`` corresponding to the user the webhook has fired for."""

    result: BankIncomeRefreshCompleteResultOrStr
    """The result of the bank income refresh report generation

    ``SUCCESS``: The refreshed report was successfully generated and can be retrieved via ``/credit/bank_income/get``.

    ``FAILURE``: The refreshed report failed to be generated"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class BankIncomeRefreshCompleteWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    user_id: str
    result: BankIncomeRefreshCompleteResultOrStr
    environment: WebhookEnvironmentValuesOrStr
