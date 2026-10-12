from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class LinkTokenCashflowReport(SdkBaseModel):
    """Configuration parameters for the Cashflow Report product. Currently in closed beta."""

    days_requested: int = 365
    """Number of days of transaction history to request in the Cashflow Report product."""


class LinkTokenCashflowReportDict(TypedDict):
    days_requested: NotRequired[int]
