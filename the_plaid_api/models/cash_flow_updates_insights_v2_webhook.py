from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.cash_flow_insight import CashFlowInsightOrStr
from .enums.monitoring_insights_status import MonitoringInsightsStatusOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class CashFlowUpdatesInsightsV2Webhook(SdkBaseModel):
    """For each item on an enabled user, this webhook will fire up to four times a day with status information. This
    webhook will not fire immediately upon enrollment in Cash Flow Updates. The payload may contain an ``insights``
    array with insights that have been detected, if any (e.g. ``LOW_BALANCE_DETECTED``, ``LARGE_DEPOSIT_DETECTED``).
    Upon receiving the webhook, call ``/cra/monitoring_insights/get`` to retrieve the updated insights."""

    webhook_type: str
    """``CASH_FLOW_UPDATES``"""

    webhook_code: str
    """``CASH_FLOW_INSIGHTS_UPDATED``"""

    status: MonitoringInsightsStatusOrStr
    """Enum for the status of the insights"""

    user_id: str
    """The ``user_id`` associated with the user whose data is being requested. This is received by calling
    ``/user/create``."""

    insights: list[CashFlowInsightOrStr]
    """Array containing the insights detected within the generated report, if any. Possible values include:
      ``LARGE_DEPOSIT_DETECTED``: signaling a deposit over $5,000
      ``LOW_BALANCE_DETECTED``: signaling a balance below $100
      ``NEW_LOAN_PAYMENT_DETECTED``: signaling a new loan payment
      ``NSF_OVERDRAFT_DETECTED``: signaling an NSF overdraft"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class CashFlowUpdatesInsightsV2WebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    status: MonitoringInsightsStatusOrStr
    user_id: str
    insights: list[CashFlowInsightOrStr]
    environment: WebhookEnvironmentValuesOrStr
