from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionsUpdateStatus(str, Enum):
    """A description of the update status for transaction pulls of an Item. This field contains the same information
    provided by transactions webhooks, and may be helpful for webhook troubleshooting or when recovering from missed
    webhooks.

    ``TRANSACTIONS_UPDATE_STATUS_UNKNOWN``: Unable to fetch transactions update status for Item. ``NOT_READY``: The Item
    is pending transaction pull. ``INITIAL_UPDATE_COMPLETE``: Initial pull for the Item is complete, historical pull is
    pending. ``HISTORICAL_UPDATE_COMPLETE``: Both initial and historical pull for Item are complete."""

    TRANSACTIONS_UPDATE_STATUS_UNKNOWN = "TRANSACTIONS_UPDATE_STATUS_UNKNOWN"
    NOT_READY = "NOT_READY"
    INITIAL_UPDATE_COMPLETE = "INITIAL_UPDATE_COMPLETE"
    HISTORICAL_UPDATE_COMPLETE = "HISTORICAL_UPDATE_COMPLETE"

    __str__ = str.__str__


TransactionsUpdateStatusOrStr: TypeAlias = Annotated[
    TransactionsUpdateStatus | str, open_enum_validator(TransactionsUpdateStatus)
]
