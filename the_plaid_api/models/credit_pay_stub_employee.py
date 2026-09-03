from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_pay_stub_address import CreditPayStubAddress, CreditPayStubAddressDict
from .pay_stub_taxpayer_id import PayStubTaxpayerId, PayStubTaxpayerIdDict


class CreditPayStubEmployee(SdkBaseModel):
    """Data about the employee."""

    address: CreditPayStubAddress
    """Address on the pay stub."""

    name: str | None
    """The name of the employee."""

    marital_status: str | None
    """Marital status of the employee - one of ``SINGLE``, ``MARRIED``, or ``NOT LISTED``."""

    taxpayer_id: PayStubTaxpayerId
    """Taxpayer ID of the individual receiving the paystub."""


class CreditPayStubEmployeeDict(TypedDict):
    address: CreditPayStubAddress | CreditPayStubAddressDict
    name: str | None
    marital_status: str | None
    taxpayer_id: PayStubTaxpayerId | PayStubTaxpayerIdDict
