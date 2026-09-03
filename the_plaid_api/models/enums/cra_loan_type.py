from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraLoanType(str, Enum):
    """The type of loan the user applied for."""

    PERSONAL = "PERSONAL"
    CREDIT_CARD = "CREDIT_CARD"
    BUSINESS = "BUSINESS"
    MORTGAGE = "MORTGAGE"
    AUTO = "AUTO"
    PAYDAY = "PAYDAY"
    STUDENT = "STUDENT"
    HOME_EQUITY = "HOME_EQUITY"
    OTHER = "OTHER"

    __str__ = str.__str__


CraLoanTypeOrStr: TypeAlias = Annotated[CraLoanType | str, open_enum_validator(CraLoanType)]
