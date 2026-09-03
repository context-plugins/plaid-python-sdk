from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HolderCategory(str, Enum):
    """Indicates the account's categorization as either a personal or a business account. This field is currently in
    beta; to request access, contact your account manager."""

    BUSINESS = "business"
    PERSONAL = "personal"
    UNRECOGNIZED = "unrecognized"

    __str__ = str.__str__


HolderCategoryOrStr: TypeAlias = Annotated[HolderCategory | str, open_enum_validator(HolderCategory)]
