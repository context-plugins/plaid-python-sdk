from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditBankIncomeRefreshResponse(SdkBaseModel):
    """CreditBankIncomeRefreshResponse defines the response schema for ``/credit/bank_income/refresh``."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditBankIncomeRefreshResponseDict(TypedDict):
    request_id: str
