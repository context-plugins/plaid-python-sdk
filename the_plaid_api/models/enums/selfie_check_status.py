from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SelfieCheckStatus(str, Enum):
    """The outcome status for the associated Identity Verification attempt's ``selfie_check`` step. This field will
    always have the same value as ``steps.selfie_check``."""

    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


SelfieCheckStatusOrStr: TypeAlias = Annotated[SelfieCheckStatus | str, open_enum_validator(SelfieCheckStatus)]
