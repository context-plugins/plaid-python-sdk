from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WebhookVerificationKeyGetRequest(SdkBaseModel):
    """WebhookVerificationKeyGetRequest defines the request schema for ``/webhook_verification_key/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    key_id: str
    """The key ID ( ``kid`` ) from the JWT header."""


class WebhookVerificationKeyGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    key_id: str
