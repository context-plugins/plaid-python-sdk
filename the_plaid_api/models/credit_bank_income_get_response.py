from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .credit_bank_income import CreditBankIncome, CreditBankIncomeDict


class CreditBankIncomeGetResponse(SdkBaseModel):
    """CreditBankIncomeGetResponse defines the response schema for ``/credit/bank_income/get``"""

    bank_income: Optional[list[CreditBankIncome]] = UNSET
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditBankIncomeGetResponseDict(TypedDict):
    bank_income: NotRequired[list[CreditBankIncomeDict]]
    request_id: str
