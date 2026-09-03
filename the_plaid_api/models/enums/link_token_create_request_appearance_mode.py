from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LinkTokenCreateRequestAppearanceMode(str, Enum):
    """Enum representing the desired appearance mode for Link, used to force light or dark modes or set Link to change
    depending on user system settings. Currently in closed beta."""

    LIGHT = "LIGHT"
    DARK = "DARK"
    SYSTEM = "SYSTEM"

    __str__ = str.__str__


LinkTokenCreateRequestAppearanceModeOrStr: TypeAlias = Annotated[
    LinkTokenCreateRequestAppearanceMode | str, open_enum_validator(LinkTokenCreateRequestAppearanceMode)
]
