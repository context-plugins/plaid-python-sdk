from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.earnings_breakdown_canonical_description import EarningsBreakdownCanonicalDescriptionOrStr


class PaystubOverrideEarningsBreakdown(SdkBaseModel):
    """An object representing the earnings line items for the pay period."""

    canonical_description: OptionalNullable[EarningsBreakdownCanonicalDescriptionOrStr] = UNSET
    """Commonly used term to describe the earning line item."""

    current_amount: OptionalNullable[float] = UNSET
    """Raw amount of the earning line item."""

    description: OptionalNullable[str] = UNSET
    """Description of the earning line item."""

    hours: OptionalNullable[float] = UNSET
    """Number of hours applicable for this earning."""

    currency: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the line item."""

    rate: OptionalNullable[float] = UNSET
    """Hourly rate applicable for this earning."""

    ytd_amount: OptionalNullable[float] = UNSET
    """The year-to-date amount of the line item."""


class PaystubOverrideEarningsBreakdownDict(TypedDict):
    canonical_description: NotRequired[EarningsBreakdownCanonicalDescriptionOrStr | None]
    current_amount: NotRequired[float | None]
    description: NotRequired[str | None]
    hours: NotRequired[float | None]
    currency: NotRequired[str | None]
    rate: NotRequired[float | None]
    ytd_amount: NotRequired[float | None]
