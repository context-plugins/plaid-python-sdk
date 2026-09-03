from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskCheckEmailName(str, Enum):
    """Indicates whether the provided name matches the email address according to the KYC name-matches-email inference
    result if known.

    ``match`` - "The email's name identifiers match the user's name."

    ``partial_match`` - "The email's name identifiers partially match the user's name."

    ``no_match`` - "The email's name identifiers do not match the user's name."

    ``indeterminate`` - "The email does not contain any name identifiers, and a match could not be determined."

    ``no_input`` - "The user's profile does not contain the required user inputs to determine a match."

    ``no_data`` - "Field could not be verified against available sources."
    """

    NO_INPUT = "no_input"
    INDETERMINATE = "indeterminate"
    NO_MATCH = "no_match"
    PARTIAL_MATCH = "partial_match"
    MATCH = "match"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskCheckEmailNameOrStr: TypeAlias = Annotated[RiskCheckEmailName | str, open_enum_validator(RiskCheckEmailName)]
