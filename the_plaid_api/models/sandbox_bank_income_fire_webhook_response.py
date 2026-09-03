from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxBankIncomeFireWebhookResponse(SdkBaseModel):
    """SandboxBankIncomeFireWebhookResponse defines the response schema for ``/sandbox/bank_income/fire_webhook``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxBankIncomeFireWebhookResponseDict(TypedDict):
    request_id: str
