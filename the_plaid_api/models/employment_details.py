from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .pay import Pay, PayDict


class EmploymentDetails(SdkBaseModel):
    """An object representing employment details found on a paystub."""

    annual_salary: Optional[Pay] = UNSET
    """An object representing a monetary amount."""

    hire_date: OptionalNullable[Date] = UNSET
    """Date on which the employee was hired, in the YYYY-MM-DD format."""


class EmploymentDetailsDict(TypedDict):
    annual_salary: NotRequired[PayDict]
    hire_date: NotRequired[Date | None]
