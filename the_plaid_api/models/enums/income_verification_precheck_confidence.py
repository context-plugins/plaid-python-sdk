from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomeVerificationPrecheckConfidence(str, Enum):
    """The confidence that Plaid can support the user in the digital income verification flow instead of requiring a
    manual paystub upload. One of the following:

    ``"HIGH"``: It is very likely that this user can use the digital income verification flow.

    "``LOW``": It is unlikely that this user can use the digital income verification flow.

    ``"UNKNOWN"``: It was not possible to determine if the user is supportable with the information passed."""

    HIGH = "HIGH"
    LOW = "LOW"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


IncomeVerificationPrecheckConfidenceOrStr: TypeAlias = Annotated[
    IncomeVerificationPrecheckConfidence | str, open_enum_validator(IncomeVerificationPrecheckConfidence)
]
