from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class IncomeVerificationPrecheckPayrollInstitution(SdkBaseModel):
    """Information about the end user's payroll institution"""

    name: OptionalNullable[str] = UNSET
    """The name of payroll institution"""


class IncomeVerificationPrecheckPayrollInstitutionDict(TypedDict):
    name: NotRequired[str | None]
