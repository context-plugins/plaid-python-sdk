from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferBalanceType(str, Enum):
    """The type of balance.

    ``prefunded_rtp_credits`` - Your prefunded RTP credit balance with Plaid ``prefunded_ach_credits`` - Your prefunded
    ACH credit balance with Plaid"""

    PREFUNDED_RTP_CREDITS = "prefunded_rtp_credits"
    PREFUNDED_ACH_CREDITS = "prefunded_ach_credits"

    __str__ = str.__str__


TransferBalanceTypeOrStr: TypeAlias = Annotated[TransferBalanceType | str, open_enum_validator(TransferBalanceType)]
