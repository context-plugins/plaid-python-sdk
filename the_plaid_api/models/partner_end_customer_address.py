from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PartnerEndCustomerAddress(SdkBaseModel):
    """The end customer's address."""

    city: Optional[str] = UNSET
    street: Optional[str] = UNSET
    region: Optional[str] = UNSET
    postal_code: Optional[str] = UNSET
    country_code: Optional[str] = UNSET
    """ISO-3166-1 alpha-2 country code standard."""


class PartnerEndCustomerAddressDict(TypedDict):
    city: NotRequired[str]
    street: NotRequired[str]
    region: NotRequired[str]
    postal_code: NotRequired[str]
    country_code: NotRequired[str]
