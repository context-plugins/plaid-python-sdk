from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CraVerificationIncomeTransactionOutlier(SdkBaseModel):
    """Metadata on whether this income transaction is an outlier."""

    is_outlier: bool
    """Indicates whether an income transaction amount is unusually high compared to the amounts for that stream."""

    amount: OptionalNullable[float] = UNSET
    """The amount that the transaction differs from the stream average transaction amount."""


class CraVerificationIncomeTransactionOutlierDict(TypedDict):
    is_outlier: bool
    amount: NotRequired[float | None]
