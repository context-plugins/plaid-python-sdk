from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FdxConsentGrantStatus(str, Enum):
    """Current status of a consent grant. One of ``ACTIVE``, ``REVOKED``, ``EXPIRED``."""

    ACTIVE = "ACTIVE"
    REVOKED = "REVOKED"
    EXPIRED = "EXPIRED"

    __str__ = str.__str__


FdxConsentGrantStatusOrStr: TypeAlias = Annotated[
    FdxConsentGrantStatus | str, open_enum_validator(FdxConsentGrantStatus)
]
