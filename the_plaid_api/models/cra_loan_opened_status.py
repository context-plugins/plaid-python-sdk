from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .enums.cra_loan_status import CraLoanStatusOrStr


class CraLoanOpenedStatus(SdkBaseModel):
    """Contains the status and date information of the loan when registering."""

    status: CraLoanStatusOrStr
    """The status of the loan."""

    date: Date
    """The effective date for the status of the loan. The date should be in ISO 8601 format (YYYY-MM-DD)."""


class CraLoanOpenedStatusDict(TypedDict):
    status: CraLoanStatusOrStr
    date: Date
