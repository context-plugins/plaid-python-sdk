from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReportType(str, Enum):
    """The report type. It can be ``asset``. Income report types are not yet supported."""

    ASSET = "asset"

    __str__ = str.__str__


ReportTypeOrStr: TypeAlias = Annotated[ReportType | str, open_enum_validator(ReportType)]
