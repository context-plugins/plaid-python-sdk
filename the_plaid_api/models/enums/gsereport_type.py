from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GsereportType(str, Enum):
    """The types of GSE Reports supported by the Plaid API"""

    VOA = "VOA"
    EMPLOYMENT_REFRESH = "EMPLOYMENT_REFRESH"

    __str__ = str.__str__


GsereportTypeOrStr: TypeAlias = Annotated[GsereportType | str, open_enum_validator(GsereportType)]
