from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_current_modeled_income import CraCurrentModeledIncome, CraCurrentModeledIncomeDict
from .cra_projected_modeled_income import CraProjectedModeledIncome, CraProjectedModeledIncomeDict


class CraIncomeMetrics(SdkBaseModel):
    """Modeled income metrics for a given income stream or user summary."""

    current: CraCurrentModeledIncome | None
    """Modeled estimate of current income based on recently observed income transactions."""

    projected: CraProjectedModeledIncome | None
    """Forward-looking modeled estimate of income based on recent income transactions and trends in active streams."""

    iso_currency_code: str | None
    """The ISO 4217 currency code of the amount or balance."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the amount or balance. Always ``null`` if ``iso_currency_code`` is
    non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries."""


class CraIncomeMetricsDict(TypedDict):
    current: CraCurrentModeledIncomeDict | None
    projected: CraProjectedModeledIncomeDict | None
    iso_currency_code: str | None
    unofficial_currency_code: str | None
