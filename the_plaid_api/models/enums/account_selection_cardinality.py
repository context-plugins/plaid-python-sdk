from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountSelectionCardinality(str, Enum):
    """The application requires that accounts be limited to a specific cardinality. ``MULTI_SELECT``: indicates that the
    user should be allowed to pick multiple accounts. ``SINGLE_SELECT``: indicates that the user should be allowed to
    pick only a single account. ``ALL``: indicates that the user must share all of their accounts and should not be
    given the opportunity to de-select"""

    SINGLE_SELECT = "SINGLE_SELECT"
    MULTI_SELECT = "MULTI_SELECT"
    ALL = "ALL"

    __str__ = str.__str__


AccountSelectionCardinalityOrStr: TypeAlias = Annotated[
    AccountSelectionCardinality | str, open_enum_validator(AccountSelectionCardinality)
]
