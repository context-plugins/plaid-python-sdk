from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_identity_match_score import AccountIdentityMatchScore, AccountIdentityMatchScoreDict
from .item import Item, ItemDict


class IdentityMatchResponse(SdkBaseModel):
    """IdentityMatchResponse defines the response schema for ``/identity/match``"""

    accounts: list[AccountIdentityMatchScore]
    """The accounts for which Identity match has been requested"""

    item: Item
    """Metadata about the Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IdentityMatchResponseDict(TypedDict):
    accounts: list[AccountIdentityMatchScore | AccountIdentityMatchScoreDict]
    item: Item | ItemDict
    request_id: str
