from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SellType(str, Enum):
    """Selling an investment"""

    DISTRIBUTION = "distribution"
    EXERCISE = "exercise"
    SELL = "sell"
    SELL_SHORT = "sell short"

    __str__ = str.__str__


SellTypeOrStr: TypeAlias = Annotated[SellType | str, open_enum_validator(SellType)]
