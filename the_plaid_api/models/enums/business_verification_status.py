from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessVerificationStatus(str, Enum):
    """Status of the KYB (Know Your Business) identity assessment check"""

    ACTIVE = "active"
    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


BusinessVerificationStatusOrStr: TypeAlias = Annotated[
    BusinessVerificationStatus | str, open_enum_validator(BusinessVerificationStatus)
]
