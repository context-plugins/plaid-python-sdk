from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraBankIncomeBonusType(str, Enum):
    """The type of bonus that this transaction represents, if it is a bonus. ``BONUS_INCLUDED``: Bonus is included in
    this transaction along with the normal pay ``BONUS_ONLY``: This transaction is a standalone bonus"""

    BONUS_INCLUDED = "BONUS_INCLUDED"
    BONUS_ONLY = "BONUS_ONLY"

    __str__ = str.__str__


CraBankIncomeBonusTypeOrStr: TypeAlias = Annotated[
    CraBankIncomeBonusType | str, open_enum_validator(CraBankIncomeBonusType)
]
