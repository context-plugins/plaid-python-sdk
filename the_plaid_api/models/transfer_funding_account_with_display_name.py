from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferFundingAccountWithDisplayName(SdkBaseModel):
    """The originator's funding account, linked with Plaid Link or ``/transfer/migrate_account``."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    account_id: str
    """The Plaid ``account_id`` for the newly created Item."""

    display_name: Optional[str] = UNSET
    """The name for the funding account that is displayed in the Plaid dashboard."""


class TransferFundingAccountWithDisplayNameDict(TypedDict):
    access_token: str
    account_id: str
    display_name: NotRequired[str]
