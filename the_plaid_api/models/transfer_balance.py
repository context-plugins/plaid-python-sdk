from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.transfer_balance_type import TransferBalanceTypeOrStr


class TransferBalance(SdkBaseModel):
    """Information about the balance held with Plaid."""

    available: str
    """The amount of this balance available for use (decimal string with two digits of precision e.g. "10.00")."""

    current: Optional[str] = UNSET
    """The available balance, plus the amount of pending funds that are in processing (decimal string with two digits of
    precision e.g. "10.00")."""

    type_: TransferBalanceTypeOrStr = Field(alias="type")
    """The type of balance.

    ``prefunded_rtp_credits`` - Your prefunded RTP credit balance with Plaid ``prefunded_ach_credits`` - Your prefunded
    ACH credit balance with Plaid"""


class TransferBalanceDict(TypedDict):
    available: str
    current: NotRequired[str]
    type_: TransferBalanceTypeOrStr
