from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.beacon_audit_trail_source import BeaconAuditTrailSourceOrStr


class BeaconAuditTrail(SdkBaseModel):
    """Information about the last change made to the parent object specifying what caused the change as well as when it
    occurred."""

    source: BeaconAuditTrailSourceOrStr
    """A type indicating what caused a resource to be changed or updated.


    ``dashboard`` - The resource was created or updated by a member of your team via the Plaid dashboard.

    ``api`` - The resource was created or updated via the Plaid API.

    ``system`` - The resource was created or updated automatically by a part of the Plaid Beacon system. For example, if
    another business using Plaid Beacon created a fraud report that matched one of your users, your matching user's
    status would automatically be updated and the audit trail source would be ``system``.

    ``bulk_import`` - The resource was created or updated as part of a bulk import process. For example, if your company
    provided a CSV of user data as part of your initial onboarding, the audit trail source would be ``bulk_import``."""

    dashboard_user_id: str | None
    """ID of the associated user. To retrieve the email address or other details of the person corresponding to this ID,
    use ``/dashboard_user/get``."""

    timestamp: RFC3339DateTime
    """An ISO8601 formatted timestamp."""


class BeaconAuditTrailDict(TypedDict):
    source: BeaconAuditTrailSourceOrStr
    dashboard_user_id: str | None
    timestamp: RFC3339DateTime
