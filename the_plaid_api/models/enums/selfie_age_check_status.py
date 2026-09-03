from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SelfieAgeCheckStatus(str, Enum):
    """An enum indicating whether the reported age aligns with the estimated selfie capture age range.

    ``match`` indicates that the reported age falls within the estimated selfie capture age range.

    ``warning`` indicates that the reported age falls outside the estimated selfie capture age range, but is close
    enough that the result should be reviewed.

    ``no_match`` indicates that the reported age falls far outside the estimated selfie capture age range.

    ``no_data`` indicates that there was not enough data available at age-estimation time to compare the reported age
    against the estimated selfie capture age range."""

    MATCH = "match"
    WARNING = "warning"
    NO_MATCH = "no_match"
    NO_DATA = "no_data"

    __str__ = str.__str__


SelfieAgeCheckStatusOrStr: TypeAlias = Annotated[SelfieAgeCheckStatus | str, open_enum_validator(SelfieAgeCheckStatus)]
