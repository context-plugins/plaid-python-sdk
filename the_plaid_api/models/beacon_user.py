from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .beacon_audit_trail import BeaconAuditTrail, BeaconAuditTrailDict
from .beacon_user_data import BeaconUserData, BeaconUserDataDict
from .enums.beacon_user_status import BeaconUserStatusOrStr


class BeaconUser(SdkBaseModel):
    """A Beacon User represents an end user that has been scanned against the Beacon Network."""

    item_ids: list[str]
    """An array of Plaid Item IDs corresponding to the Accounts associated with this Beacon User."""

    id: str
    """ID of the associated Beacon User."""

    version: int
    """The ``version`` field begins with 1 and increments each time the user is updated."""

    created_at: RFC3339DateTime
    """An ISO8601 formatted timestamp."""

    updated_at: RFC3339DateTime
    """An ISO8601 formatted timestamp. This field indicates the last time the resource was modified."""

    status: BeaconUserStatusOrStr
    """A status of a Beacon User.

    ``rejected``: The Beacon User has been rejected for fraud. Users can be automatically or manually rejected.

    ``pending_review``: The Beacon User has been marked for review.

    ``cleared``: The Beacon User has been cleared of fraud."""

    program_id: str
    """ID of the associated Beacon Program."""

    client_user_id: str
    """A unique ID that identifies the end user in your system. Either a ``user_id`` or the ``client_user_id`` must be
    provided. This ID can also be used to associate user-specific data from other Plaid products. Financial Account
    Matching requires this field and the ``/link/token/create`` ``client_user_id`` to be consistent. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``."""

    user: BeaconUserData
    """A Beacon User's data and resulting analysis when checked against duplicate records and the Beacon Fraud
    Network."""

    audit_trail: BeaconAuditTrail
    """Information about the last change made to the parent object specifying what caused the change as well as when it
    occurred."""


class BeaconUserDict(TypedDict):
    item_ids: list[str]
    id: str
    version: int
    created_at: RFC3339DateTime
    updated_at: RFC3339DateTime
    status: BeaconUserStatusOrStr
    program_id: str
    client_user_id: str
    user: BeaconUserData | BeaconUserDataDict
    audit_trail: BeaconAuditTrail | BeaconAuditTrailDict
