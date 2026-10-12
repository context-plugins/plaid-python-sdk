from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .employer_verification import EmployerVerification, EmployerVerificationDict
from .enums.employment_verification_status import EmploymentVerificationStatusOrStr
from .platform_ids import PlatformIds, PlatformIdsDict


class EmploymentVerification(SdkBaseModel):
    """An object containing proof of employment data for an individual"""

    status: OptionalNullable[EmploymentVerificationStatusOrStr] = UNSET
    """Current employment status."""

    start_date: OptionalNullable[Date] = UNSET
    """Start of employment in ISO 8601 format (YYYY-MM-DD)."""

    end_date: OptionalNullable[Date] = UNSET
    """End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD)."""

    employer: Optional[EmployerVerification] = UNSET
    """An object containing employer data."""

    title: OptionalNullable[str] = UNSET
    """Current title of employee."""

    platform_ids: Optional[PlatformIds] = UNSET
    """An object containing a set of ids related to an employee"""


class EmploymentVerificationDict(TypedDict):
    status: NotRequired[EmploymentVerificationStatusOrStr | None]
    start_date: NotRequired[Date | None]
    end_date: NotRequired[Date | None]
    employer: NotRequired[EmployerVerificationDict]
    title: NotRequired[str | None]
    platform_ids: NotRequired[PlatformIdsDict]
