from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.link_delivery_session_status import LinkDeliverySessionStatusOrStr


class LinkDeliveryGetResponse(SdkBaseModel):
    """LinkDeliveryGetResponse defines the response schema for ``/link_delivery/get``"""

    status: LinkDeliverySessionStatusOrStr
    """The status of the given Hosted Link session.

    ``CREATED``: The session is created but not yet accessed by the user

    ``OPENED``: The session is opened by the user but not yet completed

    ``EXITED``: The session has been exited by the user

    ``COMPLETED``: The session has been completed by the user

    ``EXPIRED``: The session has expired"""

    created_at: RFC3339DateTime
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (``YYYY-MM-DDTHH:mm:ssZ``) indicating the
    time the given Hosted Link session was created at."""

    completed_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (``YYYY-MM-DDTHH:mm:ssZ``) indicating the
    time the given Hosted Link session was completed at."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    access_tokens: OptionalNullable[list[str]] = UNSET
    """An array of access tokens associated with the Hosted Link session."""

    item_ids: OptionalNullable[list[str]] = UNSET
    """An array of ``item_id``s associated with the Hosted Link session."""


class LinkDeliveryGetResponseDict(TypedDict):
    status: LinkDeliverySessionStatusOrStr
    created_at: RFC3339DateTime
    completed_at: NotRequired[RFC3339DateTime | None]
    request_id: str
    access_tokens: NotRequired[list[str] | None]
    item_ids: NotRequired[list[str] | None]
