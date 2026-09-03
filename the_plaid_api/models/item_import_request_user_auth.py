from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ItemImportRequestUserAuth(SdkBaseModel):
    """Object of user ID and auth token pair, permitting Plaid to aggregate a user's accounts"""

    user_id: str
    """Opaque user identifier"""

    auth_token: str
    """Authorization token Plaid will use to aggregate this user's accounts"""


class ItemImportRequestUserAuthDict(TypedDict):
    user_id: str
    auth_token: str
