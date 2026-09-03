from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.personal_finance_category_version import PersonalFinanceCategoryVersionOrStr
from .transaction_stream import TransactionStream, TransactionStreamDict


class TransactionsRecurringGetResponse(SdkBaseModel):
    """TransactionsRecurringGetResponse defines the response schema for ``/transactions/recurring/get``"""

    inflow_streams: list[TransactionStream]
    """An array of inflow transaction streams."""

    outflow_streams: list[TransactionStream]
    """An array of expense transaction streams."""

    updated_datetime: RFC3339DateTime
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (``YYYY-MM-DDTHH:mm:ssZ``) indicating the
    last time transaction streams for the given account were updated on"""

    personal_finance_category_version: Optional[PersonalFinanceCategoryVersionOrStr] = UNSET
    """Indicates which version of the personal finance category taxonomy is being used. `View PFCv2 and PFCv1 taxonomies
    <https://plaid.com/documents/pfc-taxonomy-all.csv>`__.

    If you enabled Transactions or Enrich before December 3, 2025 you will receive the ``v1`` taxonomy by default and
    may request ``v2`` by explicitly setting this field to ``v2`` in the request.

    If you enabled Transactions or Enrich on or after December 3, 2025, you may only receive the ``v2`` taxonomy."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransactionsRecurringGetResponseDict(TypedDict):
    inflow_streams: list[TransactionStream | TransactionStreamDict]
    outflow_streams: list[TransactionStream | TransactionStreamDict]
    updated_datetime: RFC3339DateTime
    personal_finance_category_version: NotRequired[PersonalFinanceCategoryVersionOrStr]
    request_id: str
