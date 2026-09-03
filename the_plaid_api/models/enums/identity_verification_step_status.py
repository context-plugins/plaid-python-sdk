from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdentityVerificationStepStatus(str, Enum):
    """The status of a step in the Identity Verification process."""

    SUCCESS = "success"
    ACTIVE = "active"
    FAILED = "failed"
    WAITING_FOR_PREREQUISITE = "waiting_for_prerequisite"
    NOT_APPLICABLE = "not_applicable"
    SKIPPED = "skipped"
    EXPIRED = "expired"
    CANCELED = "canceled"
    PENDING_REVIEW = "pending_review"
    MANUALLY_APPROVED = "manually_approved"
    MANUALLY_REJECTED = "manually_rejected"

    __str__ = str.__str__


IdentityVerificationStepStatusOrStr: TypeAlias = Annotated[
    IdentityVerificationStepStatus | str, open_enum_validator(IdentityVerificationStepStatus)
]
