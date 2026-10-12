from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_identity_match_score import AccountIdentityMatchScore, AccountIdentityMatchScoreDict


class ProcessorIdentityMatchResponse(SdkBaseModel):
    """ProcessorIdentityMatchResponse defines the response schema for ``/processor/identity/match``"""

    account: AccountIdentityMatchScore
    """Identity match scores for an account"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorIdentityMatchResponseDict(TypedDict):
    account: AccountIdentityMatchScoreDict
    request_id: str
