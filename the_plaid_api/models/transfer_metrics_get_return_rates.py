from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .transfer_metrics_get_return_rates_over_interval import (
    TransferMetricsGetReturnRatesOverInterval,
    TransferMetricsGetReturnRatesOverIntervalDict,
)


class TransferMetricsGetReturnRates(SdkBaseModel):
    """Details regarding return rates."""

    last_60d: OptionalNullable[TransferMetricsGetReturnRatesOverInterval] = UNSET
    """Details regarding return rates."""


class TransferMetricsGetReturnRatesDict(TypedDict):
    last_60d: NotRequired[TransferMetricsGetReturnRatesOverIntervalDict | None]
