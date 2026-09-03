from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .trust_index import TrustIndex, TrustIndexDict


class ProtectEventGetResponse(SdkBaseModel):
    """Response object for /protect/event/get"""

    event_id: str
    """The event ID."""

    timestamp: RFC3339DateTime
    """The timestamp of the event, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g.
    ``"2017-09-14T14:42:19.350Z"``"""

    trust_index: OptionalNullable[TrustIndex] = UNSET
    """Represents a calculated Trust Index Score."""

    fraud_attributes: OptionalNullable[Any] = UNSET
    """Event fraud attributes as an arbitrary set of key-value pairs. The set of attributes returned varies by model."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProtectEventGetResponseDict(TypedDict):
    event_id: str
    timestamp: RFC3339DateTime
    trust_index: NotRequired[TrustIndex | TrustIndexDict | None]
    fraud_attributes: NotRequired[Any | None]
    request_id: str
