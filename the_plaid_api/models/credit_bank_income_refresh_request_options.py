from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditBankIncomeRefreshRequestOptions(SdkBaseModel):
    """An optional object for ``/credit/bank_income/refresh`` request options."""

    days_requested: Optional[int] = UNSET
    """How many days of data to include in the refresh. If not specified, this will default to the days requested in the
    most recently generated bank income report for the user."""


class CreditBankIncomeRefreshRequestOptionsDict(TypedDict):
    days_requested: NotRequired[int]
