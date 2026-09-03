from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClientProvidedTransactionLocation(SdkBaseModel):
    """A representation of where a transaction took place.

    Use this field to pass in structured location information you may have about your transactions. Providing location
    data is optional but can increase result quality. If you have unstructured location information, it may be appended
    to the ``description`` field."""

    country: Optional[str] = UNSET
    """The country where the transaction occurred, formatted as an ISO 3166-1 alpha-2 country code ("US" or "CA")."""

    region: Optional[str] = UNSET
    """The region or state where the transaction occurred, formatted as the official two-letter US state or Canadian
    province postal code, e.g. "CT" or "QC"."""

    city: Optional[str] = UNSET
    """The city where the transaction occurred."""

    address: Optional[str] = UNSET
    """The street address where the transaction occurred."""

    postal_code: Optional[str] = UNSET
    """The postal code where the transaction occurred."""


class ClientProvidedTransactionLocationDict(TypedDict):
    country: NotRequired[str]
    region: NotRequired[str]
    city: NotRequired[str]
    address: NotRequired[str]
    postal_code: NotRequired[str]
