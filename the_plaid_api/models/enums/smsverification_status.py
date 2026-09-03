from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SmsverificationStatus(str, Enum):
    """The outcome status for the individual SMS verification."""

    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELED = "canceled"

    __str__ = str.__str__


SmsverificationStatusOrStr: TypeAlias = Annotated[
    SmsverificationStatus | str, open_enum_validator(SmsverificationStatus)
]
