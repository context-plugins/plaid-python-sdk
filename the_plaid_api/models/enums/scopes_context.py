from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScopesContext(str, Enum):
    """An indicator for when scopes are being updated. When scopes are updated via enrollment (i.e. OAuth), the partner
    must send ``ENROLLMENT``. When scopes are updated in a post-enrollment view, the partner must send ``PORTAL``."""

    ENROLLMENT = "ENROLLMENT"
    PORTAL = "PORTAL"

    __str__ = str.__str__


ScopesContextOrStr: TypeAlias = Annotated[ScopesContext | str, open_enum_validator(ScopesContext)]
