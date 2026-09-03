from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .apr import Apr, AprDict


class CreditCardLiability(SdkBaseModel):
    """An object representing a credit card account."""

    account_id: str | None
    """The ID of the account that this liability belongs to."""

    aprs: list[Apr]
    """The various interest rates that apply to the account. APR information is not provided by all card issuers; if APR
    data is not available, this array will be empty."""

    is_overdue: bool | None
    """true if a payment is currently overdue. Availability for this field is limited."""

    last_payment_amount: float | None
    """The amount of the last payment."""

    last_payment_date: Date | None
    """The date of the last payment. Dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (YYYY-MM-DD). Availability for this field is limited."""

    last_statement_issue_date: Date | None
    """The date of the last statement. Dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__
    format (YYYY-MM-DD)."""

    last_statement_balance: float | None
    """The total amount owed as of the last statement issued"""

    minimum_payment_amount: float | None
    """The minimum payment due for the next billing cycle."""

    next_payment_due_date: Date | None
    """The due date for the next payment. The due date is ``null`` if a payment is not expected. Dates are returned in
    an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""


class CreditCardLiabilityDict(TypedDict):
    account_id: str | None
    aprs: list[Apr | AprDict]
    is_overdue: bool | None
    last_payment_amount: float | None
    last_payment_date: Date | None
    last_statement_issue_date: Date | None
    last_statement_balance: float | None
    minimum_payment_amount: float | None
    next_payment_due_date: Date | None
