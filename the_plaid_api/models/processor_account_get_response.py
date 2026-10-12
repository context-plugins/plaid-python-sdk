from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account import Account, AccountDict


class ProcessorAccountGetResponse(SdkBaseModel):
    """ProcessorAccountGetResponse defines the response schema for ``/processor/account/get``"""

    account: Account
    """A single account at a financial institution."""

    institution_id: str
    """The Plaid Institution ID associated with the Account."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorAccountGetResponseDict(TypedDict):
    account: AccountDict
    institution_id: str
    request_id: str
