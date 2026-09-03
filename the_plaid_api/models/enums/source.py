from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Source(str, Enum):
    """A type indicating who or what last touched this object. ``dashboard``, ``link``, and ``api`` indicate the
    originating surface; ``system`` indicates Plaid. ``retro`` indicates a screening created retroactively via a bulk
    screening creation."""

    DASHBOARD = "dashboard"
    LINK = "link"
    API = "api"
    SYSTEM = "system"
    RETRO = "retro"

    __str__ = str.__str__


SourceOrStr: TypeAlias = Annotated[Source | str, open_enum_validator(Source)]
