from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartyRoleType(str, Enum):
    """A value from a MISMO defined list that identifies the role that the party plays in the transaction. Parties may
    be either a person or legal entity. A party may play multiple roles in a transaction."""

    BORROWER = "Borrower"

    __str__ = str.__str__


PartyRoleTypeOrStr: TypeAlias = Annotated[PartyRoleType | str, open_enum_validator(PartyRoleType)]
