from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditPlatformIds(SdkBaseModel):
    """The object containing a set of ids related to an employee."""

    employee_id: str | None
    """The ID of an employee as given by their employer."""

    payroll_id: str | None
    """The ID of an employee as given by their payroll."""

    position_id: str | None
    """The ID of the position of the employee."""


class CreditPlatformIdsDict(TypedDict):
    employee_id: str | None
    payroll_id: str | None
    position_id: str | None
