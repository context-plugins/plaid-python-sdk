from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxOauthSelectAccountsRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/oauth/select_accounts``"""

    oauth_state_id: str
    accounts: list[str]


class SandboxOauthSelectAccountsRequestDict(TypedDict):
    oauth_state_id: str
    accounts: list[str]
