from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RemovedTransaction(SdkBaseModel):
    """A representation of a removed transaction"""

    transaction_id: str
    """The ID of the removed transaction."""

    account_id: str
    """The ID of the account of the removed transaction."""


class RemovedTransactionDict(TypedDict):
    transaction_id: str
    account_id: str
