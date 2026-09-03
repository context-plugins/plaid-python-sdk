from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class Pslfstatus(SdkBaseModel):
    """Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned
    if the institution is FedLoan (``ins_116527``). Since FedLoan no longer services student loans, this field is no
    longer returned."""

    estimated_eligibility_date: Date | None
    """The estimated date borrower will have completed 120 qualifying monthly payments. Returned in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    payments_made: int | None
    """The number of qualifying payments that have been made."""

    payments_remaining: int | None
    """The number of qualifying payments remaining."""


class PslfstatusDict(TypedDict):
    estimated_eligibility_date: Date | None
    payments_made: int | None
    payments_remaining: int | None
