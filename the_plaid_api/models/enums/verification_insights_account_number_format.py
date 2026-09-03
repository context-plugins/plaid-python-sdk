from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationInsightsAccountNumberFormat(str, Enum):
    """Indicator of account number format validity for institution.

    ``valid``: indicates that the account number has a correct format for the institution.

    ``invalid``: indicates that the account number has an incorrect format for the institution.

    ``unknown``: indicates that there was not enough information to determine whether the format is correct for the
    institution."""

    VALID = "valid"
    INVALID = "invalid"
    UNKNOWN = "unknown"

    __str__ = str.__str__


VerificationInsightsAccountNumberFormatOrStr: TypeAlias = Annotated[
    VerificationInsightsAccountNumberFormat | str, open_enum_validator(VerificationInsightsAccountNumberFormat)
]
