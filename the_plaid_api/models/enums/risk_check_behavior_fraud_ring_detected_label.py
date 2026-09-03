from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskCheckBehaviorFraudRingDetectedLabel(str, Enum):
    """Field describing the outcome of a fraud ring behavior risk check.

    ``yes`` indicates that fraud ring activity was detected.

    ``no`` indicates that fraud ring activity was not detected.

    ``no_data`` indicates there was not enough information available to give an accurate signal."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskCheckBehaviorFraudRingDetectedLabelOrStr: TypeAlias = Annotated[
    RiskCheckBehaviorFraudRingDetectedLabel | str, open_enum_validator(RiskCheckBehaviorFraudRingDetectedLabel)
]
