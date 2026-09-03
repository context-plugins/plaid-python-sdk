from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_identity import AccountIdentity, AccountIdentityDict


class ProcessorIdentityGetResponse(SdkBaseModel):
    """ProcessorIdentityGetResponse defines the response schema for ``/processor/identity/get``"""

    account: AccountIdentity
    """Identity information about an account"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorIdentityGetResponseDict(TypedDict):
    account: AccountIdentity | AccountIdentityDict
    request_id: str
