from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionsRuleField(str, Enum):
    """Transaction field for which the rule is defined."""

    TRANSACTION_ID = "TRANSACTION_ID"
    MERCHANT_NAME = "MERCHANT_NAME"

    __str__ = str.__str__


TransactionsRuleFieldOrStr: TypeAlias = Annotated[
    TransactionsRuleField | str, open_enum_validator(TransactionsRuleField)
]
