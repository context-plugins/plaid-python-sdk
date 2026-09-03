from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transactions_category_rule import TransactionsCategoryRule, TransactionsCategoryRuleDict


class TransactionsRulesListResponse(SdkBaseModel):
    """TransactionsRulesListResponse defines the response schema for ``/beta/transactions/rules/v1/list``"""

    rules: list[TransactionsCategoryRule]
    """A list of the user's transaction rules"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransactionsRulesListResponseDict(TypedDict):
    rules: list[TransactionsCategoryRule | TransactionsCategoryRuleDict]
    request_id: str
