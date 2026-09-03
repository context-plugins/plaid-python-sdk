from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferAuthorizationRiskLevel(str, Enum):
    """Comprises five risk categories (high risk, medium-high risk, medium risk, medium-low risk, low risk) based on the
    probability of return"""

    HIGH_RISK = "HIGH_RISK"
    MEDIUM_HIGH_RISK = "MEDIUM_HIGH_RISK"
    MEDIUM_RISK = "MEDIUM_RISK"
    MEDIUM_LOW_RISK = "MEDIUM_LOW_RISK"
    LOW_RISK = "LOW_RISK"

    __str__ = str.__str__


TransferAuthorizationRiskLevelOrStr: TypeAlias = Annotated[
    TransferAuthorizationRiskLevel | str, open_enum_validator(TransferAuthorizationRiskLevel)
]
