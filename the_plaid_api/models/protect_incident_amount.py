from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ProtectIncidentAmount(SdkBaseModel):
    """The monetary amount associated with the incident."""

    iso_currency_code: str | None = "USD"
    """The ISO-4217 currency code of the incident amount. Defaults to ``USD`` if not specified."""

    value: float
    """The monetary value of the incident amount."""


class ProtectIncidentAmountDict(TypedDict):
    iso_currency_code: NotRequired[str | None]
    value: float
