from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecommendationString(str, Enum):
    """The recommendation result for that date."""

    RECOMMENDED = "RECOMMENDED"
    NOT_RECOMMENDED = "NOT_RECOMMENDED"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


RecommendationStringOrStr: TypeAlias = Annotated[RecommendationString | str, open_enum_validator(RecommendationString)]
