from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.fdx_update_reason import FdxUpdateReasonOrStr
from .enums.party_type import PartyTypeOrStr


class FdxconsentRevocation(SdkBaseModel):
    """Request body for PUT /fdx/consents/{consentId}/revocation."""

    initiator: PartyTypeOrStr
    """Identifies the type of a party"""

    reason: FdxUpdateReasonOrStr
    """Reason for lifecycle event status change"""

    other_reason: Optional[str] = Field(default=UNSET, alias="otherReason")
    """Additional information or description of an ``OTHER`` reason"""

    updated_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedTime")
    """When the revocation was effected on the initiator's side"""


class FdxconsentRevocationDict(TypedDict):
    initiator: PartyTypeOrStr
    reason: FdxUpdateReasonOrStr
    other_reason: NotRequired[str]
    updated_time: NotRequired[RFC3339DateTime]
