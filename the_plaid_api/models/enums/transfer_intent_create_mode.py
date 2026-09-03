from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferIntentCreateMode(str, Enum):
    """The direction of the flow of transfer funds.

    ``PAYMENT``: Transfers funds from an end user's account to your business account.

    ``DISBURSEMENT``: Transfers funds from your business account to an end user's account."""

    PAYMENT = "PAYMENT"
    DISBURSEMENT = "DISBURSEMENT"

    __str__ = str.__str__


TransferIntentCreateModeOrStr: TypeAlias = Annotated[
    TransferIntentCreateMode | str, open_enum_validator(TransferIntentCreateMode)
]
