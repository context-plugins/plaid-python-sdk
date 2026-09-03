from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionsRuleType(str, Enum):
    """Transaction rule's match type. For ``TRANSACTION_ID`` field, ``EXACT_MATCH`` is available. Matches are case
    sensitive."""

    EXACT_MATCH = "EXACT_MATCH"
    SUBSTRING_MATCH = "SUBSTRING_MATCH"

    __str__ = str.__str__


TransactionsRuleTypeOrStr: TypeAlias = Annotated[TransactionsRuleType | str, open_enum_validator(TransactionsRuleType)]
