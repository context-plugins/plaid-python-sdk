from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditPayStubPayBasisType(str, Enum):
    """The explicit pay basis on the paystub (if present)."""

    SALARY = "SALARY"
    HOURLY = "HOURLY"
    COMMISSION = "COMMISSION"

    __str__ = str.__str__


CreditPayStubPayBasisTypeOrStr: TypeAlias = Annotated[
    CreditPayStubPayBasisType | str, open_enum_validator(CreditPayStubPayBasisType)
]
