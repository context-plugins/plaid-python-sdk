from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class CustomSandboxTransaction(SdkBaseModel):
    """Data to populate as test transaction data."""

    date_transacted: Date
    """The date of the transaction, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format.
    Transaction date must be the present date or a date up to 14 days in the past. Future dates are not allowed."""

    date_posted: Date
    """The date the transaction posted, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format.
    Posted date must be the present date or a date up to 14 days in the past. Future dates are not allowed."""

    amount: float
    """The transaction amount. Can be negative."""

    description: str
    """The transaction description."""

    iso_currency_code: Optional[str] = UNSET
    """The ISO-4217 format currency code for the transaction. Defaults to USD."""


class CustomSandboxTransactionDict(TypedDict):
    date_transacted: Date
    date_posted: Date
    amount: float
    description: str
    iso_currency_code: NotRequired[str]
