from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.webhook_environment_values import WebhookEnvironmentValuesOrStr


class ProtectUserEventWebhook(SdkBaseModel):
    """Fired when there has been a new user event. The webhook payload contains limited information about the event. For
    full event details, call https://plaid.com/docs/api/products/protect/#protecteventget."""

    webhook_type: str
    """``"PROTECT"``"""

    webhook_code: str
    """``PROTECT_USER_EVENT``"""

    event_id: str
    """The event ID of the user event that occurred."""

    event_type: str
    """The type of user event that occurred. Possible values include ``LINK_COMPLETE`` (the Link session has finished
    and a Trust Index score has been computed without waiting for transaction extraction) and ``PROTECT_RUN_FINISH``
    (extraction-required scoring is complete, including transaction extraction; may arrive 30 seconds or more after Link
    completion)."""

    timestamp: RFC3339DateTime
    """The timestamp of the event, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g.
    ``"2017-09-14T14:42:19.350Z"``"""

    user_id: str | None
    """The Plaid User ID."""

    client_user_id: OptionalNullable[str] = UNSET
    """The ``client_user_id`` provided by the client when the user was created via ``/user/create`` or Link."""

    link_session_id: OptionalNullable[str] = UNSET
    """An identifier for the Link session this event occurred in"""

    environment: WebhookEnvironmentValuesOrStr
    """The Plaid environment the webhook was sent from"""


class ProtectUserEventWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    event_id: str
    event_type: str
    timestamp: RFC3339DateTime
    user_id: str | None
    client_user_id: NotRequired[str | None]
    link_session_id: NotRequired[str | None]
    environment: WebhookEnvironmentValuesOrStr
