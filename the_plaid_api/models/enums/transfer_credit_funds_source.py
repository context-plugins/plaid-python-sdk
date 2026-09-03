from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferCreditFundsSource(str, Enum):
    """This field is now deprecated. You may ignore it for transfers created on and after 12/01/2023.

    Specifies the source of funds for the transfer. Only valid for ``credit`` transfers, and defaults to ``sweep`` if
    not specified. This field is not specified for ``debit`` transfers.

    ``sweep`` - Sweep funds from your funding account ``prefunded_rtp_credits`` - Use your prefunded RTP credit balance
    with Plaid ``prefunded_ach_credits`` - Use your prefunded ACH credit balance with Plaid"""

    SWEEP = "sweep"
    PREFUNDED_RTP_CREDITS = "prefunded_rtp_credits"
    PREFUNDED_ACH_CREDITS = "prefunded_ach_credits"

    __str__ = str.__str__


TransferCreditFundsSourceOrStr: TypeAlias = Annotated[
    TransferCreditFundsSource | str, open_enum_validator(TransferCreditFundsSource)
]
