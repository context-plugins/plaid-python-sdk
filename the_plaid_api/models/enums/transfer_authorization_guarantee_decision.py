from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferAuthorizationGuaranteeDecision(str, Enum):
    """Indicates whether the transfer is guaranteed by Plaid (Guarantee customers only). This field will contain either
    ``GUARANTEED`` or ``NOT_GUARANTEED`` indicating whether Plaid will guarantee the transfer."""

    GUARANTEED = "GUARANTEED"
    NOT_GUARANTEED = "NOT_GUARANTEED"

    __str__ = str.__str__


TransferAuthorizationGuaranteeDecisionOrStr: TypeAlias = Annotated[
    TransferAuthorizationGuaranteeDecision | str, open_enum_validator(TransferAuthorizationGuaranteeDecision)
]
