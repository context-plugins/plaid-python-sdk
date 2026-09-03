from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.monitoring_insights_status import MonitoringInsightsStatusOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class CashFlowUpdatesInsightsWebhook(SdkBaseModel):
    """For each user's Item enabled for Cash Flow Updates, this webhook will fire between one and four times a day with
    information on the status of the update. This webhook will not fire immediately upon enrollment in Cash Flow
    Updates. Upon receiving the webhook, call ``/cra/monitoring_insights/get`` to retrieve the updated insights. At
    approximately the same time as the ``INSIGHTS_UPDATED`` webhook, any event-driven ``CASH_FLOW_UPDATES`` webhooks
    (e.g. ``LOW_BALANCE_DETECTED``, ``LARGE_DEPOSIT_DETECTED``) that were triggered by the update will also fire. This
    webhook has been replaced by the ``CASH_FLOW_INSIGHTS_UPDATED`` webhook for all customers who began using Plaid
    Check on or after December 10, 2025."""

    webhook_type: str
    """``CASH_FLOW_UPDATES``"""

    webhook_code: str
    """``INSIGHTS_UPDATED``"""

    status: MonitoringInsightsStatusOrStr
    """Enum for the status of the insights"""

    user_id: str
    """The ``user_id`` that the report is associated with"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class CashFlowUpdatesInsightsWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    status: MonitoringInsightsStatusOrStr
    user_id: str
    environment: WebhookEnvironmentValuesOrStr
