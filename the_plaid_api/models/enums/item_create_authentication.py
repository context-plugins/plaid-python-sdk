from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemCreateAuthentication(str, Enum):
    """Enum representing the entity authenticating the user."""

    UNKNOWN = "UNKNOWN"
    DATA_PARTNER = "DATA_PARTNER"
    PLAID = "PLAID"

    __str__ = str.__str__


ItemCreateAuthenticationOrStr: TypeAlias = Annotated[
    ItemCreateAuthentication | str, open_enum_validator(ItemCreateAuthentication)
]
