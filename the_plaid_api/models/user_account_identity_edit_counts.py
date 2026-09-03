from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UserAccountIdentityEditCounts(SdkBaseModel):
    """Edit counts over various time periods."""

    edits_current: Optional[int] = UNSET
    """Number of edits in the current session"""

    edits_1d: Optional[int] = UNSET
    """Number of edits in the last 1 day"""

    edits_30d: Optional[int] = UNSET
    """Number of edits in the last 30 days"""

    edits_365d: Optional[int] = UNSET
    """Number of edits in the last 365 days"""

    edits_all_time: Optional[int] = UNSET
    """Total number of edits"""


class UserAccountIdentityEditCountsDict(TypedDict):
    edits_current: NotRequired[int]
    edits_1d: NotRequired[int]
    edits_30d: NotRequired[int]
    edits_365d: NotRequired[int]
    edits_all_time: NotRequired[int]
