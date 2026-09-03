from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_card_liability import CreditCardLiability, CreditCardLiabilityDict
from .mortgage_liability import MortgageLiability, MortgageLiabilityDict
from .student_loan import StudentLoan, StudentLoanDict


class LiabilitiesObject(SdkBaseModel):
    """An object containing liability accounts"""

    credit: list[CreditCardLiability | None]
    """The credit accounts returned."""

    mortgage: list[MortgageLiability | None]
    """The mortgage accounts returned."""

    student: list[StudentLoan | None]
    """The student loan accounts returned."""


class LiabilitiesObjectDict(TypedDict):
    credit: list[CreditCardLiability | CreditCardLiabilityDict | None]
    mortgage: list[MortgageLiability | MortgageLiabilityDict | None]
    student: list[StudentLoan | StudentLoanDict | None]
