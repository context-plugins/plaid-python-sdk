from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskCheckEmailIsEdu(str, Enum):
    """Indicates whether the email address domain is an educational institution domain if known."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskCheckEmailIsEduOrStr: TypeAlias = Annotated[RiskCheckEmailIsEdu | str, open_enum_validator(RiskCheckEmailIsEdu)]
