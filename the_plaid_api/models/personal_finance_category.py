from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.personal_finance_category_version import PersonalFinanceCategoryVersionOrStr


class PersonalFinanceCategory(SdkBaseModel):
    """Information describing the intent of the transaction. Most relevant for personal finance use cases, but not
    limited to such use cases.

    See the `taxonomy CSV file <https://plaid.com/documents/pfc-taxonomy-all.csv>`__ for a full list of personal finance
    categories. If you are migrating to personal finance categories from the legacy categories, also refer to the
    `migration guide <https://plaid.com/docs/transactions/pfc-migration/>`__."""

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

    version: Optional[PersonalFinanceCategoryVersionOrStr] = UNSET
    """Indicates which version of the personal finance category taxonomy is being used. `View PFCv2 and PFCv1 taxonomies
    <https://plaid.com/documents/pfc-taxonomy-all.csv>`__.

    If you enabled Transactions or Enrich before December 3, 2025 you will receive the ``v1`` taxonomy by default and
    may request ``v2`` by explicitly setting this field to ``v2`` in the request.

    If you enabled Transactions or Enrich on or after December 3, 2025, you may only receive the ``v2`` taxonomy."""


class PersonalFinanceCategoryDict(TypedDict):
    primary: str
    detailed: str
    confidence_level: NotRequired[str | None]
    version: NotRequired[PersonalFinanceCategoryVersionOrStr]
