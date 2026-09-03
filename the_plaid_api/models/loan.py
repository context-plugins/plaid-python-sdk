from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .loan_identifiers import LoanIdentifiers, LoanIdentifiersDict


class Loan(SdkBaseModel):
    """Information specific to a mortgage loan agreement between one or more borrowers and a mortgage lender."""

    loan_identifiers: LoanIdentifiers = Field(alias="LOAN_IDENTIFIERS")
    """Collection of current and previous identifiers for this loan."""


class LoanDict(TypedDict):
    loan_identifiers: LoanIdentifiers | LoanIdentifiersDict
