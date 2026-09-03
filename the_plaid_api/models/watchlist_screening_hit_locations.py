from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WatchlistScreeningHitLocations(SdkBaseModel):
    """Location information for the associated watchlist hit"""

    full: str
    """The full location string, potentially including elements like street, city, postal codes and country codes. Note
    that this is not necessarily a complete or well-formatted address."""

    country: str
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2
    form."""


class WatchlistScreeningHitLocationsDict(TypedDict):
    full: str
    country: str
