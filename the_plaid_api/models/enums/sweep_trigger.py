from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SweepTrigger(str, Enum):
    """The trigger of the sweep

    ``"manual"`` - The sweep is created manually by the customer ``"incoming"`` - The sweep is created by incoming funds
    flow (e.g. Incoming Wire) ``"balance_threshold"`` - The sweep is created by balance threshold setting
    ``"automatic_aggregate"`` - The sweep is created by the Plaid automatic aggregation process. These funds did not
    pass through the Plaid Ledger balance."""

    MANUAL = "manual"
    INCOMING = "incoming"
    BALANCE_THRESHOLD = "balance_threshold"
    AUTOMATIC_AGGREGATE = "automatic_aggregate"

    __str__ = str.__str__


SweepTriggerOrStr: TypeAlias = Annotated[SweepTrigger | str, open_enum_validator(SweepTrigger)]
