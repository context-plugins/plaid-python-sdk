from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditCategory(SdkBaseModel):
    """Information describing the intent of the transaction. Most relevant for credit use cases, but not limited to such
    use cases.

    See the https://plaid.com/documents/credit-category-taxonomy.csv for a full list of credit categories."""

    primary: str
    """A high level category that communicates the broad category of the transaction."""

    detailed: str
    """A granular category conveying the transaction's intent. This field can also be used as a unique identifier for
    the category."""


class CreditCategoryDict(TypedDict):
    primary: str
    detailed: str
