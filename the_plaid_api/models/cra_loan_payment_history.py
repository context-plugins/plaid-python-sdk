from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class CraLoanPaymentHistory(SdkBaseModel):
    """Contains the payment information for a loan payment period."""

    period: int
    """The index to identify the loan's payment period, starting from 1. For example:
      1 means the period between the loan's opening date and the 1st payment due date.
      2 means the period between the loan's 1st payment due date and 2nd payment due date."""

    due_date: Date
    """The payment due date or end date of the payment period. The date should be in ISO 8601 format (YYYY-MM-DD)."""

    days_past_due: int
    """The number of days the loan was delinquent at the end of the pay period. If specified, should be greater than or
    equal to 0."""

    amount_past_due: Optional[float] = UNSET
    """The amount past due or the charge-off amount of the loan at the end of the payment period."""

    balance_remaining: Optional[float] = UNSET
    """The balance remaining on the loan at the end of the payment period."""


class CraLoanPaymentHistoryDict(TypedDict):
    period: int
    due_date: Date
    days_past_due: int
    amount_past_due: NotRequired[float]
    balance_remaining: NotRequired[float]
