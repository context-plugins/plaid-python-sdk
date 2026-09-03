from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .loan import Loan, LoanDict


class Loans(SdkBaseModel):
    """A collection of loans that are part of a single deal."""

    loan: Loan = Field(alias="LOAN")
    """Information specific to a mortgage loan agreement between one or more borrowers and a mortgage lender."""


class LoansDict(TypedDict):
    loan: Loan | LoanDict
