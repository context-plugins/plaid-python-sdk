from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferMetricsGetReturnRatesOverInterval(SdkBaseModel):
    """Details regarding return rates."""

    overall_return_rate: Optional[str] = UNSET
    """The overall return rate."""

    unauthorized_return_rate: Optional[str] = UNSET
    """The unauthorized return rate."""

    administrative_return_rate: Optional[str] = UNSET
    """The administrative return rate."""


class TransferMetricsGetReturnRatesOverIntervalDict(TypedDict):
    overall_return_rate: NotRequired[str]
    unauthorized_return_rate: NotRequired[str]
    administrative_return_rate: NotRequired[str]
