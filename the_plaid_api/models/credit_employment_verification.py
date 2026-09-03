from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .credit_employer_verification import CreditEmployerVerification, CreditEmployerVerificationDict
from .credit_platform_ids import CreditPlatformIds, CreditPlatformIdsDict


class CreditEmploymentVerification(SdkBaseModel):
    """The object containing proof of employment data for an individual."""

    account_id: str | None
    """ID of the payroll provider account."""

    status: str | None
    """Current employment status."""

    start_date: Date | None
    """Start of employment in ISO 8601 format (YYYY-MM-DD)."""

    end_date: Date | None
    """End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD)."""

    employer: CreditEmployerVerification
    """An object containing employer data."""

    title: str | None
    """Current title of employee."""

    platform_ids: CreditPlatformIds
    """The object containing a set of ids related to an employee."""

    employee_type: str | None
    """The type of employment for the individual. ``"FULL_TIME"``: A full-time employee. ``"PART_TIME"``: A part-time
    employee. ``"CONTRACTOR"``: An employee typically hired externally through a contracting group. ``"TEMPORARY"``: A
    temporary employee. ``"OTHER"``: The employee type is not one of the above defined types."""

    last_paystub_date: Date | None
    """The date of the employee's most recent paystub in ISO 8601 format (YYYY-MM-DD)."""


class CreditEmploymentVerificationDict(TypedDict):
    account_id: str | None
    status: str | None
    start_date: Date | None
    end_date: Date | None
    employer: CreditEmployerVerification | CreditEmployerVerificationDict
    title: str | None
    platform_ids: CreditPlatformIds | CreditPlatformIdsDict
    employee_type: str | None
    last_paystub_date: Date | None
