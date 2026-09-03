from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BeaconUserHistoryListRequest(SdkBaseModel):
    """Request input for listing the history of a Beacon User"""

    beacon_user_id: str
    """ID of the associated Beacon User."""

    cursor: OptionalNullable[str] = UNSET
    """An identifier that determines which page of results you receive."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""


class BeaconUserHistoryListRequestDict(TypedDict):
    beacon_user_id: str
    cursor: NotRequired[str | None]
    client_id: NotRequired[str]
    secret: NotRequired[str]
