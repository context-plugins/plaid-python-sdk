from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetReportType(str, Enum):
    """Indicates either a Fast Asset Report, which will contain only current identity and balance information, or a Full
    Asset Report, which will also contain historical balance information and transaction data."""

    FULL = "FULL"
    FAST = "FAST"

    __str__ = str.__str__


AssetReportTypeOrStr: TypeAlias = Annotated[AssetReportType | str, open_enum_validator(AssetReportType)]
