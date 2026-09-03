from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UpdateType(str, Enum):
    """Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some
    forms of two-factor authentication.

    ``background`` - Item can be updated in the background

    ``user_present_required`` - Item requires user interaction to be updated"""

    BACKGROUND = "background"
    USER_PRESENT_REQUIRED = "user_present_required"

    __str__ = str.__str__


UpdateTypeOrStr: TypeAlias = Annotated[UpdateType | str, open_enum_validator(UpdateType)]
