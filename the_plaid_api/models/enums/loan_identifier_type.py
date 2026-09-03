from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoanIdentifierType(str, Enum):
    """A value from a MISMO prescribed list that specifies the type of loan identifier."""

    LENDER_LOAN = "LenderLoan"
    UNIVERSAL_LOAN = "UniversalLoan"

    __str__ = str.__str__


LoanIdentifierTypeOrStr: TypeAlias = Annotated[LoanIdentifierType | str, open_enum_validator(LoanIdentifierType)]
