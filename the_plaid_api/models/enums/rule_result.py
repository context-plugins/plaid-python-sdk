from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RuleResult(str, Enum):
    """The result of the rule that was triggered for this transaction.

    ``ACCEPT``: Accept the transaction for processing. ``REROUTE``: Reroute the transaction to a different payment
    method, as this transaction is too risky. ``REVIEW``: Review the transaction before proceeding."""

    ACCEPT = "ACCEPT"
    REROUTE = "REROUTE"
    REVIEW = "REVIEW"

    __str__ = str.__str__


RuleResultOrStr: TypeAlias = Annotated[RuleResult | str, open_enum_validator(RuleResult)]
