from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .protect_event import ProtectEvent, ProtectEventDict


class ProtectEventSendRequest(SdkBaseModel):
    """Request object for /protect/event/send"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    timestamp: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the event. Might be the current moment or a time in the past. In `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g. ``"2017-09-14T14:42:19.350Z"``"""

    event: ProtectEvent | None
    """Event data for Protect events."""

    protect_session_id: Optional[str] = UNSET
    """Protect Session ID should be provided for any event correlated with a frontend user session started via the
    Protect SDK."""

    request_trust_index: Optional[bool] = UNSET
    """Whether this event should be scored with Trust Index. The default is false."""


class ProtectEventSendRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    timestamp: NotRequired[RFC3339DateTime]
    event: ProtectEventDict | None
    protect_session_id: NotRequired[str]
    request_trust_index: NotRequired[bool]
