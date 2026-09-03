from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BankTransferBalance(SdkBaseModel):
    """Information about the balance of a bank transfer"""

    available: str
    """The total available balance - the sum of all successful debit transfer amounts minus all credit transfer
    amounts."""

    transactable: str
    """The transactable balance shows the amount in your account that you are able to use for transfers, and is
    essentially your available balance minus your minimum balance."""


class BankTransferBalanceDict(TypedDict):
    available: str
    transactable: str
