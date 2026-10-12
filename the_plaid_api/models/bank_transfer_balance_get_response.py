from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bank_transfer_balance import BankTransferBalance, BankTransferBalanceDict


class BankTransferBalanceGetResponse(SdkBaseModel):
    """Defines the response schema for ``/bank_transfer/balance/get``"""

    balance: BankTransferBalance
    """Information about the balance of a bank transfer"""

    origination_account_id: str | None
    """The ID of the origination account that this balance belongs to."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BankTransferBalanceGetResponseDict(TypedDict):
    balance: BankTransferBalanceDict
    origination_account_id: str | None
    request_id: str
