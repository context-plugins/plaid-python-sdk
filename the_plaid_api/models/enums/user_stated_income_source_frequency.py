from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UserStatedIncomeSourceFrequency(str, Enum):
    """The pay frequency of a specified income source"""

    UNKNOWN = "UNKNOWN"
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    SEMI_MONTHLY = "SEMI_MONTHLY"
    MONTHLY = "MONTHLY"

    __str__ = str.__str__


UserStatedIncomeSourceFrequencyOrStr: TypeAlias = Annotated[
    UserStatedIncomeSourceFrequency | str, open_enum_validator(UserStatedIncomeSourceFrequency)
]
