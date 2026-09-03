from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationRefreshStatus(str, Enum):
    """The verification refresh status. One of the following:

    ``"VERIFICATION_REFRESH_STATUS_USER_PRESENCE_REQUIRED"`` User presence is required to refresh an income
    verification. ``"VERIFICATION_REFRESH_SUCCESSFUL"`` The income verification refresh was successful.
    ``"VERIFICATION_REFRESH_NOT_FOUND"`` No new data was found after the income verification refresh."""

    VERIFICATION_REFRESH_STATUS_USER_PRESENCE_REQUIRED = "VERIFICATION_REFRESH_STATUS_USER_PRESENCE_REQUIRED"
    VERIFICATION_REFRESH_SUCCESSFUL = "VERIFICATION_REFRESH_SUCCESSFUL"
    VERIFICATION_REFRESH_NOT_FOUND = "VERIFICATION_REFRESH_NOT_FOUND"

    __str__ = str.__str__


VerificationRefreshStatusOrStr: TypeAlias = Annotated[
    VerificationRefreshStatus | str, open_enum_validator(VerificationRefreshStatus)
]
