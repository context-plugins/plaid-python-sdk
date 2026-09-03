from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TransferLedgerGetRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/ledger/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    ledger_id: OptionalNullable[str] = UNSET
    """Specify which ledger balance to get. Customers can find a list of ``ledger_id``s in the Accounts page of your
    Plaid Dashboard. If this field is left blank, this will default to the id of the default ledger balance."""

    originator_client_id: OptionalNullable[str] = UNSET
    """Client ID of the end customer."""


class TransferLedgerGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    ledger_id: NotRequired[str | None]
    originator_client_id: NotRequired[str | None]
