from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OauthErrorCode(str, Enum):
    """OAuth error code"""

    INVALID_REQUEST = "invalid_request"
    INVALID_CLIENT = "invalid_client"
    INVALID_GRANT = "invalid_grant"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    INVALID_SCOPE = "invalid_scope"
    UNSUPPORTED_GRANT_TYPE = "unsupported_grant_type"

    __str__ = str.__str__


OauthErrorCodeOrStr: TypeAlias = Annotated[OauthErrorCode | str, open_enum_validator(OauthErrorCode)]
