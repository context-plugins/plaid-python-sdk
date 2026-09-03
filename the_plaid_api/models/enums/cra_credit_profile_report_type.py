from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraCreditProfileReportType(str, Enum):
    """The product type for the credit profile report request."""

    QUALIFY = "QUALIFY"

    __str__ = str.__str__


CraCreditProfileReportTypeOrStr: TypeAlias = Annotated[
    CraCreditProfileReportType | str, open_enum_validator(CraCreditProfileReportType)
]
