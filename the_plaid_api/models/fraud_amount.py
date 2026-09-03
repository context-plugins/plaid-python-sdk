from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class FraudAmount(SdkBaseModel):
    """The amount and currency of the fraud or attempted fraud. ``fraud_amount`` should be omitted to indicate an
    unknown fraud amount."""

    iso_currency_code: Literal["USD"] = "USD"
    """An ISO-4217 currency code."""

    value: float
    """The amount value. This value can be 0 to indicate no money was lost. Must not contain more than two digits of
    precision (e.g., ``1.23``)."""


class FraudAmountDict(TypedDict):
    iso_currency_code: NotRequired[Literal["USD"]]
    value: float
