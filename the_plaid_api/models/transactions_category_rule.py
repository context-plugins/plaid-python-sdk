from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .transactions_rule_details import TransactionsRuleDetails, TransactionsRuleDetailsDict


class TransactionsCategoryRule(SdkBaseModel):
    """A representation of a transactions category rule."""

    id: Optional[str] = UNSET
    """A unique identifier of the rule created"""

    user_id: Optional[str] = UNSET
    """The Plaid-generated unique identifier for the end user this rule belongs to."""

    created_at: Optional[RFC3339DateTime] = UNSET
    """Date and time when a rule was created in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DDTHH:mm:ssZ`` )."""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """Date and time when a rule was last updated in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DDTHH:mm:ssZ`` )."""

    pfc_primary_category: Optional[str] = UNSET
    """A personal finance primary category. See the `taxonomy csv file
    <https://plaid.com/documents/pfc-taxonomy-all.csv>`__ for a full list of personal finance categories."""

    pfc_detailed_category: Optional[str] = UNSET
    """A personal finance detailed category. See the `taxonomy csv file
    <https://plaid.com/documents/pfc-taxonomy-all.csv>`__ for a full list of personal finance categories."""

    rule_details: Optional[TransactionsRuleDetails] = UNSET
    """A representation of transactions rule details."""


class TransactionsCategoryRuleDict(TypedDict):
    id: NotRequired[str]
    user_id: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    pfc_primary_category: NotRequired[str]
    pfc_detailed_category: NotRequired[str]
    rule_details: NotRequired[TransactionsRuleDetailsDict]
