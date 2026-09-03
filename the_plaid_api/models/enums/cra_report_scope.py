from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraReportScope(str, Enum):
    """Determines whose items are used. ``PLAID_NETWORK`` (default) uses the Plaid Network view of the user's profile.
    ``CLIENT_USER`` uses only the items linked by this client."""

    PLAID_NETWORK = "PLAID_NETWORK"
    CLIENT_USER = "CLIENT_USER"

    __str__ = str.__str__


CraReportScopeOrStr: TypeAlias = Annotated[CraReportScope | str, open_enum_validator(CraReportScope)]
