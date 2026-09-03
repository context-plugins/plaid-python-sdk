from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MortgagePropertyAddress(SdkBaseModel):
    """Object containing fields describing property address."""

    city: str | None
    """The city name."""

    country: str | None
    """The ISO 3166-1 alpha-2 country code."""

    postal_code: str | None
    """The five or nine digit postal code."""

    region: str | None
    """The region or state (example "NC")."""

    street: str | None
    """The full street address (example "564 Main Street, Apt 15")."""


class MortgagePropertyAddressDict(TypedDict):
    city: str | None
    country: str | None
    postal_code: str | None
    region: str | None
    street: str | None
