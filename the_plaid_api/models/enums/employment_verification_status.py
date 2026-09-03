from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EmploymentVerificationStatus(str, Enum):
    """Current employment status."""

    EMPLOYMENT_STATUS_ACTIVE = "EMPLOYMENT_STATUS_ACTIVE"
    EMPLOYMENT_STATUS_INACTIVE = "EMPLOYMENT_STATUS_INACTIVE"

    __str__ = str.__str__


EmploymentVerificationStatusOrStr: TypeAlias = Annotated[
    EmploymentVerificationStatus | str, open_enum_validator(EmploymentVerificationStatus)
]
