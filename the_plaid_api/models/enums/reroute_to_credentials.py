from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RerouteToCredentials(str, Enum):
    """Specifies what type of `Reroute to Credentials
    <https://plaid.com/docs/auth/coverage/flow-options/#removing-manual-verification-entry-points-with-reroute-to-credentials>`__
    pane should be used in the Link session for the Same-Day Micro-deposits flow. Default behavior is ``OPTIONAL``."""

    OFF = "OFF"
    OPTIONAL = "OPTIONAL"
    FORCED = "FORCED"

    __str__ = str.__str__


RerouteToCredentialsOrStr: TypeAlias = Annotated[RerouteToCredentials | str, open_enum_validator(RerouteToCredentials)]
