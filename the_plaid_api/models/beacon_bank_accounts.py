from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .beacon_bank_account_insights import BeaconBankAccountInsights, BeaconBankAccountInsightsDict


class BeaconBankAccounts(SdkBaseModel):
    """A collection of Bank Accounts linked to an Item that is associated with this Beacon User."""

    item_id: str
    """The Plaid Item ID the Bank Accounts belong to."""

    accounts: list[BeaconBankAccountInsights]


class BeaconBankAccountsDict(TypedDict):
    item_id: str
    accounts: list[BeaconBankAccountInsightsDict]
