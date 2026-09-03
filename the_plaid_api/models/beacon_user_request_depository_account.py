from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BeaconUserRequestDepositoryAccount(SdkBaseModel):
    """Depository account information for the associated user."""

    account_number: str
    """Must be a valid US Bank Account Number"""

    routing_number: str
    """The routing number of the account."""


class BeaconUserRequestDepositoryAccountDict(TypedDict):
    account_number: str
    routing_number: str
