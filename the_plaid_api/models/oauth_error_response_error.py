from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.oauth_error_code import OauthErrorCodeOrStr


class OauthErrorResponseError(SdkBaseModel):
    """OAuth error response"""

    error: Optional[OauthErrorCodeOrStr] = UNSET
    """OAuth error code"""

    error_description: Optional[str] = UNSET
    """A human-readable description of the error"""

    error_uri: Optional[str] = UNSET
    """A URI identifying the specific error"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class OauthErrorResponseErrorDict(TypedDict):
    error: NotRequired[OauthErrorCodeOrStr]
    error_description: NotRequired[str]
    error_uri: NotRequired[str]
    request_id: str
