from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomeBreakdownType(str, Enum):
    """The type of income. Possible values include:
      ``"regular"``: regular income
      ``"overtime"``: overtime income
      ``"bonus"``: bonus income"""

    BONUS = "bonus"
    OVERTIME = "overtime"
    REGULAR = "regular"

    __str__ = str.__str__


IncomeBreakdownTypeOrStr: TypeAlias = Annotated[IncomeBreakdownType | str, open_enum_validator(IncomeBreakdownType)]
