from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_loan_identifiers import CreditFreddieMacLoanIdentifiers, CreditFreddieMacLoanIdentifiersDict


class CreditFreddieMacLoan(SdkBaseModel):
    """Information specific to a mortgage loan agreement between one or more borrowers and a mortgage lender."""

    loan_identifiers: CreditFreddieMacLoanIdentifiers = Field(alias="LOAN_IDENTIFIERS")
    """Collection of current and previous identifiers for this loan."""

    loan_role_type: str = Field(alias="LoanRoleType")
    """Type of loan. The value can only be "SubjectLoan"."""


class CreditFreddieMacLoanDict(TypedDict):
    loan_identifiers: CreditFreddieMacLoanIdentifiers | CreditFreddieMacLoanIdentifiersDict
    loan_role_type: str
