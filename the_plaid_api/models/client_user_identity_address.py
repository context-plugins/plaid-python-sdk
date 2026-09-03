from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ClientUserIdentityAddress(SdkBaseModel):
    """User address information."""

    street_1: OptionalNullable[str] = UNSET
    """First line of street address."""

    street_2: OptionalNullable[str] = UNSET
    """Second line of street address."""

    city: OptionalNullable[str] = UNSET
    """City name."""

    region: OptionalNullable[str] = UNSET
    """State, province or region."""

    country: str
    """Country code."""

    postal_code: OptionalNullable[str] = UNSET
    """Postal or ZIP code."""

    primary: bool
    """Indicates whether this is the primary address for the User."""


class ClientUserIdentityAddressDict(TypedDict):
    street_1: NotRequired[str | None]
    street_2: NotRequired[str | None]
    city: NotRequired[str | None]
    region: NotRequired[str | None]
    country: str
    postal_code: NotRequired[str | None]
    primary: bool
