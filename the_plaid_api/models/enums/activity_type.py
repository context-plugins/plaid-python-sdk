from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ActivityType(str, Enum):
    """Types of consent activities"""

    UNKNOWN = "UNKNOWN"
    ITEM_CREATE = "ITEM_CREATE"
    ITEM_IMPORT = "ITEM_IMPORT"
    ITEM_UPDATE = "ITEM_UPDATE"
    ITEM_UNLINK = "ITEM_UNLINK"
    PORTAL_UNLINK = "PORTAL_UNLINK"
    PORTAL_ITEMS_DELETE = "PORTAL_ITEMS_DELETE"
    ITEM_REMOVE = "ITEM_REMOVE"
    INVARIANT_CHECKER_DELETION = "INVARIANT_CHECKER_DELETION"
    SCOPES_UPDATE = "SCOPES_UPDATE"

    __str__ = str.__str__


ActivityTypeOrStr: TypeAlias = Annotated[ActivityType | str, open_enum_validator(ActivityType)]
