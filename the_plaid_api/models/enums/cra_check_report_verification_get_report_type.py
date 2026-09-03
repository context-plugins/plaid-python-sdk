from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraCheckReportVerificationGetReportType(str, Enum):
    """Type of home lending report."""

    VOA = "VOA"
    EMPLOYMENT_REFRESH = "EMPLOYMENT_REFRESH"
    INCOME = "INCOME"

    __str__ = str.__str__


CraCheckReportVerificationGetReportTypeOrStr: TypeAlias = Annotated[
    CraCheckReportVerificationGetReportType | str, open_enum_validator(CraCheckReportVerificationGetReportType)
]
