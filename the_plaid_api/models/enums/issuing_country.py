from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IssuingCountry(str, Enum):
    """A binary match indicator specifying whether the country that issued the provided document matches the country
    that the user separately provided to Plaid.

    Note: You can configure whether a ``no_match`` on ``issuing_country`` fails the ``documentary_verification`` by
    editing your Plaid Template."""

    MATCH = "match"
    NO_MATCH = "no_match"

    __str__ = str.__str__


IssuingCountryOrStr: TypeAlias = Annotated[IssuingCountry | str, open_enum_validator(IssuingCountry)]
