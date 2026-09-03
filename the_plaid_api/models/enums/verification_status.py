from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationStatus(str, Enum):
    """The verification status. One of the following:

    ``"VERIFIED"``: The information was successfully verified.

    ``"UNVERIFIED"``: The verification has not yet been performed.

    ``"NEEDS_INFO"``: The verification was attempted but could not be completed due to missing information.

    "``UNABLE_TO_VERIFY``": The verification was performed and the information could not be verified.

    ``"UNKNOWN"``: The verification status is unknown."""

    VERIFIED = "VERIFIED"
    UNVERIFIED = "UNVERIFIED"
    NEEDS_INFO = "NEEDS_INFO"
    UNABLE_TO_VERIFY = "UNABLE_TO_VERIFY"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


VerificationStatusOrStr: TypeAlias = Annotated[VerificationStatus | str, open_enum_validator(VerificationStatus)]
