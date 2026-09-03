from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskCheckBehaviorBotDetectedLabel(str, Enum):
    """Field describing the outcome of a bot detection behavior risk check.

    ``yes`` indicates that automated activity was detected.

    ``no`` indicates that automated activity was not detected.

    ``no_data`` indicates there was not enough information available to give an accurate signal."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskCheckBehaviorBotDetectedLabelOrStr: TypeAlias = Annotated[
    RiskCheckBehaviorBotDetectedLabel | str, open_enum_validator(RiskCheckBehaviorBotDetectedLabel)
]
