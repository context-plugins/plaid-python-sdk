from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetReportAddOns(str, Enum):
    """Add-ons that should be included in the Asset Report.

    ``investments``: The Investments add-on ``fast_assets``: The Fast Assets add-on"""

    INVESTMENTS = "investments"
    FAST_ASSETS = "fast_assets"

    __str__ = str.__str__


AssetReportAddOnsOrStr: TypeAlias = Annotated[AssetReportAddOns | str, open_enum_validator(AssetReportAddOns)]
