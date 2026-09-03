from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.fdx_consent_grant_status import FdxConsentGrantStatusOrStr
from .enums.fdx_update_reason import FdxUpdateReasonOrStr
from .enums.party_type import PartyTypeOrStr


class FdxconsentRevocationRecord(SdkBaseModel):
    """One revocation record on a consent grant, mirroring the FDX ConsentRevocation entity."""

    status: FdxConsentGrantStatusOrStr
    """Current status of a consent grant. One of ``ACTIVE``, ``REVOKED``, ``EXPIRED``."""

    reason: FdxUpdateReasonOrStr
    """Reason for lifecycle event status change"""

    initiator: PartyTypeOrStr
    """Identifies the type of a party"""

    updated_time: RFC3339DateTime = Field(alias="updatedTime")
    """When the consent grant was revoked"""


class FdxconsentRevocationRecordDict(TypedDict):
    status: FdxConsentGrantStatusOrStr
    reason: FdxUpdateReasonOrStr
    initiator: PartyTypeOrStr
    updated_time: RFC3339DateTime
