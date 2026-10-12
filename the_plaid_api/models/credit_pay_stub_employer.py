from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_pay_stub_address import CreditPayStubAddress, CreditPayStubAddressDict


class CreditPayStubEmployer(SdkBaseModel):
    """Information about the employer on the pay stub."""

    address: CreditPayStubAddress
    """Address on the pay stub."""

    name: str | None
    """The name of the employer on the pay stub."""


class CreditPayStubEmployerDict(TypedDict):
    address: CreditPayStubAddressDict
    name: str | None
