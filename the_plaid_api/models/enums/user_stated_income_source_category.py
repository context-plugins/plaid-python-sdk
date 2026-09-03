from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UserStatedIncomeSourceCategory(str, Enum):
    """The income category for a specified income source"""

    OTHER = "OTHER"
    SALARY = "SALARY"
    UNEMPLOYMENT = "UNEMPLOYMENT"
    CASH = "CASH"
    GIG_ECONOMY = "GIG_ECONOMY"
    RENTAL = "RENTAL"
    CHILD_SUPPORT = "CHILD_SUPPORT"
    MILITARY = "MILITARY"
    RETIREMENT = "RETIREMENT"
    LONG_TERM_DISABILITY = "LONG_TERM_DISABILITY"
    BANK_INTEREST = "BANK_INTEREST"

    __str__ = str.__str__


UserStatedIncomeSourceCategoryOrStr: TypeAlias = Annotated[
    UserStatedIncomeSourceCategory | str, open_enum_validator(UserStatedIncomeSourceCategory)
]
