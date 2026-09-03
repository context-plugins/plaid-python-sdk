from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RefreshInterval(str, Enum):
    """How frequently data for subscription products like Investments, Transactions, and Liabilities, is being
    refreshed, relative to the institution's normal scheduling. The ``refresh_interval`` may be ``DELAYED`` or
    ``STOPPED`` even when the success rate is high."""

    NORMAL = "NORMAL"
    DELAYED = "DELAYED"
    STOPPED = "STOPPED"

    __str__ = str.__str__


RefreshIntervalOrStr: TypeAlias = Annotated[RefreshInterval | str, open_enum_validator(RefreshInterval)]
