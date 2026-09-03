from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferOriginatorAddress(SdkBaseModel):
    """The originator's address."""

    city: str
    """The full city name."""

    street: str
    """The full street address."""

    region: str
    """The two-letter code for the state or province (e.g., "CA")."""

    postal_code: str
    """The postal code (e.g., "94103")."""

    country_code: str
    """ISO-3166-1 alpha-2 country code standard."""


class TransferOriginatorAddressDict(TypedDict):
    city: str
    street: str
    region: str
    postal_code: str
    country_code: str
