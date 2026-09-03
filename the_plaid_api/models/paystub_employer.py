from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .paystub_address import PaystubAddress, PaystubAddressDict


class PaystubEmployer(SdkBaseModel):
    """Information about the employer on the paystub"""

    address: Optional[PaystubAddress] = UNSET
    """Address on the paystub"""

    name: str | None
    """The name of the employer on the paystub."""


class PaystubEmployerDict(TypedDict):
    address: NotRequired[PaystubAddress | PaystubAddressDict]
    name: str | None
