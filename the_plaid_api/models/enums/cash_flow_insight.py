from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CashFlowInsight(str, Enum):
    """An insight that can be detected by the Cash Flow Updates product"""

    LARGE_DEPOSIT_DETECTED = "LARGE_DEPOSIT_DETECTED"
    LOW_BALANCE_DETECTED = "LOW_BALANCE_DETECTED"
    NEW_LOAN_PAYMENT_DETECTED = "NEW_LOAN_PAYMENT_DETECTED"
    NSF_OVERDRAFT_DETECTED = "NSF_OVERDRAFT_DETECTED"

    __str__ = str.__str__


CashFlowInsightOrStr: TypeAlias = Annotated[CashFlowInsight | str, open_enum_validator(CashFlowInsight)]
