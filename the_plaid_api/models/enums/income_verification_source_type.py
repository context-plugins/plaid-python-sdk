from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomeVerificationSourceType(str, Enum):
    """The types of source income data that users should be able to share"""

    BANK = "bank"
    PAYROLL = "payroll"

    __str__ = str.__str__


IncomeVerificationSourceTypeOrStr: TypeAlias = Annotated[
    IncomeVerificationSourceType | str, open_enum_validator(IncomeVerificationSourceType)
]
