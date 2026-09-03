from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.bank_income_complete_result import BankIncomeCompleteResultOrStr
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class BankIncomeCompleteWebhook(SdkBaseModel):
    """Fired when a bank income report has finished generating or failed to generate, triggered by calling
    ``/credit/bank_income/get`` in CRA enabled client."""

    webhook_type: str
    """``INCOME``"""

    webhook_code: str
    """``BANK_INCOME_COMPLETE``"""

    user_id: str
    """The ``user_id`` corresponding to the user the webhook has fired for."""

    result: BankIncomeCompleteResultOrStr
    """The result of the bank income report generation

    ``SUCCESS``: The bank income report was successfully generated and can be retrieved via ``/credit/bank_income/get``.

    ``FAILURE``: The bank income report failed to be generated"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class BankIncomeCompleteWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    user_id: str
    result: BankIncomeCompleteResultOrStr
    environment: WebhookEnvironmentValuesOrStr
