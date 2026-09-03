from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProtectEventGetRequest(SdkBaseModel):
    """Request object for /protect/event/get"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    event_id: str
    """The event ID to retrieve information for."""


class ProtectEventGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    event_id: str
