from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .trust_index import TrustIndex, TrustIndexDict


class ProtectEventSendResponse(SdkBaseModel):
    """Response object for /protect/event/send"""

    event_id: str
    """The id of the recorded event."""

    trust_index: OptionalNullable[TrustIndex] = UNSET
    """Represents a calculated Trust Index Score."""

    fraud_attributes: OptionalNullable[Any] = UNSET
    """Event fraud attributes as an arbitrary set of key-value pairs. The set of attributes returned varies by model."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProtectEventSendResponseDict(TypedDict):
    event_id: str
    trust_index: NotRequired[TrustIndex | TrustIndexDict | None]
    fraud_attributes: NotRequired[Any | None]
    request_id: str
