from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxBankTransferFireWebhookResponse(SdkBaseModel):
    """Defines the response schema for ``/sandbox/bank_transfer/fire_webhook``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxBankTransferFireWebhookResponseDict(TypedDict):
    request_id: str
