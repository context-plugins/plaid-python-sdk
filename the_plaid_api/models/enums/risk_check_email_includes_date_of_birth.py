from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskCheckEmailIncludesDateOfBirth(str, Enum):
    """Indicates whether the email address includes the date of birth or year of birth if known."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskCheckEmailIncludesDateOfBirthOrStr: TypeAlias = Annotated[
    RiskCheckEmailIncludesDateOfBirth | str, open_enum_validator(RiskCheckEmailIncludesDateOfBirth)
]
