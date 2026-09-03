from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FraudCheckOutcome(str, Enum):
    """The outcome of the fraud check.


    ``success`` - The check passed.

    ``failed`` - The check did not pass."""

    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


FraudCheckOutcomeOrStr: TypeAlias = Annotated[FraudCheckOutcome | str, open_enum_validator(FraudCheckOutcome)]
