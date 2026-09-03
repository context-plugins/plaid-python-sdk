from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConsentEventType(str, Enum):
    """A broad categorization of the consent event."""

    CONSENT_GRANTED = "CONSENT_GRANTED"
    CONSENT_REVOKED = "CONSENT_REVOKED"
    CONSENT_UPDATED = "CONSENT_UPDATED"

    __str__ = str.__str__


ConsentEventTypeOrStr: TypeAlias = Annotated[ConsentEventType | str, open_enum_validator(ConsentEventType)]
