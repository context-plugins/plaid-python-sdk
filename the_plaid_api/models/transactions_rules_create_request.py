from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transactions_rule_details import TransactionsRuleDetails, TransactionsRuleDetailsDict


class TransactionsRulesCreateRequest(SdkBaseModel):
    """TransactionsRulesCreateRequest defines the request schema for ``/beta/transactions/rules/v1/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_user_id: str
    """A unique ID representing the end user. This ID is used to associate rules with a specific user."""

    pfc_primary_category: str
    """A personal finance primary category. See the `taxonomy csv file
    <https://plaid.com/documents/pfc-taxonomy-all.csv>`__ for a full list of personal finance categories."""

    pfc_detailed_category: str
    """A personal finance detailed category. See the `taxonomy csv file
    <https://plaid.com/documents/pfc-taxonomy-all.csv>`__ for a full list of personal finance categories."""

    rule_details: TransactionsRuleDetails
    """A representation of transactions rule details."""


class TransactionsRulesCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    client_user_id: str
    pfc_primary_category: str
    pfc_detailed_category: str
    rule_details: TransactionsRuleDetailsDict
