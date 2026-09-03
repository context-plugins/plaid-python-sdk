from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferOriginatorFundingAccountCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/originator/funding_account/create``"""

    funding_account_id: Optional[str] = UNSET
    """The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business
    checking accounts will be credited or debited."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferOriginatorFundingAccountCreateResponseDict(TypedDict):
    funding_account_id: NotRequired[str]
    request_id: str
