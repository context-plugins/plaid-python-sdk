from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .credit_pay_stub_address import CreditPayStubAddress, CreditPayStubAddressDict


class Credit1099Filer(SdkBaseModel):
    """An object representing a filer used by 1099-K tax documents."""

    address: Optional[CreditPayStubAddress] = UNSET
    """Address on the pay stub."""

    name: OptionalNullable[str] = UNSET
    """Name of filer."""

    tin: OptionalNullable[str] = UNSET
    """Tax identification number of filer."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """One of the following values will be provided: Payment Settlement Entity (PSE), Electronic Payment Facilitator
    (EPF), Other Third Party"""


class Credit1099FilerDict(TypedDict):
    address: NotRequired[CreditPayStubAddressDict]
    name: NotRequired[str | None]
    tin: NotRequired[str | None]
    type_: NotRequired[str | None]
