from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.personal_finance_category_version import PersonalFinanceCategoryVersionOrStr


class TransactionsEnrichRequestOptions(SdkBaseModel):
    """An optional object to be used with the request."""

    include_legacy_category: Optional[bool] = UNSET
    """Include ``legacy_category`` and ``legacy_category_id`` in the response (in addition to the default
    ``personal_finance_category``).

    Categories are based on Plaid's legacy taxonomy. For a full list of legacy categories, see
    https://plaid.com/docs/api/products/transactions/#categoriesget."""

    personal_finance_category_version: Optional[PersonalFinanceCategoryVersionOrStr] = UNSET
    """Indicates which version of the personal finance category taxonomy is being used. `View PFCv2 and PFCv1 taxonomies
    <https://plaid.com/documents/pfc-taxonomy-all.csv>`__.

    If you enabled Transactions or Enrich before December 3, 2025 you will receive the ``v1`` taxonomy by default and
    may request ``v2`` by explicitly setting this field to ``v2`` in the request.

    If you enabled Transactions or Enrich on or after December 3, 2025, you may only receive the ``v2`` taxonomy."""


class TransactionsEnrichRequestOptionsDict(TypedDict):
    include_legacy_category: NotRequired[bool]
    personal_finance_category_version: NotRequired[PersonalFinanceCategoryVersionOrStr]
