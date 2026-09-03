from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BeaconUserStatus(str, Enum):
    """A status of a Beacon User.

    ``rejected``: The Beacon User has been rejected for fraud. Users can be automatically or manually rejected.

    ``pending_review``: The Beacon User has been marked for review.

    ``cleared``: The Beacon User has been cleared of fraud."""

    REJECTED = "rejected"
    PENDING_REVIEW = "pending_review"
    CLEARED = "cleared"

    __str__ = str.__str__


BeaconUserStatusOrStr: TypeAlias = Annotated[BeaconUserStatus | str, open_enum_validator(BeaconUserStatus)]
