from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .paystub_override_employer_address import PaystubOverrideEmployerAddress, PaystubOverrideEmployerAddressDict


class PaystubOverrideEmployer(SdkBaseModel):
    """The employer on the paystub."""

    name: OptionalNullable[str] = UNSET
    """The name of the employer."""

    address: Optional[PaystubOverrideEmployerAddress] = UNSET
    """The address of the employer."""


class PaystubOverrideEmployerDict(TypedDict):
    name: NotRequired[str | None]
    address: NotRequired[PaystubOverrideEmployerAddress | PaystubOverrideEmployerAddressDict]
