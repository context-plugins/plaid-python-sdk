from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FraudCheckOutcomeWithNoData(str, Enum):
    """The outcome of the fraud check.


    ``success`` - The check passed.

    ``failed`` - The check did not pass.

    ``no_data`` - The check could not be performed due to insufficient data."""

    SUCCESS = "success"
    FAILED = "failed"
    NO_DATA = "no_data"

    __str__ = str.__str__


FraudCheckOutcomeWithNoDataOrStr: TypeAlias = Annotated[
    FraudCheckOutcomeWithNoData | str, open_enum_validator(FraudCheckOutcomeWithNoData)
]
