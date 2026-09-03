from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferUserAddressInRequest(SdkBaseModel):
    """The address associated with the account holder."""

    street: Optional[str] = UNSET
    """The street number and name (i.e., "100 Market St.")."""

    city: Optional[str] = UNSET
    """Ex. "San Francisco"
    """

    region: Optional[str] = UNSET
    """The state or province (e.g., "CA")."""

    postal_code: Optional[str] = UNSET
    """The postal code (e.g., "94103")."""

    country: Optional[str] = UNSET
    """A two-letter country code (e.g., "US")."""


class TransferUserAddressInRequestDict(TypedDict):
    street: NotRequired[str]
    city: NotRequired[str]
    region: NotRequired[str]
    postal_code: NotRequired[str]
    country: NotRequired[str]
