from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraCreditProfileReportVersion(str, Enum):
    """The version of the credit profile report to retrieve."""

    V1 = "v1"

    __str__ = str.__str__


CraCreditProfileReportVersionOrStr: TypeAlias = Annotated[
    CraCreditProfileReportVersion | str, open_enum_validator(CraCreditProfileReportVersion)
]
