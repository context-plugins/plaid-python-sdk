from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.total_canonical_description import TotalCanonicalDescriptionOrStr
from .pay import Pay, PayDict


class Total(SdkBaseModel):
    """An object representing both the current pay period and year to date amount for a category."""

    canonical_description: OptionalNullable[TotalCanonicalDescriptionOrStr] = UNSET
    """Commonly used term to describe the line item."""

    description: OptionalNullable[str] = UNSET
    """Text of the line item as printed on the paystub."""

    current_pay: Optional[Pay] = UNSET
    """An object representing a monetary amount."""

    ytd_pay: Optional[Pay] = UNSET
    """An object representing a monetary amount."""


class TotalDict(TypedDict):
    canonical_description: NotRequired[TotalCanonicalDescriptionOrStr | None]
    description: NotRequired[str | None]
    current_pay: NotRequired[Pay | PayDict]
    ytd_pay: NotRequired[Pay | PayDict]
