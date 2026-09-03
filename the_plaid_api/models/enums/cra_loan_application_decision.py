from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraLoanApplicationDecision(str, Enum):
    """The decision of the loan application."""

    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    OTHER = "OTHER"

    __str__ = str.__str__


CraLoanApplicationDecisionOrStr: TypeAlias = Annotated[
    CraLoanApplicationDecision | str, open_enum_validator(CraLoanApplicationDecision)
]
