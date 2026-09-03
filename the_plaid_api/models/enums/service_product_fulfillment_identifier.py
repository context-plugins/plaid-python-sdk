from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ServiceProductFulfillmentIdentifier(str, Enum):
    """Documentation not found in the MISMO model viewer and not provided by Freddie Mac."""

    VOA = "VOA"
    VOE = "VOE"

    __str__ = str.__str__


ServiceProductFulfillmentIdentifierOrStr: TypeAlias = Annotated[
    ServiceProductFulfillmentIdentifier | str, open_enum_validator(ServiceProductFulfillmentIdentifier)
]
