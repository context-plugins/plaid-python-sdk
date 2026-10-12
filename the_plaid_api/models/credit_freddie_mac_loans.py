from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_freddie_mac_loan import CreditFreddieMacLoan, CreditFreddieMacLoanDict


class CreditFreddieMacLoans(SdkBaseModel):
    """A collection of loans that are part of a single deal."""

    loan: CreditFreddieMacLoan = Field(alias="LOAN")
    """Information specific to a mortgage loan agreement between one or more borrowers and a mortgage lender."""


class CreditFreddieMacLoansDict(TypedDict):
    loan: CreditFreddieMacLoanDict
