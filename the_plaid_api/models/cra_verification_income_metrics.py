from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_verification_modeled_income import CraVerificationModeledIncome, CraVerificationModeledIncomeDict


class CraVerificationIncomeMetrics(SdkBaseModel):
    """Modeled income metrics for a given income stream or user summary."""

    current: CraVerificationModeledIncome | None
    """Modeled estimate of current income based on recently observed income transactions."""

    iso_currency_code: str | None
    """The ISO 4217 currency code of the amount or balance."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the amount or balance. Always ``null`` if ``iso_currency_code`` is
    non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries."""


class CraVerificationIncomeMetricsDict(TypedDict):
    current: CraVerificationModeledIncomeDict | None
    iso_currency_code: str | None
    unofficial_currency_code: str | None
