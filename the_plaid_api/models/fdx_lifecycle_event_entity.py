from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.fdx_event_status import FdxEventStatusOrStr
from .enums.fdx_update_reason import FdxUpdateReasonOrStr
from .enums.party_type import PartyTypeOrStr


class FdxLifecycleEventEntity(SdkBaseModel):
    """Details of consent or payment network identifier or other entity's revocation request or other lifecycle status
    change event"""

    status: Optional[FdxEventStatusOrStr] = UNSET
    """Current status of indicated entity after reported event change. Not all statuses will be supported on all entity
    types by all data providers"""

    reason: Optional[FdxUpdateReasonOrStr] = UNSET
    """Reason for lifecycle event status change"""

    other_reason: Optional[str] = Field(default=UNSET, alias="otherReason")
    """Additional information or description of an ``OTHER`` reason"""

    initiator: Optional[PartyTypeOrStr] = UNSET
    """Identifies the type of a party"""

    updated_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedTime")
    """ISO 8601 date-time in format 'YYYY-MM-DDThh:mm:ss.nnn[Z|[+|-]hh:mm]' according to `IETF RFC3339
    <https://datatracker.ietf.org/doc/html/rfc3339>`__"""


class FdxLifecycleEventEntityDict(TypedDict):
    status: NotRequired[FdxEventStatusOrStr]
    reason: NotRequired[FdxUpdateReasonOrStr]
    other_reason: NotRequired[str]
    initiator: NotRequired[PartyTypeOrStr]
    updated_time: NotRequired[RFC3339DateTime]
