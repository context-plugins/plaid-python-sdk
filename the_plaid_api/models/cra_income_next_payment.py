from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class CraIncomeNextPayment(SdkBaseModel):
    """Metadata of the income stream's next payment."""

    date: Date
    """The expected date of the income stream's next payment. The date will be returned in an ISO 8601 format
    (YYYY-MM-DD)."""


class CraIncomeNextPaymentDict(TypedDict):
    date: Date
