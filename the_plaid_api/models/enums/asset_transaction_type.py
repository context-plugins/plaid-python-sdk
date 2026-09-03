from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetTransactionType(str, Enum):
    """Asset Transaction Type."""

    CREDIT = "Credit"
    DEBIT = "Debit"

    __str__ = str.__str__


AssetTransactionTypeOrStr: TypeAlias = Annotated[AssetTransactionType | str, open_enum_validator(AssetTransactionType)]
