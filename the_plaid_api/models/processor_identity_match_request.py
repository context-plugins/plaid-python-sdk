from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .identity_match_user import IdentityMatchUser, IdentityMatchUserDict


class ProcessorIdentityMatchRequest(SdkBaseModel):
    """ProcessorIdentityMatchRequest defines the request schema for ``/processor/identity/match``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    processor_token: str
    """The processor token obtained from the Plaid integration partner. Processor tokens are in the format:
    ``processor-<environment>-<identifier>``"""

    user: Optional[IdentityMatchUser] = UNSET
    """The user's legal name, phone number, email address and address used to perform fuzzy match. If Financial Account
    Matching is enabled in the Identity Verification product, leave this field empty to automatically match against PII
    collected from the Identity Verification checks."""


class ProcessorIdentityMatchRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    processor_token: str
    user: NotRequired[IdentityMatchUserDict]
