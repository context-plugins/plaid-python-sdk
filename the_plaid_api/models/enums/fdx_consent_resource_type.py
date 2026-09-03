from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FdxConsentResourceType(str, Enum):
    """Type of resource permissioned on a consent grant."""

    ACCOUNT = "ACCOUNT"
    CUSTOMER = "CUSTOMER"
    DOCUMENT = "DOCUMENT"

    __str__ = str.__str__


FdxConsentResourceTypeOrStr: TypeAlias = Annotated[
    FdxConsentResourceType | str, open_enum_validator(FdxConsentResourceType)
]
