from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferUserAddressInResponse(SdkBaseModel):
    """The address associated with the account holder."""

    street: str | None
    """The street number and name (i.e., "100 Market St.")."""

    city: str | None
    """Ex. "San Francisco"
    """

    region: str | None
    """The state or province (e.g., "CA")."""

    postal_code: str | None
    """The postal code (e.g., "94103")."""

    country: str | None
    """A two-letter country code (e.g., "US")."""


class TransferUserAddressInResponseDict(TypedDict):
    street: str | None
    city: str | None
    region: str | None
    postal_code: str | None
    country: str | None
