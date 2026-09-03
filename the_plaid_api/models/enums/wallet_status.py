from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalletStatus(str, Enum):
    """The status of the wallet.

    ``UNKNOWN``: The wallet status is unknown.

    ``ACTIVE``: The wallet is active and ready to send money to and receive money from.

    ``CLOSED``: The wallet is closed. Any transactions made to or from this wallet will error."""

    UNKNOWN = "UNKNOWN"
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"

    __str__ = str.__str__


WalletStatusOrStr: TypeAlias = Annotated[WalletStatus | str, open_enum_validator(WalletStatus)]
