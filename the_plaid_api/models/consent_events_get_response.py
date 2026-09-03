from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .consent_event import ConsentEvent, ConsentEventDict


class ConsentEventsGetResponse(SdkBaseModel):
    """Describes a historical log of item consent events."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    consent_events: list[ConsentEvent]
    """A list of consent events."""


class ConsentEventsGetResponseDict(TypedDict):
    request_id: str
    consent_events: list[ConsentEvent | ConsentEventDict]
