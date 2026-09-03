from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetHoldingType(str, Enum):
    """Type of holding (e.g. bond, stock, crypto, other)"""

    BOND = "Bond"
    STOCK = "Stock"
    CRYPTO = "Crypto"
    OTHER = "Other"

    __str__ = str.__str__


AssetHoldingTypeOrStr: TypeAlias = Annotated[AssetHoldingType | str, open_enum_validator(AssetHoldingType)]
