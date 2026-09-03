from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class BeaconUserDepositoryAccount(SdkBaseModel):
    """Depository account information for the associated user."""

    account_mask: str
    """The last 2-4 numeric characters of this account's account number."""

    routing_number: str
    """The routing number of the account."""

    added_at: RFC3339DateTime
    """An ISO8601 formatted timestamp."""


class BeaconUserDepositoryAccountDict(TypedDict):
    account_mask: str
    routing_number: str
    added_at: RFC3339DateTime
