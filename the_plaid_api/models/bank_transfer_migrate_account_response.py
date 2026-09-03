from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BankTransferMigrateAccountResponse(SdkBaseModel):
    """Defines the response schema for ``/bank_transfer/migrate_account``"""

    access_token: str
    """The Plaid ``access_token`` for the newly created Item."""

    account_id: str
    """The Plaid ``account_id`` for the newly created Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BankTransferMigrateAccountResponseDict(TypedDict):
    access_token: str
    account_id: str
    request_id: str
