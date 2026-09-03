from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferDiligenceStatus(str, Enum):
    """Originator's diligence status."""

    NOT_SUBMITTED = "not_submitted"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    DENIED = "denied"
    MORE_INFORMATION_REQUIRED = "more_information_required"

    __str__ = str.__str__


TransferDiligenceStatusOrStr: TypeAlias = Annotated[
    TransferDiligenceStatus | str, open_enum_validator(TransferDiligenceStatus)
]
