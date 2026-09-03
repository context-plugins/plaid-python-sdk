from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_loan_closed_status import CraLoanClosedStatus, CraLoanClosedStatusDict


class CraLoanUnregister(SdkBaseModel):
    """Contains loan data for the loan being unregistered."""

    loan_id: str
    """A unique identifier for the loan. Personally identifiable information, such as an email address or phone number,
    should not be used in the ``loan_id``."""

    closed_with_status: CraLoanClosedStatus
    """Contains the status and date information of the loan when unregistering."""


class CraLoanUnregisterDict(TypedDict):
    loan_id: str
    closed_with_status: CraLoanClosedStatus | CraLoanClosedStatusDict
