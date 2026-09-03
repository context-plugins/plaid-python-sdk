from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TransferGetRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    transfer_id: Optional[str] = UNSET
    """Plaid's unique identifier for a transfer."""

    authorization_id: Optional[str] = UNSET
    """Plaid's unique identifier for a transfer authorization."""

    originator_client_id: OptionalNullable[str] = UNSET
    """The Plaid client ID of the transfer originator. Should only be present if ``client_id`` is a third-party sender
    (TPS)."""


class TransferGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    transfer_id: NotRequired[str]
    authorization_id: NotRequired[str]
    originator_client_id: NotRequired[str | None]
