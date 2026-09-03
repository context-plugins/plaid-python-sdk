from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UserStatedIncomeSourcePayType(str, Enum):
    """The pay type - ``GROSS``, ``NET``, or ``UNKNOWN`` for a specified income source"""

    UNKNOWN = "UNKNOWN"
    GROSS = "GROSS"
    NET = "NET"

    __str__ = str.__str__


UserStatedIncomeSourcePayTypeOrStr: TypeAlias = Annotated[
    UserStatedIncomeSourcePayType | str, open_enum_validator(UserStatedIncomeSourcePayType)
]
