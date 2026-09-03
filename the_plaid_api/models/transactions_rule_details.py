from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.transactions_rule_field import TransactionsRuleFieldOrStr
from .enums.transactions_rule_type import TransactionsRuleTypeOrStr


class TransactionsRuleDetails(SdkBaseModel):
    """A representation of transactions rule details."""

    field: TransactionsRuleFieldOrStr
    """Transaction field for which the rule is defined."""

    type_: TransactionsRuleTypeOrStr = Field(alias="type")
    """Transaction rule's match type. For ``TRANSACTION_ID`` field, ``EXACT_MATCH`` is available. Matches are case
    sensitive."""

    query: str
    """For ``TRANSACTION_ID`` field, provide ``transaction_id``. For ``MERCHANT_NAME`` field, provide a string
    pattern."""


class TransactionsRuleDetailsDict(TypedDict):
    field: TransactionsRuleFieldOrStr
    type_: TransactionsRuleTypeOrStr
    query: str
