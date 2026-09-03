from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AamvamatchResult(str, Enum):
    """The outcome of checking the particular field against state databases.


    ``match`` - The field is an exact match with the state database.

    ``no_match`` - The field is not an exact match with the state database.

    ``no_data`` - The field was unable to be checked against state databases."""

    MATCH = "match"
    NO_MATCH = "no_match"
    NO_DATA = "no_data"

    __str__ = str.__str__


AamvamatchResultOrStr: TypeAlias = Annotated[AamvamatchResult | str, open_enum_validator(AamvamatchResult)]
