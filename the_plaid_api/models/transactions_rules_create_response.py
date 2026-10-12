from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transactions_category_rule import TransactionsCategoryRule, TransactionsCategoryRuleDict


class TransactionsRulesCreateResponse(SdkBaseModel):
    """TransactionsRulesCreateResponse defines the response schema for ``/beta/transactions/rules/v1/create``"""

    rule: TransactionsCategoryRule
    """A representation of a transactions category rule."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransactionsRulesCreateResponseDict(TypedDict):
    rule: TransactionsCategoryRuleDict
    request_id: str
