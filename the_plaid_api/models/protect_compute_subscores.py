from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ProtectComputeSubscores(SdkBaseModel):
    """Per-bucket subscores returned alongside the overall Trust Index score. For cash-advance models, each key maps to
    an amount-bucket subscore (0-100); higher values indicate lower fraud risk. Only buckets that were scored are
    included in the response."""

    cash_advance_bucket_0_25: OptionalNullable[int] = UNSET
    """Subscore for cash advance amounts in the range $0-$25."""

    cash_advance_bucket_25_50: OptionalNullable[int] = UNSET
    """Subscore for cash advance amounts in the range $25-$50."""

    cash_advance_bucket_50_100: OptionalNullable[int] = UNSET
    """Subscore for cash advance amounts in the range $50-$100."""

    cash_advance_bucket_100_200: OptionalNullable[int] = UNSET
    """Subscore for cash advance amounts in the range $100-$200."""

    cash_advance_bucket_200_300: OptionalNullable[int] = UNSET
    """Subscore for cash advance amounts in the range $200-$300."""

    cash_advance_bucket_300_400: OptionalNullable[int] = UNSET
    """Subscore for cash advance amounts in the range $300-$400."""

    cash_advance_bucket_400_500: OptionalNullable[int] = UNSET
    """Subscore for cash advance amounts in the range $400-$500."""


class ProtectComputeSubscoresDict(TypedDict):
    cash_advance_bucket_0_25: NotRequired[int | None]
    cash_advance_bucket_25_50: NotRequired[int | None]
    cash_advance_bucket_50_100: NotRequired[int | None]
    cash_advance_bucket_100_200: NotRequired[int | None]
    cash_advance_bucket_200_300: NotRequired[int | None]
    cash_advance_bucket_300_400: NotRequired[int | None]
    cash_advance_bucket_400_500: NotRequired[int | None]
