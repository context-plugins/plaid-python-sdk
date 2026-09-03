from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bank_income_refresh_complete_result import BankIncomeRefreshCompleteResultOrStr


class SandboxBankIncomeWebhookFireRequestWebhookFields(SdkBaseModel):
    """Optional fields which will be populated in the simulated webhook"""

    user_id: str
    """The user id to be returned in INCOME webhooks"""

    bank_income_refresh_complete_result: Optional[BankIncomeRefreshCompleteResultOrStr] = UNSET
    """The result of the bank income refresh report generation

    ``SUCCESS``: The refreshed report was successfully generated and can be retrieved via ``/credit/bank_income/get``.

    ``FAILURE``: The refreshed report failed to be generated"""


class SandboxBankIncomeWebhookFireRequestWebhookFieldsDict(TypedDict):
    user_id: str
    bank_income_refresh_complete_result: NotRequired[BankIncomeRefreshCompleteResultOrStr]
