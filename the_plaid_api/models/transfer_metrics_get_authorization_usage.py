from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferMetricsGetAuthorizationUsage(SdkBaseModel):
    """Details regarding authorization usage."""

    daily_credit_utilization: Optional[str] = UNSET
    """The daily credit utilization formatted as a decimal."""

    daily_debit_utilization: Optional[str] = UNSET
    """The daily debit utilization formatted as a decimal."""

    monthly_credit_utilization: Optional[str] = UNSET
    """The monthly credit utilization formatted as a decimal."""

    monthly_debit_utilization: Optional[str] = UNSET
    """The monthly debit utilization formatted as a decimal."""


class TransferMetricsGetAuthorizationUsageDict(TypedDict):
    daily_credit_utilization: NotRequired[str]
    daily_debit_utilization: NotRequired[str]
    monthly_credit_utilization: NotRequired[str]
    monthly_debit_utilization: NotRequired[str]
