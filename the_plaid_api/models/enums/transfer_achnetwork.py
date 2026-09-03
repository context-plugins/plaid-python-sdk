from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferAchnetwork(str, Enum):
    """The ACH networks used for the funds flow.

    For requests submitted as either ``ach`` or ``same-day-ach`` the cutoff for Same Day ACH is 3:00 PM Eastern Time and
    the cutoff for Standard ACH transfers is 8:30 PM Eastern Time. It is recommended to submit a request at least 15
    minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any request that is
    indicated as ``same-day-ach`` and that misses the Same Day ACH cutoff, but is submitted in time for the Standard ACH
    cutoff, will be sent over Standard ACH rails and will not incur same-day charges."""

    ACH = "ach"
    SAME_DAY_ACH = "same-day-ach"

    __str__ = str.__str__


TransferAchnetworkOrStr: TypeAlias = Annotated[TransferAchnetwork | str, open_enum_validator(TransferAchnetwork)]
