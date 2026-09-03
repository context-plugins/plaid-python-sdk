from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .protect_incident_amount import ProtectIncidentAmount, ProtectIncidentAmountDict


class ProtectIncidentEventResponse(SdkBaseModel):
    """Details about the incident event."""

    protect_event_id: OptionalNullable[str] = UNSET
    """A globally unique identifier representing a Protect event that may be associated with this incident."""

    link_session_id: OptionalNullable[str] = UNSET
    """A unique identifier for a Link session that may be associated with this incident."""

    idv_session_id: OptionalNullable[str] = UNSET
    """A unique identifier for an Identity Verification session that may be associated with this incident."""

    signal_client_transaction_id: OptionalNullable[str] = UNSET
    """The unique ID used to refer to a Signal transaction evaluation that may be associated with this incident."""

    internal_reference: OptionalNullable[str] = UNSET
    """A unique ID representing the incident in your system. Personally identifiable information, such as an email
    address or phone number, should not be used in this field."""

    time: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp when the incident occurred, in ISO 8601 format (e.g., '2020-07-24T03:26:02Z')."""

    amount: OptionalNullable[ProtectIncidentAmount] = UNSET
    """The monetary amount associated with the incident."""

    item_id: OptionalNullable[str] = UNSET
    """The ``item_id`` associated with the Item related to this incident."""


class ProtectIncidentEventResponseDict(TypedDict):
    protect_event_id: NotRequired[str | None]
    link_session_id: NotRequired[str | None]
    idv_session_id: NotRequired[str | None]
    signal_client_transaction_id: NotRequired[str | None]
    internal_reference: NotRequired[str | None]
    time: NotRequired[RFC3339DateTime | None]
    amount: NotRequired[ProtectIncidentAmount | ProtectIncidentAmountDict | None]
    item_id: NotRequired[str | None]
