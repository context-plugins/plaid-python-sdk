from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account import Account, AccountDict


class ProcessorBalanceGetResponse(SdkBaseModel):
    """ProcessorBalanceGetResponse defines the response schema for ``/processor/balance/get``"""

    account: Account
    """A single account at a financial institution."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorBalanceGetResponseDict(TypedDict):
    account: AccountDict
    request_id: str
