from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WatchlistScreeningStatus(str, Enum):
    """A status enum indicating whether a screening is still pending review, has been rejected, or has been cleared."""

    REJECTED = "rejected"
    PENDING_REVIEW = "pending_review"
    CLEARED = "cleared"

    __str__ = str.__str__


WatchlistScreeningStatusOrStr: TypeAlias = Annotated[
    WatchlistScreeningStatus | str, open_enum_validator(WatchlistScreeningStatus)
]
