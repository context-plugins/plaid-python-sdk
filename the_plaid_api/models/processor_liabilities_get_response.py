from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account import Account, AccountDict
from .liabilities_object import LiabilitiesObject, LiabilitiesObjectDict


class ProcessorLiabilitiesGetResponse(SdkBaseModel):
    """ProcessorLiabilitiesGetResponse defines the response schema for ``/processor/liabilities/get``"""

    account: Account
    """A single account at a financial institution."""

    liabilities: LiabilitiesObject
    """An object containing liability accounts"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorLiabilitiesGetResponseDict(TypedDict):
    account: AccountDict
    liabilities: LiabilitiesObjectDict
    request_id: str
