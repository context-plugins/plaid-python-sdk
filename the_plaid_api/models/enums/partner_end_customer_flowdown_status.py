from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartnerEndCustomerFlowdownStatus(str, Enum):
    """The status of the addendum to the Plaid MSA ("flowdown") for the end customer."""

    NOT_STARTED = "NOT_STARTED"
    IN_REVIEW = "IN_REVIEW"
    NEGOTIATION = "NEGOTIATION"
    COMPLETE = "COMPLETE"

    __str__ = str.__str__


PartnerEndCustomerFlowdownStatusOrStr: TypeAlias = Annotated[
    PartnerEndCustomerFlowdownStatus | str, open_enum_validator(PartnerEndCustomerFlowdownStatus)
]
