from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.monitoring_insights_status import MonitoringInsightsStatusOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class CashFlowUpdatesNewLoanPaymentWebhook(SdkBaseModel):
    """For each user's Item enabled for Cash Flow Updates, this webhook will fire when an update detects a new loan
    payment. Upon receiving the webhook, call ``/cra/monitoring_insights/get`` to retrieve the updated insights."""

    webhook_type: str
    """``CASH_FLOW_UPDATES``"""

    webhook_code: str
    """``NEW_LOAN_PAYMENT_DETECTED``"""

    status: MonitoringInsightsStatusOrStr
    """Enum for the status of the insights"""

    user_id: str
    """The ``user_id`` that the report is associated with"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class CashFlowUpdatesNewLoanPaymentWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    status: MonitoringInsightsStatusOrStr
    user_id: str
    environment: WebhookEnvironmentValuesOrStr
