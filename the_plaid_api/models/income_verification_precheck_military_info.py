from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class IncomeVerificationPrecheckMilitaryInfo(SdkBaseModel):
    """Data about military info in the income verification precheck."""

    is_active_duty: OptionalNullable[bool] = UNSET
    """Is the user currently active duty in the US military"""

    branch: OptionalNullable[str] = UNSET
    """If the user is currently serving in the US military, the branch of the military in which they are serving Valid
    values: 'AIR FORCE', 'ARMY', 'COAST GUARD', 'MARINES', 'NAVY', 'UNKNOWN'"""


class IncomeVerificationPrecheckMilitaryInfoDict(TypedDict):
    is_active_duty: NotRequired[bool | None]
    branch: NotRequired[str | None]
