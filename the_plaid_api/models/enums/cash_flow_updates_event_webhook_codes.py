from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CashFlowUpdatesEventWebhookCodes(str, Enum):
    """Webhook code for a Cash Flow Updates event."""

    LARGE_DEPOSIT_DETECTED = "LARGE_DEPOSIT_DETECTED"
    LOW_BALANCE_DETECTED = "LOW_BALANCE_DETECTED"
    NEW_LOAN_PAYMENT_DETECTED = "NEW_LOAN_PAYMENT_DETECTED"
    NSF_OVERDRAFT_DETECTED = "NSF_OVERDRAFT_DETECTED"

    __str__ = str.__str__


CashFlowUpdatesEventWebhookCodesOrStr: TypeAlias = Annotated[
    CashFlowUpdatesEventWebhookCodes | str, open_enum_validator(CashFlowUpdatesEventWebhookCodes)
]
