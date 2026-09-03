from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditBankIncomeWebhookUpdateResponse(SdkBaseModel):
    """CreditBankIncomeWebhookUpdateResponse defines the response schema for ``/credit/bank_income/webhook/update``."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditBankIncomeWebhookUpdateResponseDict(TypedDict):
    request_id: str
