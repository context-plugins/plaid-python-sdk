from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.wallet_transaction_status import WalletTransactionStatusOrStr


class WalletTransactionExecuteResponse(SdkBaseModel):
    """WalletTransactionExecuteResponse defines the response schema for ``/wallet/transaction/execute``"""

    transaction_id: str
    """A unique ID identifying the transaction"""

    status: WalletTransactionStatusOrStr
    """The status of the transaction.

    ``AUTHORISING``: The transaction is being processed for validation and compliance.

    ``INITIATED``: The transaction has been initiated and is currently being processed.

    ``EXECUTED``: The transaction has been successfully executed and is considered complete. This is only applicable for
    debit transactions.

    ``SETTLED``: The transaction has settled and funds are available for use. This is only applicable for credit
    transactions. A transaction will typically settle within seconds to several days, depending on which payment rail is
    used.

    ``FAILED``: The transaction failed to process successfully. This is a terminal status.

    ``BLOCKED``: The transaction has been blocked for violating compliance rules. This is a terminal status."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class WalletTransactionExecuteResponseDict(TypedDict):
    transaction_id: str
    status: WalletTransactionStatusOrStr
    request_id: str
