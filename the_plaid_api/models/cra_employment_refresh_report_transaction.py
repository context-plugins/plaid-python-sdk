from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class CraEmploymentRefreshReportTransaction(SdkBaseModel):
    """A transaction on the Employment Refresh Report. Note that this transaction differs from a Base Report transaction
    in that it will only be deposits, and the amounts will be omitted."""

    account_id: str
    """The ID of the account in which this transaction occurred."""

    original_description: str
    """The string returned by the financial institution to describe the transaction."""

    date: Date
    """For pending transactions, the date that the transaction occurred; for posted transactions, the date that the
    transaction posted. Both dates are returned in an ISO 8601 format ( ``YYYY-MM-DD`` )."""

    pending: bool
    """When ``true``, identifies the transaction as pending or unsettled. Pending transaction details (name, type,
    amount, category ID) may change before they are settled."""

    transaction_id: str
    """The unique ID of the transaction. Like all Plaid identifiers, the ``transaction_id`` is case sensitive."""


class CraEmploymentRefreshReportTransactionDict(TypedDict):
    account_id: str
    original_description: str
    date: Date
    pending: bool
    transaction_id: str
