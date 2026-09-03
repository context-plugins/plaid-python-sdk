from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CashflowAttributesVersion(str, Enum):
    """The version of cashflow attributes. Required if using Cash Flow Insights."""

    V1_0 = "v1.0"
    V2_0 = "v2.0"
    CFI1 = "CFI1"

    __str__ = str.__str__


CashflowAttributesVersionOrStr: TypeAlias = Annotated[
    CashflowAttributesVersion | str, open_enum_validator(CashflowAttributesVersion)
]
