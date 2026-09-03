from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConsentEventCode(str, Enum):
    """Codes describing the object of a consent event."""

    USER_AGREEMENT = "USER_AGREEMENT"
    USE_CASES = "USE_CASES"
    DATA_SCOPES = "DATA_SCOPES"
    ACCOUNT_SCOPES = "ACCOUNT_SCOPES"
    REVOCATION = "REVOCATION"

    __str__ = str.__str__


ConsentEventCodeOrStr: TypeAlias = Annotated[ConsentEventCode | str, open_enum_validator(ConsentEventCode)]
