from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .paystub_override_employee_address import PaystubOverrideEmployeeAddress, PaystubOverrideEmployeeAddressDict
from .paystub_override_taxpayer_id import PaystubOverrideTaxpayerId, PaystubOverrideTaxpayerIdDict


class PaystubOverrideEmployee(SdkBaseModel):
    """The employee on the paystub."""

    name: Optional[str] = UNSET
    """The name of the employee."""

    address: Optional[PaystubOverrideEmployeeAddress] = UNSET
    """The address of the employee."""

    marital_status: OptionalNullable[str] = UNSET
    """Marital status of the employee - either ``single`` or ``married``."""

    taxpayer_id: Optional[PaystubOverrideTaxpayerId] = UNSET
    """Taxpayer ID of the individual receiving the paystub."""


class PaystubOverrideEmployeeDict(TypedDict):
    name: NotRequired[str]
    address: NotRequired[PaystubOverrideEmployeeAddressDict]
    marital_status: NotRequired[str | None]
    taxpayer_id: NotRequired[PaystubOverrideTaxpayerIdDict]
