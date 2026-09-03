from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditSessionBankEmploymentStatus(str, Enum):
    """Status of the Bank Employment Link session.

    ``APPROVED``: User has approved and verified their employment.

    ``NO_EMPLOYERS_FOUND``: We attempted, but were unable to find any employment in the connected account.

    ``EMPLOYER_NOT_LISTED``: The user explicitly indicated that they did not see their current or previous employer in
    the list of employer names found.

    ``STARTED``: The user began the bank employment portion of the link flow.

    ``INTERNAL_ERROR``: The user encountered an internal error."""

    APPROVED = "APPROVED"
    NO_EMPLOYERS_FOUND = "NO_EMPLOYERS_FOUND"
    EMPLOYER_NOT_LISTED = "EMPLOYER_NOT_LISTED"
    STARTED = "STARTED"
    INTERNAL_ERROR = "INTERNAL_ERROR"

    __str__ = str.__str__


CreditSessionBankEmploymentStatusOrStr: TypeAlias = Annotated[
    CreditSessionBankEmploymentStatus | str, open_enum_validator(CreditSessionBankEmploymentStatus)
]
