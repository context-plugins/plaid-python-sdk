from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetHoldingRestrictedIndicator(str, Enum):
    """Whether or not the stock is restricted, i.e. "Restricted" or "Not Restricted"
    """

    YES = "Yes"
    NO = "No"

    __str__ = str.__str__


AssetHoldingRestrictedIndicatorOrStr: TypeAlias = Annotated[
    AssetHoldingRestrictedIndicator | str, open_enum_validator(AssetHoldingRestrictedIndicator)
]
