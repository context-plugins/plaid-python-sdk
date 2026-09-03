from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraCheckReportVerificationPdfReportType(str, Enum):
    """The type of verification PDF report to fetch."""

    VOA = "voa"
    EMPLOYMENT_REFRESH = "employment_refresh"
    INCOME = "income"

    __str__ = str.__str__


CraCheckReportVerificationPdfReportTypeOrStr: TypeAlias = Annotated[
    CraCheckReportVerificationPdfReportType | str, open_enum_validator(CraCheckReportVerificationPdfReportType)
]
