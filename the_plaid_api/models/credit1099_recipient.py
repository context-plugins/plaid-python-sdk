from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .credit_pay_stub_address import CreditPayStubAddress, CreditPayStubAddressDict


class Credit1099Recipient(SdkBaseModel):
    """An object representing a recipient used in both 1099-K and 1099-MISC tax documents."""

    address: Optional[CreditPayStubAddress] = UNSET
    """Address on the pay stub."""

    name: OptionalNullable[str] = UNSET
    """Name of recipient."""

    tin: OptionalNullable[str] = UNSET
    """Tax identification number of recipient."""

    account_number: OptionalNullable[str] = UNSET
    """Account number of recipient."""

    facta_filing_requirement: OptionalNullable[str] = UNSET
    """Checked if FATCA is a filing requirement."""

    second_tin_exists: OptionalNullable[str] = UNSET
    """Checked if 2nd TIN exists."""


class Credit1099RecipientDict(TypedDict):
    address: NotRequired[CreditPayStubAddress | CreditPayStubAddressDict]
    name: NotRequired[str | None]
    tin: NotRequired[str | None]
    account_number: NotRequired[str | None]
    facta_filing_requirement: NotRequired[str | None]
    second_tin_exists: NotRequired[str | None]
