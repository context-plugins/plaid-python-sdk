from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditBankIncomeGetRequestOptions(SdkBaseModel):
    """An optional object for ``/credit/bank_income/get`` request options."""

    count: Optional[int] = UNSET
    """How many Bank Income Reports should be fetched. Multiple reports may be available if the report has been
    re-created or refreshed. If more than one report is available, the most recent reports will be returned first."""


class CreditBankIncomeGetRequestOptionsDict(TypedDict):
    count: NotRequired[int]
