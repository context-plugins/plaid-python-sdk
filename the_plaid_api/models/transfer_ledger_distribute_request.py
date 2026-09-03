from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferLedgerDistributeRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/ledger/distribute``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    from_ledger_id: str
    """The Ledger to pull money from."""

    to_ledger_id: str
    """The Ledger to credit money to."""

    amount: str
    """The amount to move (decimal string with two digits of precision e.g. "10.00"). Amount must be positive."""

    idempotency_key: str
    """A unique key provided by the client, per unique ledger distribute. Maximum of 50 characters.

    The API supports idempotency for safely retrying the request without accidentally performing the same operation
    twice. For example, if a request to create a ledger distribute fails due to a network connection error, you can
    retry the request with the same idempotency key to guarantee that only a single distribute is created."""

    description: Optional[str] = UNSET
    """An optional description for the ledger distribute operation."""


class TransferLedgerDistributeRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    from_ledger_id: str
    to_ledger_id: str
    amount: str
    idempotency_key: str
    description: NotRequired[str]
