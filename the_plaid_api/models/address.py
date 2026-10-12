from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address_data import AddressData, AddressDataDict


class Address(SdkBaseModel):
    """A physical mailing address."""

    data: AddressData
    """Data about the components comprising an address."""

    primary: Optional[bool] = UNSET
    """When ``true``, identifies the address as the primary address on an account."""


class AddressDict(TypedDict):
    data: AddressDataDict
    primary: NotRequired[bool]
