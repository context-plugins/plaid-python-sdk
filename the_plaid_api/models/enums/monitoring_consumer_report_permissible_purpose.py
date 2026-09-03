from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MonitoringConsumerReportPermissiblePurpose(str, Enum):
    """Describes the reason you are generating a Consumer Report for this user.

    ``ACCOUNT_REVIEW_CREDIT``: In connection with a consumer credit transaction for the review or collection of an
    account pursuant to FCRA Section 604(a)(3)(A).

    ``WRITTEN_INSTRUCTION_OTHER``: In accordance with the written instructions of the consumer pursuant to FCRA Section
    604(a)(2), such as when an individual agrees to act as a guarantor or assumes personal liability for a consumer,
    business, or commercial loan."""

    ACCOUNT_REVIEW_CREDIT = "ACCOUNT_REVIEW_CREDIT"
    WRITTEN_INSTRUCTION_OTHER = "WRITTEN_INSTRUCTION_OTHER"

    __str__ = str.__str__


MonitoringConsumerReportPermissiblePurposeOrStr: TypeAlias = Annotated[
    MonitoringConsumerReportPermissiblePurpose | str, open_enum_validator(MonitoringConsumerReportPermissiblePurpose)
]
