from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdentityVerificationAutofillStatus(str, Enum):
    """A status enum indicating whether autofill succeeded or failed."""

    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


IdentityVerificationAutofillStatusOrStr: TypeAlias = Annotated[
    IdentityVerificationAutofillStatus | str, open_enum_validator(IdentityVerificationAutofillStatus)
]
