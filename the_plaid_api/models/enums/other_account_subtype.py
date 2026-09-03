from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OtherAccountSubtype(str, Enum):
    """Valid account subtypes for other accounts. For a list containing descriptions of each subtype, see `Account
    schemas <https://plaid.com/docs/api/accounts/#StandaloneAccountType-other>`__."""

    OTHER = "other"
    ALL = "all"

    __str__ = str.__str__


OtherAccountSubtypeOrStr: TypeAlias = Annotated[OtherAccountSubtype | str, open_enum_validator(OtherAccountSubtype)]
