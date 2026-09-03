from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConsentEventInitiator(str, Enum):
    """The entity that initiated collection of consent."""

    PLAID = "PLAID"
    DATA_PROVIDER = "DATA_PROVIDER"
    CUSTOMER = "CUSTOMER"
    END_USER = "END_USER"

    __str__ = str.__str__


ConsentEventInitiatorOrStr: TypeAlias = Annotated[
    ConsentEventInitiator | str, open_enum_validator(ConsentEventInitiator)
]
