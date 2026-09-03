from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferGuaranteeOutcome(str, Enum):
    """The adaptive guarantee outcome for a transfer.

    ``FULL_INSTANT``: The full transfer amount is guaranteed and funds are available instantly.

    ``PARTIAL_INSTANT_ONLY``: A partial amount is guaranteed and available instantly; the remainder is not guaranteed.

    ``PARTIAL_INSTANT_WITH_OBSERVATION_WINDOW``: A partial amount is guaranteed instantly; an additional amount is
    conditionally guaranteed subject to an observation window.

    ``NOT_GUARANTEED``: Plaid did not provide a guarantee for this transfer."""

    FULL_INSTANT = "FULL_INSTANT"
    PARTIAL_INSTANT_ONLY = "PARTIAL_INSTANT_ONLY"
    PARTIAL_INSTANT_WITH_OBSERVATION_WINDOW = "PARTIAL_INSTANT_WITH_OBSERVATION_WINDOW"
    NOT_GUARANTEED = "NOT_GUARANTEED"

    __str__ = str.__str__


TransferGuaranteeOutcomeOrStr: TypeAlias = Annotated[
    TransferGuaranteeOutcome | str, open_enum_validator(TransferGuaranteeOutcome)
]
