from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .loan_identifier import LoanIdentifier, LoanIdentifierDict


class LoanIdentifiers(SdkBaseModel):
    """Collection of current and previous identifiers for this loan."""

    loan_identifier: LoanIdentifier = Field(alias="LOAN_IDENTIFIER")
    """The information used to identify this loan by various parties to the transaction or other organizations."""


class LoanIdentifiersDict(TypedDict):
    loan_identifier: LoanIdentifier | LoanIdentifierDict
