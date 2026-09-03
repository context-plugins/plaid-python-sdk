from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessVerificationStatusRiskCheck(str, Enum):
    """Status of the business risk assessment check"""

    ACTIVE = "active"
    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


BusinessVerificationStatusRiskCheckOrStr: TypeAlias = Annotated[
    BusinessVerificationStatusRiskCheck | str, open_enum_validator(BusinessVerificationStatusRiskCheck)
]
