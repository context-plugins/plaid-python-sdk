from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WatchlistScreeningIndividualUpdateRequestResettableField(str, Enum):
    """The name of a field that can be reset back to null"""

    ASSIGNEE = "assignee"

    __str__ = str.__str__


WatchlistScreeningIndividualUpdateRequestResettableFieldOrStr: TypeAlias = Annotated[
    WatchlistScreeningIndividualUpdateRequestResettableField | str,
    open_enum_validator(WatchlistScreeningIndividualUpdateRequestResettableField),
]
