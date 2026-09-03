from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .credit_pay_stub_address import CreditPayStubAddress, CreditPayStubAddressDict


class Credit1099Payer(SdkBaseModel):
    """An object representing a payer used by 1099-MISC tax documents."""

    address: Optional[CreditPayStubAddress] = UNSET
    """Address on the pay stub."""

    name: OptionalNullable[str] = UNSET
    """Name of payer."""

    tin: OptionalNullable[str] = UNSET
    """Tax identification number of payer."""

    telephone_number: OptionalNullable[str] = UNSET
    """Telephone number of payer."""


class Credit1099PayerDict(TypedDict):
    address: NotRequired[CreditPayStubAddress | CreditPayStubAddressDict]
    name: NotRequired[str | None]
    tin: NotRequired[str | None]
    telephone_number: NotRequired[str | None]
