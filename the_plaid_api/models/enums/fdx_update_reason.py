from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FdxUpdateReason(str, Enum):
    """Reason for lifecycle event status change"""

    BUSINESS_RULE = "BUSINESS_RULE"
    SECURITY_EVENT = "SECURITY_EVENT"
    USER_ACTION = "USER_ACTION"
    OTHER = "OTHER"

    __str__ = str.__str__


FdxUpdateReasonOrStr: TypeAlias = Annotated[FdxUpdateReason | str, open_enum_validator(FdxUpdateReason)]
