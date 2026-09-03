from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetRetirementIndicator(str, Enum):
    """Whether or not the account is a retirement account (e.g., 401K, 403b, 457, thrift savings plans, traditional and
    Roth, IRAs, SEP-IRA, SIMPLE-IRA, KEOGH, state retirement savings plans, other independent and IRS-qualified employer
    retirement plans)"""

    YES = "Yes"
    NO = "No"

    __str__ = str.__str__


AssetRetirementIndicatorOrStr: TypeAlias = Annotated[
    AssetRetirementIndicator | str, open_enum_validator(AssetRetirementIndicator)
]
