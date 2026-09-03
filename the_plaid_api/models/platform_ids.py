from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PlatformIds(SdkBaseModel):
    """An object containing a set of ids related to an employee"""

    employee_id: OptionalNullable[str] = UNSET
    """The ID of an employee as given by their employer"""

    payroll_id: OptionalNullable[str] = UNSET
    """The ID of an employee as given by their payroll"""

    position_id: OptionalNullable[str] = UNSET
    """The ID of the position of the employee"""


class PlatformIdsDict(TypedDict):
    employee_id: NotRequired[str | None]
    payroll_id: NotRequired[str | None]
    position_id: NotRequired[str | None]
