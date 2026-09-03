from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferEventType(str, Enum):
    """The type of event that this transfer represents. Event types with prefix ``sweep`` represent events for Plaid
    Ledger sweeps.

    ``pending``: A new transfer was created; it is in the pending state.

    ``cancelled``: The transfer was cancelled by the client.

    ``failed``: The transfer failed, no funds were moved.

    ``posted``: The transfer has been successfully submitted to the payment network.

    ``settled``: The transfer has been successfully completed by the payment network.

    ``funds_available``: Funds from the transfer have been released from hold and applied to the ledger's available
    balance. (Only applicable to ACH debits.)

    ``guaranteed``: The transfer has been fully guaranteed by Plaid.

    ``returned``: A posted transfer was returned.

    ``guarantee_reimbursed``: Plaid reimbursed the client for the loss on a returned guaranteed transfer. The
    ``event_amount`` is the reimbursed amount.

    ``client_return_recovered``: The client reported recovering the loss on a returned transfer via
    ``/transfer/return/recover``, and Plaid debited the recovered amount from the client's ledger. The ``event_amount``
    is the recovered amount.

    ``plaid_return_recovered``: Plaid recovered the loss on a returned transfer by successfully reinitiating it. The
    ``event_amount`` is the recovered amount. Client should stop their return recovery effort.

    ``swept``: The transfer was swept to / from the sweep account.

    ``swept_settled``: Credits are available to be withdrawn or debits have been deducted from the customer's business
    checking account.

    ``return_swept``: Due to the transfer being returned, funds were pulled from or pushed back to the sweep account.

    ``sweep.pending``: A new ledger sweep was created; it is in the pending state.

    ``sweep.posted``: The ledger sweep has been successfully submitted to the payment network.

    ``sweep.settled``: The transaction has settled in the funding account. This means that funds withdrawn from Plaid
    Ledger balance have reached the funding account, or funds to be deposited into the Plaid Ledger Balance have been
    pulled, and the hold period has begun.

    ``sweep.returned``: A posted ledger sweep was returned.

    ``sweep.failed``: The ledger sweep failed, no funds were moved.

    ``sweep.funds_available``: Funds from the ledger sweep have been released from hold and applied to the ledger's
    available balance. This is only applicable to debits.

    ``refund.pending``: A new refund was created; it is in the pending state.

    ``refund.cancelled``: The refund was cancelled.

    ``refund.failed``: The refund failed, no funds were moved.

    ``refund.posted``: The refund has been successfully submitted to the payment network.

    ``refund.settled``: The refund transaction has settled in the Plaid linked account.

    ``refund.returned``: A posted refund was returned.

    ``refund.swept``: The refund was swept from the sweep account.

    ``refund.return_swept``: Due to the refund being returned, funds were pushed back to the sweep account."""

    PENDING = "pending"
    CANCELLED = "cancelled"
    FAILED = "failed"
    POSTED = "posted"
    SETTLED = "settled"
    FUNDS_AVAILABLE = "funds_available"
    GUARANTEED = "guaranteed"
    RETURNED = "returned"
    GUARANTEE_REIMBURSED = "guarantee_reimbursed"
    CLIENT_RETURN_RECOVERED = "client_return_recovered"
    PLAID_RETURN_RECOVERED = "plaid_return_recovered"
    SWEPT = "swept"
    SWEPT_SETTLED = "swept_settled"
    RETURN_SWEPT = "return_swept"
    SWEEP_PENDING = "sweep.pending"
    SWEEP_POSTED = "sweep.posted"
    SWEEP_SETTLED = "sweep.settled"
    SWEEP_RETURNED = "sweep.returned"
    SWEEP_FAILED = "sweep.failed"
    SWEEP_FUNDS_AVAILABLE = "sweep.funds_available"
    REFUND_PENDING = "refund.pending"
    REFUND_CANCELLED = "refund.cancelled"
    REFUND_FAILED = "refund.failed"
    REFUND_POSTED = "refund.posted"
    REFUND_SETTLED = "refund.settled"
    REFUND_RETURNED = "refund.returned"
    REFUND_SWEPT = "refund.swept"
    REFUND_RETURN_SWEPT = "refund.return_swept"

    __str__ = str.__str__


TransferEventTypeOrStr: TypeAlias = Annotated[TransferEventType | str, open_enum_validator(TransferEventType)]
