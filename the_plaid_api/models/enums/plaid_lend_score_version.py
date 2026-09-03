from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PlaidLendScoreVersion(str, Enum):
    """The version of the LendScore to use. Required if using LendScore."""

    V1_0 = "v1.0"
    V2_0 = "v2.0"
    LS1 = "LS1"

    __str__ = str.__str__


PlaidLendScoreVersionOrStr: TypeAlias = Annotated[
    PlaidLendScoreVersion | str, open_enum_validator(PlaidLendScoreVersion)
]
