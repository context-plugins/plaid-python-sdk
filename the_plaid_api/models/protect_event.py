from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ProtectEvent(SdkBaseModel):
    """Event data for Protect events."""

    timestamp: RFC3339DateTime
    """The timestamp of the event, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g.
    ``"2017-09-14T14:42:19.350Z"``"""

    protect_session_id: Optional[str] = UNSET
    """If present, contains the current Protect Session ID from the Protect SDK."""

    app_visit: OptionalNullable[Any] = UNSET
    """This event type represents a user visiting the client application."""

    user_sign_in: OptionalNullable[Any] = UNSET
    """This event type represents a user signing in to the application."""

    user_sign_up: OptionalNullable[Any] = UNSET
    """This event type represents a user signing up for the application."""


class ProtectEventDict(TypedDict):
    timestamp: RFC3339DateTime
    protect_session_id: NotRequired[str]
    app_visit: NotRequired[Any | None]
    user_sign_in: NotRequired[Any | None]
    user_sign_up: NotRequired[Any | None]
