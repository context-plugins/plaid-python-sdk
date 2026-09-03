from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .loan_identifier import LoanIdentifier, LoanIdentifierDict


class CreditFreddieMacLoanIdentifiers(SdkBaseModel):
    """Collection of current and previous identifiers for this loan."""

    loan_identifier: list[LoanIdentifier] = Field(alias="LOAN_IDENTIFIER")


class CreditFreddieMacLoanIdentifiersDict(TypedDict):
    loan_identifier: list[LoanIdentifier | LoanIdentifierDict]
