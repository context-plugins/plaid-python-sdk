from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class BusinessFinanceCategory(SdkBaseModel):
    """Information describing the intent of the transaction. Most relevant for business finance use cases, but not
    limited to such use cases."""

    primary: str
    """A high level category that communicates the broad category of the transaction."""

    detailed: str
    """A granular category conveying the transaction's intent. This field can also be used as a unique identifier for
    the category."""

    confidence_level: OptionalNullable[str] = UNSET
    """A description of how confident we are that the provided categories accurately describe the transaction intent.

    ``VERY_HIGH``: We are more than 98% confident that this category reflects the intent of the transaction. ``HIGH``:
    We are more than 90% confident that this category reflects the intent of the transaction. ``MEDIUM``: We are
    moderately confident that this category reflects the intent of the transaction. ``LOW``: This category may reflect
    the intent, but there may be other categories that are more accurate. ``UNKNOWN``: We don't know the confidence
    level for this category."""


class BusinessFinanceCategoryDict(TypedDict):
    primary: str
    detailed: str
    confidence_level: NotRequired[str | None]
