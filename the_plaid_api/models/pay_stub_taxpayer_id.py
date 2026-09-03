from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PayStubTaxpayerId(SdkBaseModel):
    """Taxpayer ID of the individual receiving the paystub."""

    id_type: str | None
    """Type of ID, e.g. 'SSN'."""

    id_mask: str | None
    """ID mask; i.e. last 4 digits of the taxpayer ID."""


class PayStubTaxpayerIdDict(TypedDict):
    id_type: str | None
    id_mask: str | None
