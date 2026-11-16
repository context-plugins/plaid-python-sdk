from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GseReportType(str, Enum):
    """The types of GSE Reports supported by the Plaid API"""

    VOA = "VOA"
    EMPLOYMENT_REFRESH = "EMPLOYMENT_REFRESH"

    __str__ = str.__str__


GseReportTypeOrStr: TypeAlias = Annotated[GseReportType | str, open_enum_validator(GseReportType)]
