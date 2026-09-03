from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PhoneType(str, Enum):
    """An enum indicating whether a phone number is a phone line or a fax line."""

    PHONE = "phone"
    FAX = "fax"

    __str__ = str.__str__


PhoneTypeOrStr: TypeAlias = Annotated[PhoneType | str, open_enum_validator(PhoneType)]
