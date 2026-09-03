from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IdentityUpdateTypes(str, Enum):
    """The possible types of identity data that may have changed."""

    PHONES = "PHONES"
    ADDRESSES = "ADDRESSES"
    EMAILS = "EMAILS"
    NAMES = "NAMES"

    __str__ = str.__str__


IdentityUpdateTypesOrStr: TypeAlias = Annotated[IdentityUpdateTypes | str, open_enum_validator(IdentityUpdateTypes)]
