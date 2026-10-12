from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .paystub_address import PaystubAddress, PaystubAddressDict
from .taxpayer_id import TaxpayerId, TaxpayerIdDict


class Employee(SdkBaseModel):
    """Data about the employee."""

    address: PaystubAddress
    """Address on the paystub"""

    name: str | None
    """The name of the employee."""

    marital_status: OptionalNullable[str] = UNSET
    """Marital status of the employee - either ``single`` or ``married``."""

    taxpayer_id: Optional[TaxpayerId] = UNSET
    """Taxpayer ID of the individual receiving the paystub."""


class EmployeeDict(TypedDict):
    address: PaystubAddressDict
    name: str | None
    marital_status: NotRequired[str | None]
    taxpayer_id: NotRequired[TaxpayerIdDict]
