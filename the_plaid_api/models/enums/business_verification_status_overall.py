from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessVerificationStatusOverall(str, Enum):
    """Status of the overall business verification"""

    ACTIVE = "active"
    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


BusinessVerificationStatusOverallOrStr: TypeAlias = Annotated[
    BusinessVerificationStatusOverall | str, open_enum_validator(BusinessVerificationStatusOverall)
]
