from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProtectReportSource(str, Enum):
    """The source that identified or reported the incident.

    ``INTERNAL_REVIEW`` - Incident was identified through internal fraud investigations or review processes.

    ``USER_SELF_REPORTED`` - Incident was reported directly by the affected user.

    ``BANK_FEEDBACK`` - Incident was identified through bank feedback, including ACH returns and connection revocations.

    ``NETWORK_FEEDBACK`` - Incident was identified through card network alerts or chargebacks.

    ``AUTOMATED_SYSTEM`` - Incident was detected by automated systems such as fraud models or rule engines.

    ``THIRD_PARTY_ALERT`` - Incident was identified through external vendor or consortium alerts.

    ``OTHER`` - Incident was identified through a source not covered by other categories."""

    INTERNAL_REVIEW = "INTERNAL_REVIEW"
    USER_SELF_REPORTED = "USER_SELF_REPORTED"
    BANK_FEEDBACK = "BANK_FEEDBACK"
    NETWORK_FEEDBACK = "NETWORK_FEEDBACK"
    AUTOMATED_SYSTEM = "AUTOMATED_SYSTEM"
    THIRD_PARTY_ALERT = "THIRD_PARTY_ALERT"
    OTHER = "OTHER"

    __str__ = str.__str__


ProtectReportSourceOrStr: TypeAlias = Annotated[ProtectReportSource | str, open_enum_validator(ProtectReportSource)]
