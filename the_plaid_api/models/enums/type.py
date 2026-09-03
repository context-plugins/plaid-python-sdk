from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type(str, Enum):
    """The type of phone number."""

    HOME = "home"
    WORK = "work"
    OFFICE = "office"
    MOBILE = "mobile"
    MOBILE1 = "mobile1"
    OTHER = "other"

    __str__ = str.__str__


TypeOrStr: TypeAlias = Annotated[Type | str, open_enum_validator(Type)]
