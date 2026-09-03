from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BuyType(str, Enum):
    """Buying an investment"""

    ASSIGNMENT = "assignment"
    CONTRIBUTION = "contribution"
    BUY = "buy"
    BUY_TO_COVER = "buy to cover"
    DIVIDEND_REINVESTMENT = "dividend reinvestment"
    INTEREST_REINVESTMENT = "interest reinvestment"
    LONG_TERM_CAPITAL_GAIN_REINVESTMENT = "long-term capital gain reinvestment"
    SHORT_TERM_CAPITAL_GAIN_REINVESTMENT = "short-term capital gain reinvestment"

    __str__ = str.__str__


BuyTypeOrStr: TypeAlias = Annotated[BuyType | str, open_enum_validator(BuyType)]
