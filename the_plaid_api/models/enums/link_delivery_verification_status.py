from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LinkDeliveryVerificationStatus(str, Enum):
    """Indicates an Item's micro-deposit-based verification or database verification status."""

    AUTOMATICALLY_VERIFIED = "automatically_verified"
    PENDING_AUTOMATIC_VERIFICATION = "pending_automatic_verification"
    PENDING_MANUAL_VERIFICATION = "pending_manual_verification"
    MANUALLY_VERIFIED = "manually_verified"
    VERIFICATION_EXPIRED = "verification_expired"
    VERIFICATION_FAILED = "verification_failed"
    UNSENT = "unsent"
    DATABASE_MATCHED = "database_matched"
    DATABASE_INSIGHTS_PENDING = "database_insights_pending"

    __str__ = str.__str__


LinkDeliveryVerificationStatusOrStr: TypeAlias = Annotated[
    LinkDeliveryVerificationStatus | str, open_enum_validator(LinkDeliveryVerificationStatus)
]
