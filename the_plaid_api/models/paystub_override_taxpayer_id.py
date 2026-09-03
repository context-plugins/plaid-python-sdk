from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaystubOverrideTaxpayerId(SdkBaseModel):
    """Taxpayer ID of the individual receiving the paystub."""

    id_type: OptionalNullable[str] = UNSET
    """Type of ID, e.g. 'SSN'"""

    id_mask: OptionalNullable[str] = UNSET
    """ID mask; i.e. last 4 digits of the taxpayer ID"""


class PaystubOverrideTaxpayerIdDict(TypedDict):
    id_type: NotRequired[str | None]
    id_mask: NotRequired[str | None]
