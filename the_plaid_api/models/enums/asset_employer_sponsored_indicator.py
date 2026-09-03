from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetEmployerSponsoredIndicator(str, Enum):
    """Whether the account is employer sponsored retirement account or not (e.g., 401K, 403b, 457, thrift savings
    plan)"""

    YES = "Yes"
    NO = "No"

    __str__ = str.__str__


AssetEmployerSponsoredIndicatorOrStr: TypeAlias = Annotated[
    AssetEmployerSponsoredIndicator | str, open_enum_validator(AssetEmployerSponsoredIndicator)
]
