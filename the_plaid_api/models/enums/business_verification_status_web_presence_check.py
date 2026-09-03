from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessVerificationStatusWebPresenceCheck(str, Enum):
    """Status of the digital presence check"""

    ACTIVE = "active"
    SUCCESS = "success"
    FAILED = "failed"
    NOT_APPLICABLE = "not_applicable"

    __str__ = str.__str__


BusinessVerificationStatusWebPresenceCheckOrStr: TypeAlias = Annotated[
    BusinessVerificationStatusWebPresenceCheck | str, open_enum_validator(BusinessVerificationStatusWebPresenceCheck)
]
