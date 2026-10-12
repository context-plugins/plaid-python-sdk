from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .user_account_session_event import UserAccountSessionEvent, UserAccountSessionEventDict


class UserAccountSessionEventSendRequest(SdkBaseModel):
    """UserAccountSessionEventSendRequest defines the request schema for ``/user_account/session/event/send``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    cohort_id: Optional[str] = UNSET
    """Optional cohort identifier for the user session."""

    link_session_id: str
    """The Link session identifier."""

    event: UserAccountSessionEvent
    """Event data for user account session tracking"""


class UserAccountSessionEventSendRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    cohort_id: NotRequired[str]
    link_session_id: str
    event: UserAccountSessionEventDict
