from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessCheckBooleanStatus(str, Enum):
    """Tri-state boolean status, where ``no_data`` indicates the check could not determine a value."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


BusinessCheckBooleanStatusOrStr: TypeAlias = Annotated[
    BusinessCheckBooleanStatus | str, open_enum_validator(BusinessCheckBooleanStatus)
]
