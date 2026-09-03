from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerifySmsdetailsStatus(str, Enum):
    """The outcome status for the associated Identity Verification attempt's ``verify_sms`` step. This field will always
    have the same value as ``steps.verify_sms``."""

    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


VerifySmsdetailsStatusOrStr: TypeAlias = Annotated[
    VerifySmsdetailsStatus | str, open_enum_validator(VerifySmsdetailsStatus)
]
