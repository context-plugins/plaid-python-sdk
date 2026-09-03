from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AuthUpdateTypes(str, Enum):
    """The possible types of auth data that may have changed."""

    ACCOUNT_NUMBER = "ACCOUNT_NUMBER"
    ROUTING_NUMBER = "ROUTING_NUMBER"

    __str__ = str.__str__


AuthUpdateTypesOrStr: TypeAlias = Annotated[AuthUpdateTypes | str, open_enum_validator(AuthUpdateTypes)]
