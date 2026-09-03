from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferFundingAccount(SdkBaseModel):
    """The originator's funding account, linked with Plaid Link or ``/transfer/migrate_account``."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    account_id: str
    """The Plaid ``account_id`` for the newly created Item."""


class TransferFundingAccountDict(TypedDict):
    access_token: str
    account_id: str
