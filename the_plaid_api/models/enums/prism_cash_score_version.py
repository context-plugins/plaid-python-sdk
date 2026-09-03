from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrismCashScoreVersion(str, Enum):
    """The version of Prism CashScore. If not specified, will default to v3."""

    _4_1 = "4.1"
    """The ``4.1`` Prism CashScore version."""

    _4 = "4"
    """The ``4`` Prism CashScore version."""

    _3_LITE = "3_lite"
    """The ``3_lite`` Prism CashScore version."""

    _3 = "3"
    """The ``3`` Prism CashScore version."""

    __str__ = str.__str__


PrismCashScoreVersionOrStr: TypeAlias = Annotated[
    PrismCashScoreVersion | str, open_enum_validator(PrismCashScoreVersion)
]
