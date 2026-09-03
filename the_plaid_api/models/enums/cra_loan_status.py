from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraLoanStatus(str, Enum):
    """The status of the loan."""

    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    BOOKED = "BOOKED"
    CURRENT = "CURRENT"
    DELINQUENT = "DELINQUENT"
    DEFAULT = "DEFAULT"
    CHARGED_OFF = "CHARGED_OFF"
    TRANSFERRED = "TRANSFERRED"
    PAID_OFF = "PAID_OFF"
    OTHER = "OTHER"

    __str__ = str.__str__


CraLoanStatusOrStr: TypeAlias = Annotated[CraLoanStatus | str, open_enum_validator(CraLoanStatus)]
