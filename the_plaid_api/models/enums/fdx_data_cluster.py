from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FdxDataCluster(str, Enum):
    """Name of a cluster of data elements permissioned by a consent grant."""

    ACCOUNT_BASIC = "ACCOUNT_BASIC"
    ACCOUNT_DETAILED = "ACCOUNT_DETAILED"
    ACCOUNT_PAYMENTS = "ACCOUNT_PAYMENTS"
    BILLS = "BILLS"
    CUSTOMER_CONTACT = "CUSTOMER_CONTACT"
    CUSTOMER_PERSONAL = "CUSTOMER_PERSONAL"
    IMAGES = "IMAGES"
    INVESTMENTS = "INVESTMENTS"
    NOTIFICATIONS = "NOTIFICATIONS"
    PAYMENT_SUPPORT = "PAYMENT_SUPPORT"
    REWARDS = "REWARDS"
    STATEMENTS = "STATEMENTS"
    TAX = "TAX"
    TRANSACTIONS = "TRANSACTIONS"
    BALANCES = "BALANCES"
    SCHEDULED_PAYMENTS = "SCHEDULED_PAYMENTS"

    __str__ = str.__str__


FdxDataClusterOrStr: TypeAlias = Annotated[FdxDataCluster | str, open_enum_validator(FdxDataCluster)]
