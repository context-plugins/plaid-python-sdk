from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SandboxBankTransferFireWebhookRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/bank_transfer/fire_webhook``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    webhook: str
    """The URL to which the webhook should be sent."""


class SandboxBankTransferFireWebhookRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    webhook: str
