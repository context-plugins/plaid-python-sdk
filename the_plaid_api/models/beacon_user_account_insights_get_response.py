from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .beacon_bank_accounts import BeaconBankAccounts, BeaconBankAccountsDict


class BeaconUserAccountInsightsGetResponse(SdkBaseModel):
    """The response schema for ``/beacon/user/account_insights/get``"""

    beacon_user_id: str
    """ID of the associated Beacon User."""

    created_at: RFC3339DateTime
    """An ISO8601 formatted timestamp."""

    updated_at: RFC3339DateTime
    """An ISO8601 formatted timestamp. This field indicates the last time the resource was modified."""

    bank_account_insights: BeaconBankAccounts
    """A collection of Bank Accounts linked to an Item that is associated with this Beacon User."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BeaconUserAccountInsightsGetResponseDict(TypedDict):
    beacon_user_id: str
    created_at: RFC3339DateTime
    updated_at: RFC3339DateTime
    bank_account_insights: BeaconBankAccountsDict
    request_id: str
