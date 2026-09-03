from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TaxpayerId(SdkBaseModel):
    """Taxpayer ID of the individual receiving the paystub."""

    id_type: OptionalNullable[str] = UNSET
    """Type of ID, e.g. 'SSN'"""

    id_mask: OptionalNullable[str] = UNSET
    """ID mask; i.e. last 4 digits of the taxpayer ID"""

    last_4_digits: OptionalNullable[str] = UNSET
    """Last 4 digits of unique number of ID."""


class TaxpayerIdDict(TypedDict):
    id_type: NotRequired[str | None]
    id_mask: NotRequired[str | None]
    last_4_digits: NotRequired[str | None]
