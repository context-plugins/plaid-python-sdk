from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraVerificationIncomeCategory(SdkBaseModel):
    """The income category for a given stream. The streams returned in the response will be filtered based on these
    primary and secondary income categories.

    See the `Income V2 Category Taxonomy <https://plaid.com/documents/income-v2-category-taxonomy.csv>`__ for a full
    list of income categories."""

    primary: str
    """A high level category that communicates the broad category of the stream."""

    secondary: str
    """A granular category conveying the stream's intent."""


class CraVerificationIncomeCategoryDict(TypedDict):
    primary: str
    secondary: str
