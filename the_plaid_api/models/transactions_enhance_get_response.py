from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .client_provided_enhanced_transaction import (
    ClientProvidedEnhancedTransaction,
    ClientProvidedEnhancedTransactionDict,
)


class TransactionsEnhanceGetResponse(SdkBaseModel):
    """TransactionsEnhanceGetResponse defines the response schema for ``/beta/transactions/v1/enhance``."""

    enhanced_transactions: list[ClientProvidedEnhancedTransaction]
    """An array of enhanced transactions."""


class TransactionsEnhanceGetResponseDict(TypedDict):
    enhanced_transactions: list[ClientProvidedEnhancedTransactionDict]
