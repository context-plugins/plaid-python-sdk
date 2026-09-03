from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .client_provided_enriched_transaction import (
    ClientProvidedEnrichedTransaction,
    ClientProvidedEnrichedTransactionDict,
)


class TransactionsEnrichResponse(SdkBaseModel):
    """TransactionsEnrichResponse defines the response schema for ``/transactions/enrich``."""

    enriched_transactions: list[ClientProvidedEnrichedTransaction]
    """A list of enriched transactions."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransactionsEnrichResponseDict(TypedDict):
    enriched_transactions: list[ClientProvidedEnrichedTransaction | ClientProvidedEnrichedTransactionDict]
    request_id: NotRequired[str]
